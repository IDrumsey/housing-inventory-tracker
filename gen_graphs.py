import json, os
from datetime import datetime

import utility

import matplotlib.pyplot as plt
import mplcyberpunk as punkplt

dataURI = os.getenv("formatted_historical_county_inventory_data_location")
saveDir = os.getenv("inventory-tracker-graph-save-location")

plt.style.use("cyberpunk")


fipsNameMapping = {39151: "Stark", 39153: "Summit"}


monthNumsMapping = {
    1: "Jan",
    2: "Feb",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}


def generateInventoryOverTimeGraph(
    fipsToGraph: list[int], colorsToUse: list[str] = ["#e01485", "#42e6f5"]
):
    # read the data json
    with open(dataURI, "r") as dataFile:
        data = json.load(dataFile)

    # only plot the counties specified
    data = [county for county in data if county["fips"] in fipsToGraph]

    for i, county in enumerate(data):
        # sort the inventory items by date
        inventory = sorted(county["inventory"], key=lambda x: (x["year"], x["month"]))
        dates = [
            f"{monthNumsMapping[x['month']]} '{str(x['year'])[2:]}" for x in inventory
        ]
        inventoryValues = [x["total_inventory"] for x in inventory]

        plt.plot(dates, inventoryValues, color=colorsToUse[i % len(colorsToUse)])

    punkplt.add_glow_effects()

    datesToShowOnXAxis = [date for i, date in enumerate(dates) if i % 4 == 0]
    plt.xticks(datesToShowOnXAxis, rotation=70)
    plt.ylabel("Total Inventory")

    plt.title(utility.generatePlotTitle(fipsToGraph))

    plt.subplots_adjust(bottom=0.2)

    now = datetime.now()
    saveFileName = now.strftime("%Y-%m-%d_%H-%M-%S")
    plt.savefig(f"{saveDir}\\{saveFileName}.png")
    # plt.show()
