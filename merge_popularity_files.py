import arrow
import csv
from collections import defaultdict
from decimal import Decimal
import numpy
from os import listdir
from os.path import isfile

with open("/Users/veronicatang/Downloads/prices/data/symbols_with_price.txt", "r") as f:
    symbols_with_price = set(l.strip() for l in f.readlines())

files = [f for f in listdir() if isfile(f) and f.endswith(".csv") and f.split(".csv")[0] in symbols_with_price]

out_columns = ["symbol", "date", "first_hld", "last_hld", "std_hld"]


def get_holding_stats(ts_holdings):
    """
    :ts_holdings: tuple of (timestamp arrow, holdings)
    """
    ts_holdings = sorted(ts_holdings)
    first_holding = ts_holdings[0][1]
    last_holding = ts_holdings[-1][1]
    holdings = [h[1] for h in ts_holdings]
    std_holding = numpy.std(holdings)
    return {
        "first_hld": first_holding,
        "last_hld": last_holding,
        "std_hld": str(Decimal(std_holding).quantize(Decimal("0.0001"))),
    }

print("Reading...")
rows = []
cnt = 0
for file in files:
    symbol = file.split(".csv")[0]
    date_to_holdings = defaultdict(list)
    # if any holding value is less than 100, skip this file
    skip_file = False
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            holding = int(row["users_holding"])
            if holding < 100:
                skip_file = True
                break
            ts = arrow.get(row["timestamp"])
            date = ts.date()
            date_to_holdings[date].append((ts, holding))
    if not skip_file:
        for date, ts_holdings in date_to_holdings.items():
            row = get_holding_stats(ts_holdings)
            row["symbol"] = symbol
            row["date"] = date
            rows.append(row)

    cnt += 1
    if cnt % 10 == 0:
        print(f"Finished {cnt} files")

print("Writing...")
with open("data/all_holdings.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=out_columns)
    writer.writeheader()
    writer.writerows(rows)


