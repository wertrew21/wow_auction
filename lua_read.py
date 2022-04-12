# lua_read.py
# Read file and sort out the file data getting rid of space, tap, newline.

### <PLAN> better to look into a way to get data in 'csv' form directly from 'Auctionator_mmddHHMM.lua'
###       and not to use this python module.

def read_file(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()

    hist_start = lines.index('AUCTIONATOR_PRICING_HISTORY = {\n')
    hist_end = lines.index('AUCTIONATOR_SHOPPING_LISTS = {\n')

    hist = lines[hist_start:hist_end]
    hist_strip = list(map(lambda x: x.strip(), hist))
    hist_join = ''.join(hist_strip)

    return hist_join