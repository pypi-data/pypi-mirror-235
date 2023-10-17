import logging
import re
from os.path import dirname, abspath
from pathlib import Path

import pytest

from igs_toolbox.extractor.readQR import main


def test_cli_without_parameters():
    with pytest.raises(SystemExit) as e:
        main([])
    assert e.value.code == 2


def test_cli_with_invalid_path(caplog):
    with pytest.raises(SystemExit) as e, caplog.at_level(logging.ERROR):
        main(["some-file-that-does-not-exist.json"])

    assert e.value.code == 1

    assert len(caplog.messages) == 1
    assert "does not point to a file" in caplog.messages[0]


def test_cli_with_invalid_paths(caplog):
    with pytest.raises(SystemExit) as e, caplog.at_level(logging.ERROR):
        main(
            ["some-file-that-does-not-exist.json some-file-that-does-not-exist-2.json"]
        )

    assert e.value.code == 1

    assert len(caplog.messages) == 1
    assert "does not point to a file" in caplog.messages[0]


def test_cli_with_valid_pdf_files(caplog, capsys):
    resources_dir = Path(dirname(abspath(__file__)))
    with caplog.at_level(logging.INFO):
        main(
            [
                str(resources_dir / Path("res/extractor_sample_a.pdf")),
                str(resources_dir / Path("res/extractor_sample_b.pdf")),
                str(resources_dir / Path("res/extractor_sample_c.pdf")),
            ]
        )

    stdout, stderr = capsys.readouterr()
    assert not stderr
    lines = stdout.splitlines()
    assert len(lines) == 3
    assert "extractor_sample_a\t685054b6-dcac-4f5b-8136-7ff604f49f90" in lines[0]
    assert "extractor_sample_b\tHello from the other side" in lines[1]
    assert "extractor_sample_c\t" in lines[2]


def test_cli_prints_version(capsys):
    with pytest.raises(SystemExit) as e:
        main(["-V"])

    assert e.value.code == 0

    stdout, _ = capsys.readouterr()
    lines = stdout.splitlines()

    assert len(lines) == 1
    assert re.fullmatch("readQR [+.0-9a-z]+", lines[0])
