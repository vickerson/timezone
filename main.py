from utils import get_country_timezone, get_current_timezone
from functions import tiemezone_difference

#You can check an example of output 
#print(get_country_timezone("Paris"))
#country A
A = input()
#country B
B = input()

REGIONS = ['Africa', 'Europe', 'Asia', 'America', ]
region = 'Europe'
#get timezones
A = get_current_timezone(region, A)
B = get_country_timezone(region, B)
difference = tiemezone_difference(A, B)
print(difference)