import requests

def divisas():
    # access_key = "a60971011d8b2e279340c4bea4543539"
    solicitud =requests.get("http://apilayer.net/api/live?access_key=a60971011d8b2e279340c4bea4543539")
    lista = requests.get("http://apilayer.net/api/list?access_key=a60971011d8b2e279340c4bea4543539")
    lana = solicitud.json()
    items = lana['source']
    monedas = lista.json()
    monedas1 = monedas['currencies']['MXN']
    conversion = lana['quotes']['USDMXN']
    pregunta = input('Cuantos dolares quieres convertir a pesos:')
    resultado = pregunta * conversion
    print (resultado)
    # print (str(conversion) + " " +str(monedas1)) 
    # print (monedas1)
    # print (items)
    # print(lista)
    # source = MXN
    # currencies = USD,AUD,CAD,PLN
    # format = 1
    # print(solicitud)
    # print (monedas)

divisas()    






# // Ivan, click on the URL above to get the most recent exchange
# // rates for USD, AUD, CAD, PLN and MXN