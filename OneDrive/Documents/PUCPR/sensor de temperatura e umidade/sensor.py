#Gabriel Ribeiro Kuchma
from wifi_lib import conecta

import urequests
import machine
import time
import dht

#Inicializando os componentes
temperatura = dht.DHT11(machine.Pin(4))
rele = machine.Pin(2,machine.Pin.OUT)

#conexao com o wifi
print("conectando...")
station = conecta("KUCHMA","K16122006")
if not station.isconnected():
    print("não conectado")
else:
    print("conectado!!")

API_KEY = 'X1MQ6UNE3NEWTTJ7'
#loop infinito pra realizar ações
while True:
    temperatura.measure()
    temp = (temperatura.temperature())
    umid = (temperatura.humidity())

    print("temperatura: {:.1f}°C, Umidade::{:.0f}%".format(temp,umid))
    if temp > 31 or umid > 70:
        rele.value(1)
        #envia dados para o thingspeak
        try:
            url = "https://api.thingspeak.com/update?api_key={}&field1={}&field2={}".format(API_KEY,umid,temp)
            response = urequests.get(url)
            print("dados enviados para ThingSpeak, status",response.status_code)
            response.close()
        except Exception as e:
            print("erro ao enviar:",e)
    else:
        rele.value(0)
        print("rele desligado,dados não enviados")

    time.sleep(20)