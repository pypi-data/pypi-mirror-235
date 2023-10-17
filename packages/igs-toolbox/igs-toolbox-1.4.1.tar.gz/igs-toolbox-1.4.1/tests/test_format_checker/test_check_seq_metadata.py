import pytest

from igs_toolbox.formatChecker.jsonChecker import check_seq_metadata
from igs_toolbox.formatChecker.seq_metadata_schema import (
    ValidationError,
    SeqMetadataKeys,
)


def test_valid_json_is_recognized(valid_json):
    check_seq_metadata(valid_json)


def test_invalid_json_is_rejected(valid_json):
    valid_json[SeqMetadataKeys.SEQUENCING_LAB_POSTAL_CODE] = "123"

    with pytest.raises(ValidationError, match="INVALID_SEQUENCING_LAB.POSTAL_CODE"):
        check_seq_metadata(valid_json)


def test_incomplete_json_is_rejected(valid_json):
    valid_json.pop(SeqMetadataKeys.SEQUENCING_LAB_DEMIS_LAB_ID)

    with pytest.raises(ValidationError, match="MISSING_SEQUENCING_LAB.DEMIS_LAB_ID"):
        check_seq_metadata(valid_json)


def test_invalid_json_leads_to_descriptive_error_messages(valid_json):
    valid_json[SeqMetadataKeys.SEQUENCING_LAB_POSTAL_CODE] = "123"
    valid_json[SeqMetadataKeys.ISOLATION_SOURCE] = "Invalid value"

    with pytest.raises(
        ValidationError,
        match="INVALID_ISOLATION_SOURCE; INVALID_SEQUENCING_LAB.POSTAL_CODE",
    ):
        check_seq_metadata(valid_json)


def test_valid_json_with_invalid_species_is_rejected(valid_json):
    valid_json[SeqMetadataKeys.SPECIES] = "Invalid species"

    with pytest.raises(ValidationError, match="INVALID_SPECIES"):
        check_seq_metadata(valid_json)
