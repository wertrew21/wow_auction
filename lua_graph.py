# lua_graph.py
# Plot time series graph with prices of item in Y-axis.

import os, csv
from time import time
from PIL import Image
import lua_re as lr
import matplotlib.pyplot as plt
import numpy as np
from lua_translation import trans_ko2en
dir = os.path.join(os.getcwd(), 'lua/')
files_dir = os.listdir(dir)
files_csv = lr.match_file(files_dir, lr.p_ext('csv'))

### [PLAN] Sort the code below out as 'function_name(fullpath)'.
timeseries_tmp = {}
for file in files_csv:
    fullpath = dir + file
    yyyymmdd = lr.get_time(file, lr.p_date)
    mmdd = int(yyyymmdd[4:])
    arr_tmp = []
    with open(fullpath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for (i, line) in enumerate(reader):
            arr_tmp.append(line)
            if i:
                line.append(mmdd)

    stats_arr = trans_ko2en(arr_tmp)
    labels = stats_arr.pop(0)
#   stats_arr = [ ['Mana Thistle', QTY, AVG, ... , mmdd],
#                 ['Terocone', QTY, AVG,   ...   , mmdd],
#                 [          ...           ]     ...     ]
#   labels = ['NAME', 'QTY', 'AVG', 'TOP', 'BTM']

    for arr in stats_arr:
        name = arr[0]
        stats = arr[1:-1]
        date = arr[-1]
        date_stats = [date] + stats

        keys = timeseries_tmp.keys()
        if name not in keys:
            timeseries_tmp[name] = []
        timeseries_tmp[name].append(date_stats)

for key in timeseries_tmp.keys():
    timeseries_tmp[key].sort()
#       timeseries_tmp = { 'Mana Thistle' : [[mmdd0, QTY0, AVG0, ... ], [mmdd1, QTY1, AVG1, ... ], ... ],
#                      'Terocone': [[ ... ], ... ], ... }
#       * 'mmdd[\d]' is sorted in ascending order as [\d] increases.


timeseries = {}
keys = timeseries_tmp.keys()
labels_date_stats = ['DATE'] + labels[1:]
# labels_date_stats = ['DATE', 'QTY', 'AVG', 'TOP', 'BTM']

for key in keys:
    y_stats_arr =[]
    stats_arr = timeseries_tmp[key]
    for stats in stats_arr:
        stats = list(map(int,stats))
        y_stats_arr.append(stats)
#       y_stats_arr = [[mmdd0, QTY0, AVG0, ... ], [mmdd1, QTY1, AVG1, ... ], ... ]

    dict_stats = {}
    for (i, label) in enumerate(labels_date_stats):
        dict_stats[label] = []
        for y_stats in y_stats_arr:
            dict_stats[label].append(y_stats[i])
#           dict_stats = {'DATE':[mmdd0, mmdd1, ... ], 'QTY':[QTY0, QTY1, ... ], 'AVG':[AVG0, AVG1, ... ], ... }

    timeseries[key] = dict_stats
#   timeseries = {'Mana Thistle' : {'QTY':[QTY0, QTY1, ... ], 'AVG':[AVG0, AVG1, ... ], ... },
#                     Terocone'  : {'QTY':[QTY0, QTY1, ... ], 'AVG':[AVG0, AVG1, ... ], ... },
#                       ...      : {                          ...                           } }

#   The example of choosing X, Y axes data:
#       'AVG' of 'Mana Thistle';   y_strtype = timeseries['Mana Thistle']['AVG']    <-- Y
#                                  y = list(map(int, y_strtype))
#       'DATE' of 'Mana Thistle';  timeseries['Mana Thistle']['DATE']  <-- X


################# Plot graph ###################
### [PLAN] 1. Add index and let each index shows date.
###        2. Iterate the code below
###        3. Save graph as 'LUA_GRAPH_yyyymmdd_HHMM.png'
###        4. (Additional) Violin plot

dir_img = os.path.join(os.getcwd(), 'img/')
keys = timeseries.keys()
for key in keys:
    y1 = timeseries[key]['AVG']
    y2 = timeseries[key]['QTY']
    t = timeseries[key]['DATE']
    x = range(len(y1))

    y1_int = list(map(lambda x: int(x) / 10000, y1))
    y1_max = max(y1_int)
    y1_min = min(y1_int)
    y2_int = list(map(int, y2))
    y2_max = max(y2_int)
    y2_min = min(y2_int)

    fig, ax1 = plt.subplots()
    ax1.plot(x, y1_int, linestyle='solid', linewidth=3, color='C1', label='AVG')
    ax1.set_xlabel('DATE', labelpad=10, fontsize=12)
    ax1.set_ylabel('Average Price [G]', color='C1', labelpad=12, fontsize=13)
    ax1.tick_params(axis='y', color='C1', labelcolor='C1', direction='in')

    ax2 = ax1.twinx()
    ax2.bar(x, y2, color='palegreen', label='QTY')
    ax2.set_ylabel('Quantity', color='limegreen', labelpad=12, fontsize=13)
    ax2.set_ylim(y2_min*0.7, y2_max*1.2)
    ax2.tick_params(axis='y', color='limegreen', labelcolor='limegreen', direction='in')

    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)

    ax1.legend(loc=(0.67, 1.02))
    ax2.legend(loc=(0.84, 1.02))

    xrange = []
    labels_xticks = []
    for (i, date) in enumerate(t):
        if i%5 == 0:
            date_str = str(date)
            xtick = '{}/{}'.format(date_str[:-2], date_str[-2:])
            if len(date_str) == 3:
                xtick = '0' + xtick
            labels_xticks.append(xtick)
            xrange.append(i)

    plt.xticks(xrange, labels_xticks)
    plt.title('      %s' %key, loc='left', fontdict={'fontsize':18}, pad=13)
    plt.savefig('{}tmp_{}.png'.format(dir, key), bbox_inches='tight', pad_inches=0.3)

    img_graph = Image.open('{}tmp_{}.png'.format(dir, key))
    img_item = Image.open('{}{}.jpg'.format(dir_img, key))
    icon_frame = Image.open('{}icon_frame.png'.format(dir_img))

    framed_img = Image.new('RGB', (icon_frame.size[0], icon_frame.size[1]))
    framed_img.paste(icon_frame, (0, 0))
    framed_img.paste(img_item, (4, 4))
    framed_img.thumbnail((img_item.size[0]*0.65, img_item.size[1]*0.65))

    new_img = Image.new('RGB', (img_graph.size[0], img_graph.size[1]))
    new_img.paste(img_graph, (0, 0))
    new_img.paste(framed_img, (87,22))
    new_img.save('{}LUA_GRAPH_[{}].png'.format(dir, key), 'PNG')

os.system('rm {}tmp*'.format(dir))