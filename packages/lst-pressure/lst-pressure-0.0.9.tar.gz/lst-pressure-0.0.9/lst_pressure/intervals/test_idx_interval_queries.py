import pytest
from .idx import Idx
from ..calender import generate_calendar
from ..utils import sun_stats
import datetime
from collections import Counter

LAT = 0
LNG = 0

calendar = [
    {"sun": sun_stats(LAT, LNG, dt), "dt": dt}
    for dt in generate_calendar("20230101", "20231231")
]
buffer = datetime.timedelta(minutes=10)


@pytest.fixture
def idx():
    idx = Idx()

    # Get intervals for each calendar day
    for i, entry in enumerate(calendar[:-1]):
        sun = entry.get("sun")

        # Today
        today_start = entry.get("dt")
        today_sunrise = sun.get("sunrise")
        today_sunset = sun.get("sunset")
        today_dusk = sun.get("dusk")

        # Tomorrow
        tomorrow_start = calendar[i + 1]["dt"]
        tomorrow_dawn = calendar[i + 1].get("sun").get("dawn")
        tomorrow_sunrise = calendar[i + 1].get("sun").get("sunrise")
        tomorrow_sunset = calendar[i + 1].get("sun").get("sunset")

        # Calculate intervals
        avoid_sunrise_start = (today_sunrise + buffer).timestamp()
        avoid_sunrise_end = (tomorrow_sunrise - buffer).timestamp()

        avoid_sunset_start = (today_sunset + buffer).timestamp()
        avoid_sunset_end = (tomorrow_sunset - buffer).timestamp()

        night_only_start = (today_dusk + buffer).timestamp()
        night_only_end = (tomorrow_dawn - buffer).timestamp()

        all_day_start = today_start.timestamp()
        all_day_end = tomorrow_start.timestamp()

        idx.insert(avoid_sunrise_start, avoid_sunrise_end, {"type": "AVOID_SUNRISE"})
        idx.insert(avoid_sunset_start, avoid_sunset_end, {"type": "AVOID_SUNSET"})
        idx.insert(night_only_start, night_only_end, {"type": "NIGHT_ONLY"})
        idx.insert(all_day_start, all_day_end, {"type": "ALL_DAY"})
    return idx


def get_valid_intervals(idx, start, end):
    return dict(
        Counter(
            interval[2]["type"]
            for interval in idx.get_intervals_containing(
                start.timestamp(), end.timestamp()
            )
        )
    )


tests = [
    {"dt": dt, "sun": sun_stats(0, 0, dt)}
    for dt in generate_calendar("20230601", "20230601")
]


@pytest.mark.parametrize("test", tests)
def test_for_0100_0200(idx, test):
    dt = test["dt"]
    start = dt + datetime.timedelta(hours=1)
    end = dt + datetime.timedelta(hours=2)
    valid_intervals = get_valid_intervals(idx, start, end)
    assert valid_intervals.get("ALL_DAY") == 1
    assert valid_intervals.get("AVOID_SUNRISE") == 1
    assert valid_intervals.get("AVOID_SUNSET") == 1
    assert valid_intervals.get("NIGHT_ONLY") == 1


@pytest.mark.parametrize("test", tests)
def test_for_1000_1400(idx, test):
    dt = test["dt"]
    start = dt + datetime.timedelta(hours=10)
    end = dt + datetime.timedelta(hours=14)
    valid_intervals = get_valid_intervals(idx, start, end)
    assert valid_intervals.get("ALL_DAY") == 1
    assert valid_intervals.get("AVOID_SUNRISE") == 1
    assert valid_intervals.get("AVOID_SUNSET") == 1


@pytest.mark.parametrize("test", tests)
def test_for_1000_1400(idx, test):
    dt = test["dt"]
    start = dt + datetime.timedelta(hours=10)
    end = dt + datetime.timedelta(hours=14)
    valid_intervals = get_valid_intervals(idx, start, end)
    assert valid_intervals.get("ALL_DAY") == 1
    assert valid_intervals.get("AVOID_SUNRISE") == 1
    assert valid_intervals.get("AVOID_SUNSET") == 1


@pytest.mark.parametrize("test", tests)
def test_sunrise_intervals_are_omitted(idx, test):
    dt = test["dt"]
    sun = sun_stats(LAT, LNG, dt)
    sunrise = sun.get("sunrise")
    before_sunrise = sunrise - buffer
    after_sunrise = sunrise + buffer
    valid_intervals = get_valid_intervals(idx, before_sunrise, after_sunrise)
    assert valid_intervals.get("ALL_DAY") == 1
    assert valid_intervals.get("AVOID_SUNRISE") == None
    assert valid_intervals.get("AVOID_SUNSET") == 1
