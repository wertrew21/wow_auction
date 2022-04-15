# api_data_extraction.py
# # 'rand' means the type number of random inchantments.

import os, csv

import api_re
from api_const import *
from api_read import read_file
from api_statistics import Statistics

dir = os.path.join(os.getcwd(), 'api/') 
files_dir = os.listdir(dir)
files_api = api_re.match_file(files_dir, api_re.p_api)
files_csv = api_re.match_file(files_dir, api_re.p_csv)
labels = ['NAME', 'QTY', 'AVG', 'TOP', 'BTM']
for file in files_api:
    file_check = file.replace('API', 'API_CSV').replace('txt', 'csv')
    if file_check in files_csv:
        continue

    hist = read_file(dir + file)            # 'hist' means the information containing id, total price, quantity 
                                            #  in 'API_yyyymmdd_HHMM.txt'.


    dict_ipq_tmp = api_re.price_quantity(hist)
    dict_npq = {}
    for item in item_select:
        id = kr_to_id.get(item)
        en = kr_to_en.get(item)
        dict_npq[en] = dict_ipq_tmp[id]
    
    stats = Statistics(dict_npq)        # dict_npq = {'Mana Thistle':[(prc0, qty0), (prc1, qty1), ...], ...}
    stats.rm_outlier()
    total_stats = stats.total()

    file_tmp = api_re.chg_ext(file, 'txt', 'csv')
    fullpath = dir + file_tmp.replace('API', 'API_CSV')

    try:
        with open(fullpath, 'w') as f:
            writer = csv.DictWriter(f, fieldnames =labels)
            writer.writeheader()
            for row in total_stats:
                writer.writerow(row)
    except IOError:
        print("I/O error")