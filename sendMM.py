import json
import sys
import requests

login_data = {
    'login_id':'YOURUSERNAME',
    'password':'YOURPASSWORD'
    }
BASEURL = 'https://yourmattermostserverurl'
TEAMNAME = 'yourteamname'

args = sys.argv

if len(args)<2:
    print("At least two arguments needed: @user date time message")
    exit()

target = sys.argv[1]
message = " ".join(sys.argv[2:])

# for testing print("To", target,"Message:", message)

login = requests.post(f'{BASEURL}/api/v4/users/login', data = json.dumps(login_data))
token = login.headers['Token']
headers = {"Authorization": f"Bearer {token}"}
me_id = login.json()['id']
me = login.json()['username']

channel_id = None
if target.find("@")==0:

    team = requests.get(f'{BASEURL}/api/v4/teams/name/{TEAMNAME}', headers=headers)
    team_id = team.json()['id']
    team_param = {"in_team": team_id, "per_page": 200}
    users = requests.get(f'{BASEURL}/api/v4/users', headers=headers, params=team_param)
    users = users.json()
    user = target[1:].lower()
    user_id = None
    for u in users:
        if u['username'].lower()==user or u['nickname'].lower()==user:
            user_id=u['id']
    if user_id is not None:
        twousers = json.dumps([user_id,me_id])
        channel = requests.post(f'{BASEURL}/api/v4/channels/direct', headers=headers,data=twousers)
        channel_id = channel.json()['id']

elif target.find("#")==0:
    r = requests.get(f'{BASEURL}/api/v4/users/{me_id}/teams/{team_id}/channels', headers=headers)
    channels = r.json()
    channel = target[1:].lower()
    for c in channels:
        if c['name'].lower()==channel or c['display_name'].lower()==channel:
            channel_id=c['id']

if channel_id is not None:
    payload = {'channel_id': channel_id,
           'message': message}
    r = requests.post(f'{BASEURL}/api/v4/posts', headers=headers,data=json.dumps(payload))
