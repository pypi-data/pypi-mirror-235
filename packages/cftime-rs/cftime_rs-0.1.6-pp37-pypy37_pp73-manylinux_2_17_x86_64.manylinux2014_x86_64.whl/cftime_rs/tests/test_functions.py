import pytest
import cftime_rs
import datetime as dt


def test_num2date():
    arr = [1, 2, 3]
    units = "days since 1970-01-01"
    calendar = "standard"

    result = cftime_rs.num2date(arr, units, calendar)
    cf_calendar = cftime_rs.PyCFCalendar.from_str("standard")
    expected = [
        cftime_rs.PyCFDatetime.from_ymd(1970, 1, 2, cf_calendar),
        cftime_rs.PyCFDatetime.from_ymd(1970, 1, 3, cf_calendar),
        cftime_rs.PyCFDatetime.from_ymd(1970, 1, 4, cf_calendar),
    ]
    assert [i.ymd_hms() for i in result] == [i.ymd_hms() for i in expected]


def test_date2num():
    units = "days since 1970-01-01"
    calendar = "standard"

    cf_calendar = cftime_rs.PyCFCalendar.from_str("standard")
    dates = [
        cftime_rs.PyCFDatetime.from_ymd(1970, 1, 2, cf_calendar),
        cftime_rs.PyCFDatetime.from_ymd(1970, 1, 3, cf_calendar),
        cftime_rs.PyCFDatetime.from_ymd(1970, 1, 4, cf_calendar),
    ]
    expected = [1, 2, 3]
    result = cftime_rs.date2num(dates, units, calendar, dtype="i64")
    assert result == expected


def test_pydate2num():
    units = "days since 1970-01-01"
    calendar = "standard"
    dates = [
        dt.datetime(1970, 1, 2),
        dt.datetime(1970, 1, 3),
        dt.datetime(1970, 1, 4),
    ]
    expected = [1, 2, 3]
    result = cftime_rs.pydate2num(dates, units, calendar, dtype="i64")
    assert result == expected


def test_num2pydate():
    arr = [1, 2, 3]
    units = "days since 1970-01-01"
    calendar = "standard"

    result = cftime_rs.num2pydate(arr, units, calendar)
    result = [i.replace(tzinfo=None) for i in result]
    expected = [
        dt.datetime(1970, 1, 2),
        dt.datetime(1970, 1, 3),
        dt.datetime(1970, 1, 4),
    ]
    assert result == expected


def test_num2date_for_float():
    arr = [95795.0]
    units = "days since 1970-01-01"
    calendar = "standard"
    cf_calendar = cftime_rs.PyCFCalendar.from_str("standard")
    expected = [
        cftime_rs.PyCFDatetime.from_ymd(2232, 4, 12, cf_calendar),
    ]
    result = cftime_rs.num2date(arr, units, calendar)
    assert [i.ymd_hms() for i in result] == [i.ymd_hms() for i in expected]


def test_idempotence_of_num2pydate_then_pydate2num_for_float():
    dts = [
        dt.datetime(2000, 1, 1, 0, 0, 0),
        dt.datetime(2000, 1, 2, 1, 0, 0),
        dt.datetime(2000, 1, 3, 2, 0, 0),
    ]
    units = "days since 0000-01-01 00:00:00"
    calendar = "standard"
    encoded_numbers = cftime_rs.pydate2num(dts, units, calendar, dtype="f64")

    result = cftime_rs.num2pydate(encoded_numbers, units, calendar)
    assert result == dts


def test_float_issue_impl_xarray():
    """Found this issue implementating cftime_rs in xarray time unit
    tests suite
    """
    units = "days since 0001-01-01"
    times = [
        dt.datetime(1, 4, 1, 1),
        dt.datetime(1, 4, 1, 2),
        dt.datetime(1, 4, 1, 3),
        dt.datetime(1, 4, 1, 4),
    ]
    calendar = "standard"
    time = cftime_rs.pydate2num(times, units, calendar=calendar, dtype="f64")
    result = cftime_rs.num2pydate(time, units, calendar=calendar)

    assert times == result


def test_360_day_issue_impl_xarray():
    units = "days since 0001-01-01"
    times = [
        dt.datetime(1, 4, 1),
        dt.datetime(1, 4, 2),
        dt.datetime(1, 4, 3),
        dt.datetime(1, 4, 4),
        dt.datetime(1, 4, 5),
        dt.datetime(1, 4, 6),
    ]
    encoded_time = cftime_rs.pydate2num(times, units, calendar="360_day", dtype="i64")
    assert encoded_time == [90, 91, 92, 93, 94, 95]

    decoded_time = cftime_rs.num2pydate(encoded_time, units, calendar="360_day")
    assert decoded_time == times
