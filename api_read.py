# api_read.py
# This module truncates API data to contain necessary information.

def read_file(file):
    f = open(file, 'r')
    lines = f.read()
    f.close()

    hist_start = lines.index('"auctions":[')
    hist_end = lines.index('],"id":6,')

    hist = lines[hist_start:hist_end]

    return hist