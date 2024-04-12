c = float(input('Informe a temperatura em ºC: '))
k = c + 273
f = (c * 1.8) + 32
print('\nTemperaturas:\nCelsius = {:.2f}°C\nFahrenheit = {:.2f}ºF\nKelvin = {:.2f}K'.format(c, f, k))
