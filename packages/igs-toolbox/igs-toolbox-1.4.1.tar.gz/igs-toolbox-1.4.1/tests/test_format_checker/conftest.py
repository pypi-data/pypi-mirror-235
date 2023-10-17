import pytest

from igs_toolbox.formatChecker.seq_metadata_schema import SeqMetadataKeys


@pytest.fixture
def valid_json():
    return {
        SeqMetadataKeys.PRIME_DIAGNOSTIC_LAB_FEDERAL_STATE: "Nordrhein-Westfalen",
        SeqMetadataKeys.LAB_SEQUENCE_ID: "NRZ-420",
        SeqMetadataKeys.MELDETATBESTAND: "EBCP",
        SeqMetadataKeys.DEMIS_NOTIFICATION_ID: "",
        SeqMetadataKeys.GEOGRAPHIC_LOCATION: "123",
        SeqMetadataKeys.PRIME_DIAGNOSTIC_LAB_ADDRESS: "Teststr. 666",
        SeqMetadataKeys.SEQUENCING_REASON: "other",
        SeqMetadataKeys.DATE_OF_SAMPLING: "2015-09-01",
        SeqMetadataKeys.DATE_OF_SEQUENCING: "2022-01-21",
        SeqMetadataKeys.SEQUENCING_INSTRUMENT: "Illumina_MiSeq",
        SeqMetadataKeys.SEQUENCING_STRATEGY: "WGS",
        SeqMetadataKeys.HOST: "Homo sapiens",
        SeqMetadataKeys.ADAPTER: "A-N703; A-S510",
        SeqMetadataKeys.SEQUENCING_LAB_ADDRESS: "Uni Testing, Universitätsstr. 69",
        SeqMetadataKeys.AUTHOR: "NRZ für gramnegative Krankenhauserreger",
        SeqMetadataKeys.SEQUENCING_LAB_NAME: "NRZ für gramnegative Krankenhauserreger",
        SeqMetadataKeys.ISOLATION_SOURCE: "Blood sample",
        SeqMetadataKeys.PRIME_DIAGNOSTIC_LAB_POSTAL_CODE: "12345",
        SeqMetadataKeys.SEQUENCING_LAB_POSTAL_CODE: "12345",
        SeqMetadataKeys.PRIME_DIAGNOSTIC_LAB_DEMIS_LAB_ID: "12345",
        SeqMetadataKeys.SEQUENCING_LAB_DEMIS_LAB_ID: "12345",
        SeqMetadataKeys.ISOLATE: "",
        "Files": [
            {
                SeqMetadataKeys.FILE_SHA256SUM: "9c1212ebb37b0850b55552104d7eac9cceee2be4b9ad7188a8615a1c3a5a7881",  # noqa: E501
                SeqMetadataKeys.FILE_NAME: "NRZ-420_S13_L001_R1_001.fastq.gz",
            },
            {
                SeqMetadataKeys.FILE_NAME: "NRZ-420_S13_L001_R2_001.fastq.gz",
                SeqMetadataKeys.FILE_SHA256SUM: "528be16bfe06cc07c305d434e94e8c9c0ee1109daf0873e0d75f7d1d74081ff4",  # noqa: E501
            },
        ],
        SeqMetadataKeys.NAME_AMP_PROTOCOL: "Nextera XT",
        SeqMetadataKeys.STATUS: "",
        SeqMetadataKeys.SPECIES: "Klebsiella pneumoniae (organism)",
        SeqMetadataKeys.SEQUENCING_LAB_FEDERAL_STATE: "Nordrhein-Westfalen",
        SeqMetadataKeys.SEQUENCING_PLATFORM: "ILLUMINA",
        SeqMetadataKeys.PRIME_DIAGNOSTIC_LAB_NAME: "Klinikum Testhausen",
        SeqMetadataKeys.DATE_OF_SUBMISSION: "2020-12-24",
    }
