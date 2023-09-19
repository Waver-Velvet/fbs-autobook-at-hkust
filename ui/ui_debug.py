import time
import time as t
from datetime import datetime, timedelta, date

import streamlit as st

import fbs

state = st.session_state

st.title("Book")

timeslot_date = date.fromisoformat("2023-09-27")
if not fbs.is_open() or not fbs.is_bookable(timeslot_date):
    begin, end = datetime.now(), max(fbs.open_time(), fbs.bookable_time_of(timeslot_date))
    remaining = end - datetime.now()
    progress_text = f"Waiting until the selected timeslot becomes bookable or FBS reopens ({end.isoformat()})...  Remaining: {remaining}"
    progress = st.progress(0, text=progress_text)
    while datetime.now() < end:
        remaining = end - datetime.now()
        percentage = 1 - (end - datetime.now()) / (end - begin)
        progress_text = f"Waiting until the selected timeslot becomes bookable or FBS reopens ({end.isoformat()})...  Remaining: {remaining}"
        progress.progress(percentage, text=progress_text)
        time.sleep(0.01)
