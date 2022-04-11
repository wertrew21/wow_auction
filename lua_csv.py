# lua_csv.py
import csv
import lua_data_extraction as lde

labels = ['NAME', 'QUANTITY', 'AVERAGE', 'TOP_PRICE', 'BTM_PRICE']

try:
    with open(lde.fname, 'w') as f:
        writer = csv.DictWriter(f, fieldnames =labels)
        writer.writeheader()
        for row in lde.total_stats:
            writer.writerow(row)
except IOError:
    print("I/O error")