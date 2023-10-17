import requests
import time
import datetime;
import json

__user = None
__channel = None
__thingSpeakChannelId = None
__thingSpeakApiKey = None

__last_send_time = 0

def send_init_request(data, log = True):
    url = 'https://weather-comp.region.mo/api/client/user'
    try:
        response = requests.post(url, json=data, timeout=5)
        
        if response.status_code == 200:
            result = response.json()
            global __user
            __user = result.get('data').get('user')
            global __channel
            __channel = __user.get('channel')
            global __thingSpeakChannelId
            __thingSpeakChannelId = __channel.get('thingSpeakChannelId')
            global __thingSpeakApiKey
            __thingSpeakApiKey = __channel.get('thingSpeakApiKey')
            if log:
                ct = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
                print('weather-comp::init>', ct, 'User authentication successful.')
        else:
            if log:
                ct = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
                print('weather-comp::init>', ct,'Request failed. Error code:', response.status_code)
    except requests.Timeout:
        if log:
            ct = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
            print('weather-comp::init>', ct,'Request timed out.')


def init(username, password, log = True):
    data = {
        'username': username,
        'password': password
    }
    send_init_request(data, log)

def send(data = {}, log = True):
    if __user is None or __channel is None or __thingSpeakChannelId is None or __thingSpeakApiKey is None:
        if log:
            ct = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
            print('weather-comp::send>', ct,'Please execute init() first.')
        return

    global __last_send_time
    current_time = time.time()
    if current_time - __last_send_time >= 28 or __last_send_time == 0:
        __last_send_time = current_time
    else:
        if log:
            ct = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
            print('weather-comp::send>', ct,'Request is too frequent. The interval between requests must be at least 30 seconds.')
        return
    
    if type(data) is not dict:
        if log:
            ct = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
            print('weather-comp::send>', ct,'The data must be of type dict.')
        return
    
    if data.get('LONG') is None and data.get('LAT') is None and data.get('PM2.5') is None and data.get('PM10') is None and data.get('CO') is None and data.get('SO2') is None and data.get('NO2') is None and data.get('O3') is None:
        if log:
            ct = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
            print('weather-comp::send>', ct,'The data must include at least one field.')
        return

    new_data = {
        'api_key': __thingSpeakApiKey,
        'field1': data.get('LONG'),
        'field2': data.get('LAT'),
        'field3': data.get('PM2.5'),
        'field4': data.get('PM10'),
        'field5': data.get('CO'),
        'field6': data.get('SO2'),
        'field7': data.get('NO2'),
        'field8': data.get('O3')
    }

    url = 'https://api.thingspeak.com/update.json'

    try:
        response = requests.post(url, json=new_data, timeout=5)
        
        if response.status_code == 200:
            result = response.json()
            if result == 0:
                if log:
                    ct = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
                    print('weather-comp::send>', ct,'Data upload failed.')
            else:
                if log:
                    ct = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
                    print('weather-comp::send>', ct,'Data upload successful.\n', json.dumps(result, sort_keys=True, indent=4))
        else:
            if log:
                ct = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
                print('weather-comp::send>', ct,'Request failed. Error code:', response.status_code)
    except requests.Timeout:
        if log:
            ct = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
            print('weather-comp::send>', ct,'Request timed out.')
