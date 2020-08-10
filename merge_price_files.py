import csv
from os import listdir
from os.path import isfile

files = [f for f in listdir() if isfile(f) and f.endswith(".csv")]

in_columns = ["date", "open", "high", "low", "close", "volume"]
out_columns = ["symbol"] + in_columns

print("Reading...")
rows = []
cnt = 0
for file in files:
    symbol = file.split(".csv")[0]
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["symbol"] = symbol
            rows.append(row)
    cnt += 1
    if cnt % 10 == 0:
        print(f"Finished {cnt} files")

print("Writing...")
with open("data/all_prices.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=out_columns)
    writer.writeheader()
    writer.writerows(rows)

with open("data/symbols_with_price.txt", "w") as f:
    for file in files:
        f.write(file.split(".csv")[0] + "\n")
