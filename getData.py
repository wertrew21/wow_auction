import os, time, sys
from api_re import p_token

dir = os.getcwd()
fullpath = os.path.join(dir, 'getData.ign')
f = open(fullpath, 'r')
lines = f.readlines()
f.close()

(client_id, client_secret) = lines[-1].split(':')

cmd_result = os.popen('curl -u %s:%s \
                      -d grant_type=client_credentials "https://kr.battle.net/oauth/token"' \
                      %(client_id, client_secret))
token_str = cmd_result.read()
access_token = p_token.search(token_str).group('token')

date = time.strftime('%Y%m%d_%H%M')
fullpath_api = './api/API_{}.txt'.format(date)
#'./api/API_' + date + '.txt'

os.system('curl -o %s --header "Authorization: Bearer %s" \
         "https://kr.api.blizzard.com/data/wow/connected-realm/4419/auctions/6?namespace=dynamic-classic-kr&locale=kr_KR"' \
         %(fullpath_api, access_token))
