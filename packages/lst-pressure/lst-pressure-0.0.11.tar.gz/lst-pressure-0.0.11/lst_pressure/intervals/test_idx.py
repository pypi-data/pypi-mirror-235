"""
test_utc_intervals.py
"""
import datetime
from collections import Counter
import pytest
from .idx import Idx, Interval
from ..calender import generate_calendar
from ..utils import sun_stats, utc_to_lst, LST_DAY_DEC

LAT = "-30:42:39.8"
LNG = "21:26:38.0"


calendar = [
    {"sun": sun_stats(LAT, LNG, dt), "dt": dt}
    for dt in generate_calendar("20230101", "20231231")
]


@pytest.fixture
def idx():
    """fixture"""
    idx = Idx()

    # Get intervals for each calendar day
    for i, entry in enumerate(calendar[:-1]):
        sun = entry.get("sun")

        # Today
        today_start = entry.get("dt")
        today_dawn = sun.get("dawn")
        today_dawn_lst = utc_to_lst(today_dawn, LAT, LNG)
        today_sunrise = sun.get("sunrise")
        today_sunrise_lst = utc_to_lst(today_sunrise, LAT, LNG)
        today_sunset = sun.get("sunset")
        today_sunset_lst = utc_to_lst(today_sunset, LAT, LNG)
        today_dusk = sun.get("dusk")
        today_dusk_lst = utc_to_lst(today_dusk, LAT, LNG)

        # Tomorrow
        tomorrow_dawn = calendar[i + 1].get("sun").get("dawn")
        tomorrow_dawn_lst = utc_to_lst(tomorrow_dawn, LAT, LNG)
        tomorrow_dawn_lst = (
            tomorrow_dawn_lst + LST_DAY_DEC
            if (tomorrow_dawn_lst - today_dawn_lst) < (LST_DAY_DEC / 2)
            else tomorrow_dawn_lst
        )

        tomorrow_sunrise = calendar[i + 1].get("sun").get("sunrise")
        tomorrow_sunrise_lst = utc_to_lst(tomorrow_sunrise, LAT, LNG) + LST_DAY_DEC
        tomorrow_sunrise_lst = (
            tomorrow_sunrise_lst + LST_DAY_DEC
            if (tomorrow_sunrise_lst - today_sunrise_lst) < (LST_DAY_DEC / 2)
            else tomorrow_sunrise_lst
        )

        tomorrow_sunset = calendar[i + 1].get("sun").get("sunset")
        tomorrow_sunset_lst = utc_to_lst(tomorrow_sunset, LAT, LNG)
        tomorrow_sunset_lst = (
            tomorrow_sunset_lst + LST_DAY_DEC
            if (tomorrow_sunset_lst - today_sunset_lst) < (LST_DAY_DEC / 2)
            else tomorrow_sunset_lst
        )

        # AVOID_SUNRISE
        idx.insert(
            Interval(
                today_sunrise_lst,
                tomorrow_sunrise_lst,
                {
                    "sun": sun,
                    "dt": today_start,
                    "type": "AVOID_SUNRISE",
                    "solar_0": today_sunrise,
                    "solar_1": tomorrow_sunrise,
                },
            )
        )

        # AVOID_SUNSET
        idx.insert(
            Interval(
                today_sunset_lst,
                tomorrow_sunset_lst,
                {
                    "sun": sun,
                    "dt": today_start,
                    "type": "AVOID_SUNSET",
                    "solar_0": today_sunset,
                    "solar_1": tomorrow_sunset,
                },
            )
        )

        # AVOID_SUNRISE_SUNSET (1/2): sunrise - sunset
        idx.insert(
            Interval(
                today_sunrise_lst,
                today_sunset_lst + LST_DAY_DEC
                if today_sunset_lst < today_sunrise_lst
                else today_sunset_lst,
                {
                    "sun": sun,
                    "dt": today_start,
                    "type": "AVOID_SUNRISE_SUNSET",
                    "solar_0": today_sunrise,
                    "solar_1": today_sunset,
                },
            )
        )

        # AVOID_SUNRISE_SUNSET (2/2): sunset - sunrise
        idx.insert(
            Interval(
                today_sunset_lst,
                tomorrow_sunrise_lst,
                {
                    "sun": sun,
                    "dt": today_start,
                    "type": "AVOID_SUNRISE_SUNSET",
                    "solar_0": today_sunset,
                    "solar_1": tomorrow_sunrise,
                },
            )
        )

        # NIGHT_ONLY
        idx.insert(
            Interval(
                today_dusk_lst,
                tomorrow_dawn_lst,
                {
                    "sun": sun,
                    "dt": today_start,
                    "type": "NIGHT_ONLY",
                    "solar_0": today_dusk,
                    "solar_1": tomorrow_dawn,
                },
            )
        )

    return idx


def summarize_results(intervals):
    """
    summarize_results
    Count data.type value occurrences in a list of intervals
    """
    return dict(Counter(interval[2]["type"] for interval in intervals))


observations = [
    {"lst_start": 8.15, "lst_end": 11.5, "constraints": {"type": "NIGHT_ONLY"}},
    {"lst_start": 1, "lst_end": 8},
    {"lst_start": 22, "lst_end": 22.5, "constraints": {"type": "AVOID_SUNRISE_SUNSET"}},
]


@pytest.mark.parametrize("observation", observations)
def test_observations(idx, observation):
    lst_start = observation.get("lst_start")
    lst_end = observation.get("lst_end")
    constraints = observation.get("constraints", {})
    interval_type = constraints.get("type", None)
    query = Interval(lst_start, lst_end)
    candidate_intervals = idx.get_intervals_containing(query)
    filtered_intervals = [
        i
        for i in candidate_intervals
        if interval_type is None or i[2]["type"] == interval_type
    ]
    stats = summarize_results(filtered_intervals)
    print("\n", stats) # TODO - Now I need to create some valid test cases
