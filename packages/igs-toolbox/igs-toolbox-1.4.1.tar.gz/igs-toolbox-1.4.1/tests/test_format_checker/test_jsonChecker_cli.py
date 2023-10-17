import json
import logging
import re

import pytest

from igs_toolbox.formatChecker.jsonChecker import main


def test_cli_without_parameters():
    with pytest.raises(SystemExit) as e:
        main([])

    assert e.value.code == 2


def test_cli_with_invalid_path(caplog):
    with pytest.raises(SystemExit) as e, caplog.at_level(logging.ERROR):
        main(["-i", "some-file-that-does-not-exist.json"])

    assert e.value.code == 1

    assert len(caplog.messages) == 1
    assert "does not point to a file" in caplog.messages[0]


def test_cli_with_non_json_file(caplog, tmp_path):
    (f := tmp_path / "file").write_text("something")
    with pytest.raises(SystemExit) as e, caplog.at_level(logging.ERROR):
        main(["-i", str(f)])

    assert e.value.code == 1

    assert len(caplog.messages) == 1
    assert "is not a valid json file" in caplog.messages[0]


def test_cli_with_valid_json_file(valid_json, caplog, capsys, tmp_path):
    (f := tmp_path / "file").write_text(json.dumps(valid_json))
    with caplog.at_level(logging.INFO):
        main(["-i", str(f)])

    assert len(caplog.messages) == 1
    assert "JSON file adheres to seqMetadata schema" in caplog.messages[0]

    stdout, stderr = capsys.readouterr()
    assert not stderr
    lines = stdout.splitlines()
    assert len(lines) == 1
    assert "adheres to seqMetadata schema" in lines[0]


def test_with_invalid_json_file(valid_json, caplog, tmp_path):
    valid_json["SEQUENCING_LAB.POSTAL_CODE"] = "123"
    valid_json["ISOLATION_SOURCE"] = "Invalid value"

    (f := tmp_path / "file").write_text(json.dumps(valid_json))
    with pytest.raises(SystemExit) as e, caplog.at_level(logging.ERROR):
        main(["-i", str(f)])

    assert e.value.code == 1
    assert len(caplog.messages) == 1
    assert "does not adhere to the seqMetadata schema" in caplog.messages[0]


def test_cli_prints_version(capsys):
    with pytest.raises(SystemExit) as e:
        main(["-V"])

    assert e.value.code == 0

    stdout, _ = capsys.readouterr()
    lines = stdout.splitlines()

    assert len(lines) == 1
    assert re.fullmatch("jsonChecker [+.0-9a-z]+", lines[0])
