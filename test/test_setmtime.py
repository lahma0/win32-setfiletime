import os
import time

import pytest

from win32_setfiletime import setmtime


def getmtime(filepath):
    return os.path.getmtime(str(filepath))


def test_setmtime(tmp_path):
    filepath = tmp_path / "test_setmtime.txt"
    timestamp = 946681200
    filepath.touch()
    setmtime(filepath, timestamp)
    assert getmtime(filepath) == timestamp


def test_timestamp_negative(tmp_path):
    filepath = tmp_path / "test_timestamp_negative.txt"
    timestamp = -5694948000
    filepath.touch()
    setmtime(filepath, timestamp)
    assert getmtime(filepath) == timestamp


def test_timestamp_with_nanoseconds(tmp_path):
    filepath = tmp_path / "test_timestamp_with_nanoseconds.txt"
    timestamp = 737206464.123456789
    filepath.touch()
    setmtime(filepath, timestamp)
    assert pytest.approx(getmtime(filepath), timestamp)


def test_timestamp_lower_bound(tmp_path):
    filepath = tmp_path / "test_timestamp_lower_sdfds.dds"
    timestamp = -11644473599
    filepath.touch()
    setmtime(filepath, timestamp)
    assert getmtime(filepath) == timestamp


def test_timestamp_exceeds_lower_bound(tmp_path):
    filepath = tmp_path / "test_timestamp_exceeds_lower_bound.txt"
    timestamp = -11644473600
    filepath.touch()
    with pytest.raises(ValueError):
        setmtime(filepath, timestamp)


def test_timestamp_far_in_the_future(tmp_path):
    filepath = tmp_path / "test_timestamp_far_in_the_future.txt"
    timestamp = 64675581821
    filepath.touch()
    setmtime(filepath, timestamp)
    assert getmtime(filepath) == timestamp


def test_timestamp_exceeds_upper_bound(tmp_path):
    filepath = tmp_path / "test_timestamp_exceeds_upper_bound.txt"
    timestamp = 1833029933770.9551616
    filepath.touch()
    with pytest.raises(ValueError):
        setmtime(filepath, timestamp)


def test_file_does_not_exist(tmp_path):
    filepath = tmp_path / "test_file_does_not_exist.txt"
    timestamp = 123456789
    with pytest.raises(FileNotFoundError):
        setmtime(filepath, timestamp)


def test_file_already_opened_read(tmp_path):
    filepath = tmp_path / "test_file_already_opened_read.txt"
    timestamp = 123456789
    filepath.touch()
    with open(str(filepath), "r"):
        setmtime(filepath, timestamp)
    assert getmtime(filepath) == timestamp


def test_file_already_opened_write(tmp_path):
    filepath = tmp_path / "test_file_already_opened_write.txt"
    timestamp = 123456789
    with open(str(filepath), "w"):
        setmtime(filepath, timestamp)
    assert getmtime(filepath) == timestamp


def test_file_already_opened_exclusive(tmp_path):
    filepath = tmp_path / "test_file_already_opened_write.txt"
    timestamp = 123456789
    with open(str(filepath), "x"):
        setmtime(filepath, timestamp)
    assert getmtime(filepath) == timestamp


def test_file_unicode(tmp_path):
    filepath = tmp_path / "𤭢.txt"
    timestamp = 123456789
    filepath.touch()
    setmtime(filepath, timestamp)
    assert getmtime(filepath) == timestamp


def test_forward_slash(tmp_path):
    folder = tmp_path / "foo" / "bar" / "baz"
    filepath = folder / "test_forward_slash.txt"
    timestamp = 123456789
    folder.mkdir(exist_ok=True, parents=True)
    filepath.touch()
    setmtime(str(filepath).replace(r"\\", "/"), timestamp)
    assert getmtime(filepath) == timestamp


def test_ctime_not_modified(tmp_path):
    filepath = tmp_path / "test_ctime_not_modified.txt"
    filepath.touch()
    before = os.path.getctime(str(filepath))
    time.sleep(0.1)
    setmtime(filepath, 123456789)
    assert os.path.getctime(str(filepath)) == before


def test_atime_not_modified(tmp_path):
    filepath = tmp_path / "test_atime_not_modified.txt"
    filepath.touch()
    before = os.path.getatime(str(filepath))
    time.sleep(0.1)
    setmtime(filepath, 123456789)
    assert os.path.getatime(str(filepath)) == before
