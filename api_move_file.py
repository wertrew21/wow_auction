# api_move_file.py

import os
import api_re


dir = os.path.join(os.getcwd(), 'api/')
files_dir = os.listdir(dir)
dir_api_dst = os.path.join(dir, 'storage/api/')
dir_grp_dst = os.path.join(dir, 'storage/graph/')
dir_csv_dst = os.path.join(dir, 'storage/csv/')
dir_tbl_dst = os.path.join(dir, 'storage/table/')

files_api = api_re.match_file(files_dir, api_re.p_api)
files_api.sort()
files_api.reverse()

files_csv = api_re.match_file(files_dir, api_re.p_csv)
files_csv.sort()
files_csv.reverse()

files_tbl = api_re.match_file(files_dir, api_re.p_tbl)
files_tbl.sort()
files_tbl.reverse()

while len(files_api) > 56:
    file_api = files_api.pop()
    file_csv = files_csv.pop()
    file_tbl = files_tbl.pop()
    os.replace(os.path.join(dir, file_api), os.path.join(dir_api_dst, file_api))
    os.replace(os.path.join(dir, file_csv), os.path.join(dir_csv_dst, file_csv))
    os.replace(os.path.join(dir, file_tbl), os.path.join(dir_tbl_dst, file_tbl))

files_grp = api_re.match_file(files_dir, api_re.p_grp)
files_grp.sort()
files_grp.reverse()

while len(files_grp) > 8:
    file = files_grp.pop()
    os.replace(os.path.join(dir, file), os.path.join(dir_grp_dst, file))