import argparse
import json
import logging
import os
import re
import sys
from os.path import basename
from pathlib import Path

from typing import Any

import jsonschema

import igs_toolbox
from igs_toolbox.formatChecker.seq_metadata_schema import (
    seq_metadata_schema,
    SeqMetadataKeys,
    ValidationError,
)

SCHEMA_NAME = "seqMetadata"


def validate_species(pathogen: str, species: str) -> bool:
    """Validate species field."""
    # get vocabulary for species
    answer_set_path = os.path.dirname(__file__) / Path(
        f"res/species/txt/answerSet{pathogen}.txt"
    )
    if not answer_set_path.is_file():
        logging.error(f"{answer_set_path} does not point to a file. Aborting.")
        return False

    with open(answer_set_path, "r") as species_file:
        species_list = [line.strip() for line in species_file]

    if species not in species_list:
        logging.error(f"{species} is not a valid species for pathogen {pathogen}.")
        return False
    return True


def check_seq_metadata(json_data: dict[SeqMetadataKeys | str, Any]) -> None:
    """Validate the sequence metadata."""
    validator = jsonschema.Draft202012Validator(schema=seq_metadata_schema)
    errors = list(validator.iter_errors(json_data))
    error_str = []
    for error in errors:
        if error.validator == "required":
            matched_prop = re.search("'(.*)'", error.message)
            if matched_prop:
                error_str.append("MISSING_" + matched_prop.group(1))
            else:
                error_str.append(
                    "MISSING_" + error.message[1 : -len("' is a required property")]
                )
        else:
            error_str.append("INVALID_" + error.relative_path[-1])

    # some validation.py rules cannot be implemented in jsonschema directly,
    # thus check them here programmatically
    if (
        SeqMetadataKeys.SPECIES in json_data
        and SeqMetadataKeys.MELDETATBESTAND in json_data
        and not validate_species(
            json_data[SeqMetadataKeys.MELDETATBESTAND],
            json_data[SeqMetadataKeys.SPECIES],
        )
    ):
        error_str.append("INVALID_SPECIES")

    if len(error_str) > 0:
        raise ValidationError("; ".join(error_str))


# Read command line arguments
def parse(args=None):
    parser = argparse.ArgumentParser(prog=basename(__file__).split(".")[0])
    parser.add_argument("-i", "--input", required=True, help="Filepath to json file.")
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {igs_toolbox.__version__}",
    )
    args = parser.parse_args(args)
    return args


def main(args=None):
    input_file = parse(args).input
    # read json file
    if not os.path.isfile(input_file):
        logging.error(f"{input_file} does not point to a file. Aborting.")
        sys.exit(1)

    with open(input_file, "r") as jsonfile:
        try:
            json_data = json.loads(jsonfile.read())
        except json.decoder.JSONDecodeError:
            logging.error(f"{input_file} is not a valid json file. Aborting.")
            sys.exit(1)

    # get schema
    try:
        check_seq_metadata(json_data)
    except ValidationError as e:
        logging.error(
            f"FAILURE: JSON file does not adhere to the {SCHEMA_NAME} schema: {e}."
        )
        sys.exit(1)

    logging.info(f"SUCCESS: JSON file adheres to {SCHEMA_NAME} schema.")
    print(f"SUCCESS: JSON file {input_file} adheres to {SCHEMA_NAME} schema.")


if __name__ == "__main__":
    main()
