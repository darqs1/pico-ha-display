import network
import urequests
from time import sleep

import libs.st7789py as st7789
from display.display import Display
import env

# initialize the display
d = Display()
# line = d.typewriter('Loading....',line=line)

def connect():
    # Connect to WiFi
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(env.wifi_name,env.wifi_key)
    while wlan.isconnected() == False:
        d.print('Waiting for connection')
        sleep(1)
    ip = str(wlan.ifconfig()[0])
    d.print("Connected, IP: ")
    d.typewriter(ip)
    sleep(2)

def get_biuro_data():
    bearer = env.bearer
    headers = {"Authorization" : f"Bearer {bearer}" }

    entities = [
        "sensor.temperatura_balkon_temperature",
        "sensor.temperatura_salon_temperature",
        "sensor.temperatura_salon_2_temperature",
        ]

    values = []

    for entity_id in entities:

        try:
            response = urequests.get("http://homeassistant.local:8123/api/states/"+entity_id, headers=headers) 
        except:
            entity_value = None
        else:
            if response.status_code == 200:
                res = response.json()
                entity_value = res['state']
            else:
                entity_value = None
        
        values.append(entity_value)
        
    return values



def main():
    connect()
    d.clear()
    d.center("Temperatura", color=st7789.YELLOW)
    d.center("na zewnatrz", color=st7789.YELLOW)
    block_line = d.line
    d.line = d.line + 40
    d.center("w salonie", color=st7789.YELLOW)
    while True:
        # d.clear()
        balkon_temp, salon_temp, salon_temp2 = get_biuro_data()
        d.center(f"     {balkon_temp} *C     ", color=st7789.GREEN, line=block_line-20)
        d.center(f"     {salon_temp2} *C     ", color=st7789.GREEN, line=block_line+90)
        d.center(f"     {salon_temp} *C     ", color=st7789.GREEN, line=block_line+125)
        for i in range(0,33):
            sleep(1)
            d.print(text="  .",line=block_line+200, col=i*6)
        d.print(text="                              ",line=block_line+200)

main()
    