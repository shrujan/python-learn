

countryList = open('TextFiles/Country.txt')

countries = {}

while True:
    country = countryList.readline()

    if country:
        c1 = country.split(':')
        print(c1[0] , c1[1])
        countries[c1[0]] = c1[1]

    else:
        print('-------------------------------------')
        break



countryList.close()

print(countries)