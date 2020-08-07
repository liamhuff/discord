import requests
import json
USER_AGENT = open('USER_HEADER').read().strip()
API_KEY = open('FM_TOKEN').read().strip()
headers = {'agent': USER_AGENT}

request_data = {
    'api_key': API_KEY,
    'format': 'json'
}

def lastfm_get(request_data):
    url = 'http://ws.audioscrobbler.com/2.0/'
    request_data['api_key'] = API_KEY
    request_data['format'] = 'json'

    response = requests.get(url, headers=headers, params=request_data)
    return response


# user IS THE USERNAME OF THE USER, AS A STRING :
def get_recent_tracks(user):
    response = lastfm_get({
        'method': 'user.getrecenttracks',
        'user': user,
        'limit' : 5
    })

    # return nothing iff error occurs
    if response.status_code != 200:
        return None

    something = [t['artist']['#text'] + ' - ' + t['name'] for t in response.json()['recenttracks']['track']]
    return something

def str_recent_tracks(user):
    s = ''
    for track in get_recent_tracks(user):
        s += track + '\n'
    return s

