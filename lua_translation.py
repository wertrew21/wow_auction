# lua_translation.py
# KR ---> EN

from lua_const import kr_to_en

def trans_ko2en(list_csv):
    result = [list_csv[0]]
    for i in range(1, len(list_csv)):
        name_ko = list_csv[i][0]
        name_en = kr_to_en.get(name_ko)
        tmp = list_csv[i]
        tmp[0] = name_en
        result.append(tmp)
    return result