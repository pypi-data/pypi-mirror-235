from setuptools import setup
from pathlib import Path

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="igs-toolbox",
    description="A toolbox to check whether files follow a predefined schema.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.rki.de/DE/Content/Infekt/IGS/IGS_node.html",
    author="IGS Developers",
    author_email="IGS-Developers@rki.de",
    license="MIT",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "jsonChecker=igs_toolbox.formatChecker.jsonChecker:main",
            "readQR=igs_toolbox.extractor.readQR:main",
        ],
    },
    python_requires=">=3.8",
    install_requires=[
        "jsonschema>=4.16.0",
        "pandas>=2.1.1",
        "pdf2image>=1.16.3",
        "opencv-python>=4.8.0.76",
    ],
    extras_require={
        "test": ["pytest"],
    },
    include_package_data=True,
)
