# exe_cron.sh
# Add a code to execute this shell script on crontab edit mode.

filedir="/root/wow_auction"

cd $filedir
python getData.py
python api_data_extraction.py
python api_table.py
python api_graph.py
phthon api_move_file.py
