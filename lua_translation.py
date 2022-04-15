# lua_translation.py
# KR ---> EN

from lua_const import kr_to_en

# lines_csv = [[ <list> of 1st line ],
#              [ <list> of 2nd line ],
#                       ...            ]
def trans_ko2en(lines_csv):
    result = [lines_csv[0]]
    for i in range(1, len(lines_csv)):
        name_ko = lines_csv[i][0]
        name_en = kr_to_en.get(name_ko)
        line = lines_csv[i]
        line[0] = name_en
        result.append(line)
    return result