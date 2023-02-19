# Իմպորտ ենք անում մոդուլները
import requests
#էս տոկենը ավտորիզացիայի համարա , առանց սրա API ն չի աշխատի , պատկերացրու cookie ա
TOKEN = "aWkfCnsTVzEUmslvCmFn"
#Հլը որ մենակ Եվրոպական երկրների համարա աշխատում
def get_country_timezone(region: str,country: str) -> str:
    path = f'https://timezoneapi.io/api/timezone/?{region}/{country}&token={TOKEN}'
    response = requests.get(path)
    data = response.json()
    if data['meta']['code'] == "200":
        location = data['data']['timezone']['location']
        time = data['data']['datetime']['date_time']
        return time
    else:
        return data['meta']['message']

def get_current_timezone():
    response = requests.get(f'https://timezoneapi.io/api/ip/?token={TOKEN}')
    data = response.json()
    if data['meta']['code'] == "200":
        location = data['data']['timezone']['location']
        time = data['data']['datetime']['date_time']
        return time
    else:
        return data['meta']['message']