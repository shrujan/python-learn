Celsius = [39.2, 36.5, 37.3, 37.8]

print ('****** Celcius to Farenheit *******')

# def celciusToFarenheit(x):
#     return (float(9)/5)*x + 32

# farenheit = list(map(celciusToFarenheit, Celsius))

farenheit = list(map(lambda c: (float(9)/5)*c + 32, Celsius))

print(farenheit)

print('*****Farenheit to Celcius*****')

Celsius1 = list(map(lambda f: round((float(5)/9)*(f-32), 2), farenheit))

print(Celsius1)
