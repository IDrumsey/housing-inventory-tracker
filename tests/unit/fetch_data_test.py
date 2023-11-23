import os

import src.fetch_data as fetch_data

import pytest


@pytest.fixture
def remove_downloaded_file():
    yield
    os.remove(os.getenv("raw_historical_county_inventory_data_save_location"))


def test_download_latest(remove_downloaded_file):
    fetch_data.download_latest(
        "https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_County_History.csv",
        os.getenv("raw_historical_county_inventory_data_save_location"),
    )

    assert os.path.isfile(
        os.getenv("raw_historical_county_inventory_data_save_location")
    )
