# lua_re.py
# Regular expressions used in data extraction, and functions related.

import re


###  <DONE> replaced with p_ext  ### p_csv = re.compile(r'(?P<name>.*)[.]csv')          
p_auct = re.compile(r'Auctionator_(\d{2})(\d{2})(\d{4})[.]lua')
p_npq = re.compile(r'\["(?P<name>\D+(?!is))"\] = \{(?P<prc_qty>.*?),\}')
p_pq = re.compile(r'\["\d+"\] = "(?P<prc>\d+):(?P<qty>\d+)"')
p_token = re.compile(r'"access_token":"(?P<token>\w*?)"')

def p_ext(ext):
    pattern = re.compile(r'(?P<name>.*)[.]' + ext)
    return pattern

def price_quantity(s):              # input for s is supposed to be 'hist_join'(refer to lua_read.py)
    item_list = p_npq.findall(s)                    # item_list[0] =                                     
                                                    #       ('ITEM_NAME', '["ddddddd"] = "PRC0:QTY0",
                                                    #                                    "PRC1:QTY1", ... ')
    name_prc_qty = {}                 
    for i in range(len(item_list)):               
        name = item_list[i][0]                      # 'ITEM_NAME'
        prc_qty = p_pq.findall(item_list[i][1])     # [('PRC0', 'QTY0'), ('PRC1', 'QTY1'), ... ]
        name_prc_qty[name] = prc_qty

    return name_prc_qty             # {'ITEM_NAME':[('PRC0', 'QTY0'), ('PRC1', 'QTY1'), ... ]), ...  ( ... )]


def match_file(files_dir, p):
    result = []
    for file in files_dir:
        if p.match(file): result.append(file)
    return result

###  <DONE> merged into function 'match_file'  ###
# def csv_file(files_dir):
#     result = []
#     for file in files_dir:
#         if p_csv.match(file): result.append(file)
#     return result

def name_auct2csv(file):
    tmp = p_auct.match(file)
    result = 'LUA_2021{0}{1}_{2}.csv'.format(tmp.group(1), tmp.group(2), tmp.group(3))
    #"LUA" + '_' + '2021' + tmp.group(1) + tmp.group(2) + '_' + tmp.group(3) + '.csv'
    return result

def chg_ext(file, ext):
    result = p_ext('csv').sub("\g<name>.{}".format(ext), file)
    return result