# api_table.py
# Create table from csv file. The label(=attribute) is below.
#
#           NAME   QTY   AVG   TOP   BTM      
#
# which means, 'name of item', 'quantity', 'average price', 'top(most expensive) price', 'bottom(cheapest) price' in the order above.

import csv, os
import pandas as pd
import matplotlib.pyplot as plt
import api_re, api_move_file

def csv2table(fullpath):
    result = []
    with open(fullpath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            result.append(line)

    fig, ax = plt.subplots(1, 1)
    column_labels = result.pop(0)
    df = pd.DataFrame(result, columns=column_labels)


    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values,
             colLabels=df.columns,
             colColours=['yellow']*len(df.columns),
             loc="center")

    dir, file = os.path.split(fullpath)
    name_fig = api_re.chg_ext(file, 'csv', 'png')
    fullpath = os.path.join(dir, name_fig.replace('API_CSV', 'API_TABLE'))
    plt.savefig(fullpath)
    plt.close('all')

dir = os.path.join(os.getcwd(), 'api/') 
files_dir = os.listdir(dir)
files_csv = api_re.match_file(files_dir, api_re.p_ext('csv'))
files_tbl = api_re.match_file(files_dir, api_re.p_tbl)
for file in files_csv:
    file_check = file.replace('CSV', 'TABLE').replace('csv', 'png')
    if file_check in files_tbl:
        continue
    fullpath = dir + file
    csv2table(fullpath)

    api_move_file.cp_file(file_check)