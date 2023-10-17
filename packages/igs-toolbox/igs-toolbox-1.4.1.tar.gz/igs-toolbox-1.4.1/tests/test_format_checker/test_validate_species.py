import logging

from igs_toolbox.formatChecker.jsonChecker import validate_species


def test_validateSpecies_works_on_valid_species():
    assert validate_species("CVDP", "Greek letter omicron (qualifier value)") is True


def test_validateSpecies_works_on_invalid_species(caplog):
    with caplog.at_level(logging.ERROR):
        assert validate_species("NEIP", "Some species which does not exist") is False
        assert "not a valid species" in caplog.messages[-1]


def test_validateSpecies_fails_on_unknown_pathogen(caplog):
    with caplog.at_level(logging.ERROR):
        assert validate_species("AAAA", "Some species which does not exist") is False
        assert "does not point to a file" in caplog.messages[-1]
