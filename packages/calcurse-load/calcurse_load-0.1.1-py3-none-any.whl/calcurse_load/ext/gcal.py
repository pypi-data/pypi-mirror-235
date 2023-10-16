from __future__ import annotations
import json
import glob
import hashlib
import logging
import io
from functools import partial
from pathlib import Path
from datetime import datetime
from typing import List, Iterator, Optional, TYPE_CHECKING

from .abstract import Extension
from .utils import yield_lines

if TYPE_CHECKING:
    from gcal_index.__main__ import GcalAppointmentData

# loads any JSON files in ~/.local/data/calcurse_load/*.json,

# one line in the appointment file
CalcurseLine = str


def pad(i: int) -> str:
    return str(i).zfill(2)


def create_calcurse_timestamp(epochtime: Optional[int]) -> str:
    """
    Create a string that represents the time in Calcurses timestamp format
    """
    if epochtime is None:
        return ""
    dt = datetime.fromtimestamp(epochtime)
    # localize to the current timezone
    dt = dt.astimezone()
    return f"{pad(dt.month)}/{pad(dt.day)}/{dt.year} @ {pad(dt.hour)}:{pad(dt.minute)}"


def create_calcurse_note(event_data: GcalAppointmentData, notes_dir: Path) -> str:
    """
    Creates the notes file if it doesn't already exist.

    Notes file contains the Google Calendar description, a link
    to the event, and any other metadata.
    """
    note_info: List[str] = []
    if event_data["summary"] is not None:
        note_info.append(event_data["summary"])
    if event_data["event_link"] is not None:
        note_info.append(event_data["event_link"])
    if event_data["description"]["text"] is not None:
        note_info.append(event_data["description"]["text"])
    if len(event_data["description"]["links"]) > 0:
        note_info.append("\n".join([a["email"] for a in event_data["attendees"]]))
    note = "\n".join(note_info)
    sha = hashlib.sha1(note.encode()).hexdigest()
    with (notes_dir / sha).open("w") as nf:
        nf.write(note)
    return sha


def create_calcurse_event(
    event_data: GcalAppointmentData, notes_dir: Path, logger: logging.Logger
) -> Optional[CalcurseLine]:
    """
    Takes the exported Google Calendar info, and creates
    a corresponding Calcurse 'apts' line, and note
    """
    if event_data["start"] is None:
        logger.warning(f"Event {event_data} has no start time")
        return None
    note_hash: str = create_calcurse_note(event_data, notes_dir)
    start_str = create_calcurse_timestamp(event_data["start"])
    end_str = create_calcurse_timestamp(event_data["end"])
    if end_str == "":
        return f"{start_str} -> {start_str}>{note_hash} |{event_data['summary']} [gcal]"
    else:
        return f"{start_str} -> {end_str}>{note_hash} |{event_data['summary']} [gcal]"


def is_google_event(appointment_line: CalcurseLine) -> bool:
    return appointment_line.endswith("[gcal]")


class gcal_ext(Extension):
    def load_json_events(self) -> Iterator[GcalAppointmentData]:
        json_files: List[str] = glob.glob(
            str(self.config.calcurse_load_dir / "gcal" / "*.json")
        )
        if not json_files:
            self.logger.warning(
                "No json files found in '{}'".format(str(self.config.calcurse_load_dir))
            )
        else:
            for event_json_path in json_files:
                with open(event_json_path, "r") as json_f:
                    yield from json.load(json_f)

    def load_calcurse_apts(self) -> Iterator[CalcurseLine]:
        """
        Loads in the calcurse appointments file, removing any google appointments
        """
        for apt in yield_lines(self.config.calcurse_dir / "apts"):
            if not is_google_event(apt):
                yield apt

    def pre_load(self) -> None:
        """
        - read in and filter out google events
        - create google events from JSON
        - write back both event types
        """
        self.logger.warn("gcal: running pre-load hook")

        filtered_apts: List[CalcurseLine] = list(self.load_calcurse_apts())
        self.logger.info(f"Found {len(filtered_apts)} non-gcal events")
        calcurse_func = partial(
            create_calcurse_event,
            notes_dir=self.config.calcurse_dir / "notes",
            logger=self.logger,
        )
        google_apts: List[CalcurseLine] = [
            ev for ev in map(calcurse_func, self.load_json_events()) if ev is not None
        ]
        self.logger.info(
            f"Writing {len(google_apts)} gcal events to calcurse appointments file"
        )

        events = filtered_apts + google_apts
        try:
            events.sort(key=lambda x: datetime.strptime(x[:10], "%m/%d/%Y"))
        except Exception as e:
            self.logger.error(f"Error sorting events: {e}")

        buf = io.StringIO()
        for event in events:
            buf.write(event)
            buf.write("\n")

        (self.config.calcurse_dir / "apts").write_text(buf.getvalue())

    def post_save(self) -> None:
        self.logger.warn("gcal: doesn't have a post-save hook!")
