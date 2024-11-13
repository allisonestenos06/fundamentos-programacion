# Programa que dice si llueve o no

is_raining = True
humidity = 100
water_mm = 2.3

if is_raining:
    if water_mm > 4:
        print("Llueve mucho")
    else:
        print("Chispea")
else:
    if humidity < 20:
        print("Qué seco está el ambiente...")
    elif humidity > 20 and humidity < 60:
        print("Se está bien")
    else:
        print("Parece que va a llover")
