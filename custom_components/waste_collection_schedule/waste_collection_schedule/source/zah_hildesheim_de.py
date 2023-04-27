import datetime
from waste_collection_schedule import Collection

TITLE = "Zweckverband Abfallwirtschaft Hildesheim" # Title will show up in README.md and info.md
DESCRIPTION = "Source script for ZAH Hildesheim"  # Describe your source
URL = "https://www.zah-hildesheim.de/"  # Insert url to service homepage. URL will show up in README.md and info.md
TEST_CASES = {  # Insert arguments for test cases to be used by test_sources.py script
    "TestName1": {"arg1": 100, "arg2": "street"},
    "TestName2": {"arg1": 200, "arg2": "road"},
    "TestName3": {"arg1": 300, "arg2": "lane"}
}

API_URL = "https://public.api.hi.abfuhrkalender.de/v1-3-0/"
ICON_MAP = {   # Optional: Dict of waste types and suitable mdi icons
    "DOMESTIC": "mdi:trash-can",
    "RECYCLE": "mdi:recycle",
    "ORGANIC": "mdi:leaf",
}


class Source:
    def __init__(self, arg1, arg2):  # argX correspond to the args dict in the source configuration
        self._arg1 = arg1
        self._arg2 = arg2

    def fetch(self):

        #  replace this comment with
        #  api calls or web scraping required
        #  to capture waste collection schedules
        #  and extract date and waste type details

        entries = []  # List that holds collection schedule

        entries.append(
            Collection(
                date = datetime.datetime(2020, 4, 11),  # Collection date
                t = "Waste Type",  # Collection type
                icon = ICON_MAP.get("Waste Type"),  # Collection icon
            )
        )

        return entries
