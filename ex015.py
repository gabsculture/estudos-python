#conversao de temperatura
#celsius pra kelvin tc + 273
# kelvin pra celsius tk - 273
# celsius em fahrenreit tc/5 = tf -32/9

temperaturaCelsius = float(input('qual a temperatura em Celsius ?'))
fahrenreit = temperaturaCelsius * 9/5 + 32
kelvin = temperaturaCelsius + 273
print("em celsius {}, em farenheit {}, em kelvin {}".format(temperaturaCelsius,fahrenreit, kelvin))