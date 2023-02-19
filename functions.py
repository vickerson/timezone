#write a function to calculate timezone differenc
from datetime import datetime
def tiemezone_difference(country1, country2):
     str_country1=country1
     str_country2=country2
     country1=datetime.strptime(str_country1, "%m/%d/%Y %H:%M:%S")
     country2=datetime.strptime(str_country2, "%m/%d/%Y %H:%M:%S")
     if country2>country1:
          return country2-country1
     else:     
      return country1-country2
     return f'Difference is {delta.days} days'