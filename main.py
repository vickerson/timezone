from utils import get_country_timezone, get_current_timezone
from functions import tiemezone_difference

#country A
A = input("Country A:")
#country B
B = input("Country B:")

REGIONS = ['Africa', 'Europe', 'Asia', 'America', ]
region = 'Europe'
#get timezones
A = get_country_timezone(region, A)
B = get_country_timezone(region, B)
difference = tiemezone_difference(A, B)
print(difference)