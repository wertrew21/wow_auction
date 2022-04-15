import os, csv

import lua_re
from lua_const import *
from lua_read import read_file
from lua_statistics import Statistics

dir = os.path.join(os.getcwd(), 'lua/') 
files_dir = os.listdir(dir)
files_auct = lua_re.match_file(files_dir, lua_re.p_auct)

labels = ['NAME', 'QTY', 'AVG', 'TOP', 'BTM']
for file in files_auct:
    hist = read_file(dir + file)                # 'hist' means AUCTIONATOR_PRICING_HISTORY in 'Auctionator_mmddHHMM.lua'.
    dict_npq_tmp = lua_re.price_quantity(hist)
    dict_npq = {}
    for item in item_select:
        dict_npq[item] = dict_npq_tmp[item]

    stats = Statistics(dict_npq)
    stats.rm_outlier()
    total_stats = stats.total()

    fullpath = dir + lua_re.name_auct2csv(file)

    try:
        with open(fullpath, 'w') as f:
            writer = csv.DictWriter(f, fieldnames =labels)
            writer.writeheader()
            for row in total_stats:
                writer.writerow(row)
    except IOError:
        print("I/O error")