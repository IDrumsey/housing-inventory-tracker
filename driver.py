import os
import fetch_data, format_data, gen_graphs

county_historical_data_csv = "https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_County_History.csv"
county_historical_data_save_file = os.environ.get(
    "raw_historical_county_inventory_data_save_location"
)


def main():
    fetch_data.download_latest(
        county_historical_data_csv, county_historical_data_save_file
    )

    format_data.formatMonthlyCountyHistoricalData()

    gen_graphs.generateInventoryOverTimeGraph()


if __name__ == "__main__":
    main()
