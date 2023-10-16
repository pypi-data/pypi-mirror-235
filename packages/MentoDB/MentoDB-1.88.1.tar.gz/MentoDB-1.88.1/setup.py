from setuptools import setup, find_packages

setup(
    name         = "MentoDB",
    version      = "1.88.1",
    url          = "https://github.com/fswair/MentoDB",
    description  = "Sqlite3 based powerful database project.",
    keywords     = ["MentoDB", "SQL", "ORM"],

    author       = "Mert Sırakaya",
    author_email = "usirakaya@ogr.iu.edu.tr",

    license      = "GPLv3+",
    classifiers  = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3"
    ],

    # ? Paket Bilgileri
    packages         = find_packages(),
    python_requires  = ">=3.10",
    install_requires = open("./MentoDB/requirements.txt", encoding="utf-8").read().splitlines(),
    entry_points = {
        "console_scripts": [
            "mento = MentoDB.cli:get_cli",
        ]
    },

    long_description_content_type = "text/markdown",
    long_description              = open("./MentoDB/README.md", encoding="utf-8").read(),
    include_package_data          = True
)