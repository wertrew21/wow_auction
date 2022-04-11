import os, csv

import lua_re
from lua_read import read_file
from lua_statistics import Statistics

#!! data below to be moved to another file.
#?? function that an input is translated into the english, ID output?
ext_obj = ['마나 엉겅퀴', '테로열매', '악몽의 덩굴',
            '불의 근원', '어둠의 근원', '마나의 근원', '생명의 근원', '물의 근원']
kr_to_en = {'마나 엉겅퀴':'Mana Thistle', '테로열매':'Terocone', '악몽의 덩굴':'Nightmare Vine',
            '불의 근원':'Primal Fire', '어둠의 근원':'Primal Shadow', '마나의 근원':'Primal Mana', 
            '생명의 근원':'Primal Life', '물의 근원':'Primal Water'}
en_to_id = {'Mana Thistle':22793, 'Terocone':22789, 'Nightmare Vine':22792,
            'Primal Fire':21884, 'Primal Shadow':22456, 'Primal Mana':22457, 'Primal Life':21886, 'Primal Water':21885}

data_dir = os.getcwd() + '/lua/'
files_in_dir = os.listdir(data_dir)
ah_flist = lua_re.ah_file(files_in_dir)


#!! Change the code below to iterate for all files.

hist = read_file(data_dir + ah_flist[0])
tmp_npq = lua_re.price_quantity(hist)
ext_npq = {}
for item in ext_obj: ext_npq[item] = tmp_npq[item]


stats = Statistics(ext_npq)
stats.rm_outlier()
total_stats = stats.total()

fname = data_dir + lua_re.output_cname(ah_flist[0])