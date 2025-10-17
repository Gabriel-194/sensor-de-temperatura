#gabriel Ribeiro Kuchma

def conecta(ssid, senha):
    import network
    import time
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid,senha)
    for i in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station

#import urequests
#print("conectando...")
#station = conecta("KUCHMA", "K16122006")
#if not station.isconnected():
#    print("não conectado!...")
#else:
#    print("conectado!...")
#    print("acessando o site...")
#    response = urequests.get("https://www.ppgia.pucpr.br")
#    print("pagina acessada:")
#    print(response.text)
#    station.disconnect