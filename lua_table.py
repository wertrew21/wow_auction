# lua_table.py
import csv, os
import pandas as pd
import matplotlib.pyplot as plt

import lua_data_extraction as lde
import lua_re
from lua_translation import trans_ko2en

def csv2table(fullpath):
    tmp_result = []
    with open(fullpath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            tmp_result.append(line)

    result = trans_ko2en(tmp_result)

    fig, ax = plt.subplots(1, 1)
    column_labels = result.pop(0)
    df = pd.DataFrame(result, columns=column_labels)


    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values,
             colLabels=df.columns,
             colColours=['yellow']*len(df.columns),
    #         rowLabels=[i+1 for i in range(len(result))],
    #         rowColours=['yellow']*8,
             loc="center")
    #plt.show()
    dir, file = os.path.split(fullpath)
    name_fig = lua_re.chg_ext(file, 'png')
    fullpath = os.path.join(dir, name_fig)
    plt.savefig(fullpath)
    plt.close('all')


dir = lde.dir
files_dir = lde.files_dir
files_csv = lua_re.match_file(files_dir, lua_re.p_ext('csv'))

for file in files_csv:
    fullpath = dir + file
    csv2table(fullpath)