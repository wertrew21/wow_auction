# lua_re.py
# Regular expressions used in data extraction, and functions related.

import re

p_npq = re.compile(r'\["(?P<name>\D+(?!is))"\] = \{(?P<prc_qty>.*?),\}')
p_pq = re.compile(r'\["\d+"\] = "(?P<prc>\d+):(?P<qty>\d+)"')
p_dir = re.compile(r'Auctionator_(\d{2})(\d{2})(\d{4})[.]lua')
p_token = re.compile(r'"access_token":"(?P<token>\w*?)"')

def price_quantity(s):              # input for s is supposed to be 'hist_join'(refer to lua_read.py)
    item_list = p_npq.findall(s)    # item_list[0] =                                     
                                    #   ('ITEM_NAME', '["6840255"] = "PRC0:QTY0",
                                    #                                "PRC1:QTY1", ... ')
    name_prc_qty = {}
    for i in range(len(item_list)):
        name = item_list[i][0]       # ITEM_NAME
        prc_qty = p_pq.findall(item_list[i][1])        # [(PRC0, QTY0), (PRC1, QTY1), ... ]
        name_prc_qty[name] = prc_qty

    return name_prc_qty             # {'ITEM_NAME':[(PRC0, QTY0), (PRC1, QTY1), ... ]), ...  ( ... )]


def ah_file(files_in_dir):
    result = []
    for file in files_in_dir:
        if p_dir.match(file): result.append(file)
    return result

def output_cname(input_f):
    tmp = p_dir.match(input_f)
    result = "LUA" + '_' + '2021' + tmp.group(1) + tmp.group(2) + '_' + tmp.group(3) + '.txt'
    return result