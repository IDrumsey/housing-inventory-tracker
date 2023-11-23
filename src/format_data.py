import json, os
import pandas as pd

county_historical_data_save_file = os.getenv(
    "raw_historical_county_inventory_data_save_location"
)
county_historical_formatted_data_save_file = os.getenv(
    "formatted_historical_county_inventory_data_location"
)


def formatMonthlyCountyHistoricalData(fipsCountiesToExtract: list[int]):
    """
    Extracts and formats the data from the monthly county historical data csv
    """

    # load the raw data into a pandas frame
    df = pd.read_csv(county_historical_data_save_file)

    for countyFIPCode in fipsCountiesToExtract:
        # extract the rows for this county
        countyRows = df[df["county_fips"] == countyFIPCode]

        if len(countyRows) > 0:
            try:
                with open(
                    county_historical_formatted_data_save_file, "r"
                ) as databankFile:
                    databank = json.load(databankFile)

            except FileNotFoundError:
                databank = []

            # try to find a pre-existing object in our formatted data
            databankCountyObj = [
                county for county in databank if county.get("fips") == countyFIPCode
            ]

            if len(databankCountyObj) == 0:
                # the object doesn't already exist so create it

                databankCountyObj = {"fips": countyFIPCode, "inventory": []}

            else:
                # already exists, so just get it out of array form
                databankCountyObj = databankCountyObj[0]

            # now for each row from the raw data, extract the needed data and add to the in memory databank county object
            for index, row in countyRows.iterrows():
                monthYear = row["month_date_yyyymm"]
                year = monthYear // 100
                month = monthYear % 100

                totalInventory = int(row["total_listing_count"])

                # check if this month/year data has already been recorded
                alreadyRecorded = (
                    len(
                        [
                            monthItem
                            for monthItem in databankCountyObj.get("inventory")
                            if monthItem.get("month") == month
                            and monthItem.get("year") == year
                        ]
                    )
                    > 0
                )

                if not alreadyRecorded:
                    # add this data as a new item for this county
                    databankCountyObj.get("inventory").append(
                        {
                            "month": month,
                            "year": year,
                            "total_inventory": totalInventory,
                        }
                    )

            # replace the old county object with the updated one
            found = False
            for i, countyItem in enumerate(databank):
                if countyItem.get("fips") == countyFIPCode:
                    # remove old item
                    databank[i] = databankCountyObj
                    found = True

            if not found:
                # not a previously recorded county, add as new
                databank.append(databankCountyObj)

            with open(county_historical_formatted_data_save_file, "w") as databankFile:
                json.dump(databank, databankFile, indent=2)
