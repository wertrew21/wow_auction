# api_re.py
# Regular expressions used in data extraction, and functions related.

import re
 
p_api = re.compile(r'API_(\d{4})(\d{4})[_](\d{4})[.]txt')
p_grp = re.compile(r'API_GRAPH.*')
p_csv = re.compile(r'API_CSV.*')
p_tbl = re.compile(r'API_TABLE.*')
p_ipq = re.compile(r'"item":\{"id":(?P<id>\d+).*?[,]"buyout":(?P<prc>\d+)[,]"quantity":(?P<qty>\d+)')
#   {"id":300425889,"item":{"id":27681},"bid":111800,"buyout":120000,"quantity":6,"time_left":"SHORT"}
p_token = re.compile(r'"access_token":"(?P<token>\w*?)"')
p_date = re.compile(r'API_CSV[_](?P<yyyy>\d{4})(?P<mmdd>\d{4})[_](?P<HHMM>\d{4})')


def get_time(file, p):
    m = p.match(file)
    yyyy = m.group(1)
    mmdd = m.group(2)
    HHMM = m.group(3)
    return (yyyy, mmdd, HHMM)


def p_ext(ext):
    pattern = re.compile(r'(?P<name>.*)[.]' + ext)
    return pattern


def price_quantity(s):
    # input for s is supposed to be 'hist_join'(refer to api_read.py)

    item_list = p_ipq.findall(s)                                                
    # item_list[0] = ("id0", "total_prc0", "qty0")                                                       
    id_prc_qty = {}
    for (id, total_prc, qty) in item_list:
        id_prc_qty[id] = []
    for (id, total_prc, qty) in item_list:
        id_prc_qty[id].append((int(int(total_prc)/int(qty)), int(qty)))
    return id_prc_qty             
           # {'id':[('PRC0', 'QTY0'), ('PRC1', 'QTY1'), ... ]), ...  ( ... )]


def match_file(files_dir, p):
    result = []
    for file in files_dir:
        if p.match(file): result.append(file)
    return result


def chg_ext(file, ext_from, ext_to):
    result = p_ext(ext_from).sub("\g<name>.{}".format(ext_to), file)
    return result