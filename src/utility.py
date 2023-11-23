import requests

fipsDataSource = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"


def getCountyNameFromFIPS(fip: int) -> str:
    with requests.get(fipsDataSource) as response:
        if response.status_code == 200:
            data = response.json()

            state = str(fip)[:2]
            county = str(fip)[2:]

            # find the county data in the json
            for feature in data["features"]:
                if (
                    feature["properties"]["STATE"] == state
                    and feature["properties"]["COUNTY"] == county
                ):
                    foundCounty = feature

                    return foundCounty.get("properties").get("NAME")

            raise Exception(f"Could not find the county data for the fip code {fip}")

        else:
            raise Exception("Failed to fetch fips data source.")


def generatePlotTitle(fips: list[int]) -> str:
    """
    Generates the name of the graph based on the counties being graphed
    """

    countyNames = [getCountyNameFromFIPS(fip) for fip in fips]

    if len(countyNames) > 1:
        return f"Housing Inventory over Time: {' '.join(countyNames)}"

    else:
        if len(countyNames) == 1:
            return f"{countyNames[0]} County Housing Inventory over Time"

        else:
            raise Exception(f"No county names found for fips codes {' '.join(fips)}")
