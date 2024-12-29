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

    entity_id = "sensor.temperatura_balkon_temperature"

    try:
        response = urequests.get("http://homeassistant.local:8123/api/states/"+entity_id, headers=headers) 
    except:
        balkon_temp = None
    else:
        if response.status_code == 200:
            res = response.json()
            balkon_temp = res['state']
        else:
            balkon_temp = None

    return balkon_temp



def main():
    connect()
    d.clear()
    d.center("Temperatura", color=st7789.YELLOW)
    d.center("na balkonie", color=st7789.YELLOW)
    block_line = d.line
    while True:
        # d.clear()
        balkon_temp = get_biuro_data()
        d.center(f"     {balkon_temp} *C     ", color=st7789.GREEN, line=block_line)
        for i in range(0,33):
            sleep(1)
            d.print(text="  .",line=block_line+60, col=i*6)
        d.print(text="                              ",line=block_line+60)

main()
    