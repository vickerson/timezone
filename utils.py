# Իմպորտ ենք անում մոդուլները
import requests

#էս տոկենը ավտորիզացիայի համարա , առանց սրա API ն չի աշխատի , պատկերացրու cookie ա
TOKEN = "aWkfCnsTVzEUmslvCmFn"
# Get
response = requests.get(f'https://timezoneapi.io/api/timezone/Paris&token={TOKEN}')

def get_country_timezone(region, country):
    path = f'https://timezoneapi.io/api/timezone/?{region}/{country}&token={TOKEN}'
    response = requests.get(path)
    data = response.json()
    if data['meta']['code'] == 200:
        location = data['data']['timezone']['location']
        time = data['data']['datetime']['date_time_txt']
        return time
    else:
        return data['meta']['message']

def get_current_timezone():
    return requests.get(f'https://timezoneapi.io/api/ip/?token={TOKEN}')
