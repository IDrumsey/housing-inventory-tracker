# housing-inventory-tracker

Creates a line graph showing inventory in a United States county using FIPs codes.

## How to Generate the Graph

1. Set your environment variables.

You need a couple environment variables

| Key                                                 | Description                                                               | Example                                       |
| --------------------------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------- |
| raw_historical_county_inventory_data_save_location  | The file location and name where you want to save the downloaded raw data | "./data/raw-data.csv"                         |
| formatted_historical_county_inventory_data_location | The file location and name where you want to save the formatted data      | "./data/formatted-data.json"                  |
| inventory-tracker-graph-save-location               | The file location where you want to save the generated graphs             | "C:\Users\someUser\Desktop\generated-graphs\" |

_Notice that the inventory-tracker-graph-save-location env variable is JUST THE LOCATION. I'll probably change the other two to match that, but haven't done it yet._

2. Open a terminal in the project root directory.
3. Run `pip install -r requirements.txt`. This will install the required dependencies.
4. Run `python driver.py` which will download the raw data, format the raw data, and generate the graph image from the formatted data.
