# exe_cron.sh
# Add a code to execute this shell script on crontab edit mode.

filedir="/root/wow_auction"
timenow=$(date "+%Y%m%d_%H:%M")

cd $filedir
python getData.py
python api_data_extraction.py
python api_table.py
python api_graph.py
python api_move_file.py

git add .
git commit -m"Automatically pushed. @ ${timenow}"
git push
