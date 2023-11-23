import os, argparse
from src import fetch_data, format_data, gen_graphs

county_historical_data_csv = "https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_County_History.csv"
county_historical_data_save_file = os.environ.get(
    "raw_historical_county_inventory_data_save_location"
)


def main(counties: list[int], colors: list[str]):
    fetch_data.download_latest(
        county_historical_data_csv, county_historical_data_save_file
    )

    format_data.formatMonthlyCountyHistoricalData(counties)

    gen_graphs.generateInventoryOverTimeGraph(counties, colors)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Housing Inventory Tracker CLI")
    parser.add_argument(
        "--counties",
        nargs="+",
        type=int,
        required=True,
        help="List of county FIPs to graph",
    )

    parser.add_argument(
        "--colors",
        nargs="+",
        type=str,
        help="List of colors to use for the lines on the graph",
    )

    args = parser.parse_args()

    # custom args validation
    if args.colors is not None:
        if len(args.colors) is not len(args.counties):
            raise Exception(
                f"You provided {len(args.colors)} colors, but {len(args.counties)} are needed because you passed {len(args.counties)} counties."
            )

    main(args.counties, args.colors)
