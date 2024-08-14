#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    base_url = 'https://www.reddit.com/'
    data = {'grant_type': 'password',
            'username': 'Hot_Seat_8723',
            'password': '252003ahmed'}
    auth = requests.auth.HTTPBasicAuth('iCqNlw7qgaMnkYySRxoVkA',
                                        'k7IeJGPZkGEG2S317NDgKJs4fnm26A')
    res = requests.post(base_url + 'api/v1/access_token',
                        data=data,
                        headers={'user-agent': 'k-fetcher by Hot_Seat_8723'},
                        auth=auth)
    dic = res.json()
    token = 'bearer ' + dic['access_token']
    base_url = 'https://oauth.reddit.com/'
    headers = {'Authorization': token,
                'User-Agent': 'k-fetcher by Hot_Seat_8723'}
    payload = {'q': subreddit, 'limit': 1, 'sort': 'relevance'}
    response = requests.get(base_url + '/subreddits/search',
                            headers=headers,
                            params=payload)
    try:
        response = response.json().get('data')
        response = response.get('children')[0].get('data').get('subscribers')
        return response
    except Exception as e:
        return 0
