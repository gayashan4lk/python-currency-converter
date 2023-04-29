def fahrenheit_to_celsius(temperature: float):
    celsius_temp: float = (temperature - 32) * 5 / 9
    return round(celsius_temp, 3)

