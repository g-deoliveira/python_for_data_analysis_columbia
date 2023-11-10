import csv

headers = ["product_id", "quantity", "price"]
data = [
    ["abc-123", 10, 12.99],
    ["mno-801", 1, 43.49],
    ["abp-003", 1, 43.49],
]

with open('purchases.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for row in data:
        writer.writerow(row)


data_io = []
with open('purchases.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers_io = next(reader)
    for row in reader:
        data_io.append(row)

assert headers_io == headers

# note that this assert will fail because the contents
# in data_io were read as strings
# assert data_io == data

# so if we convert the original data to strings,
# this assert passes
assert data_io == [[str(elm) for elm in row] for row in data]
