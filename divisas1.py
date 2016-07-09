import requests
solicitud =requests.get("http://apilayer.net/api/live?access_key=a60971011d8b2e279340c4bea4543539")
lista = requests.get("http://apilayer.net/api/list?access_key=a60971011d8b2e279340c4bea4543539")
lana = solicitud.json()
items = lana['source']
monedas = lista.json()

def divisas():
    pregunta1 = str(input('Que tipo de moneda deseas cambiar EUR, AUD, CAD, MXN: '))
    resultado = 0
    if pregunta1 == 'MXN':
        pregunta = int(input('Cuantos dolares quieres convertir a pesos:'))
        conversion = lana['quotes']['USDMXN']
        resultado = pregunta * conversion
    elif pregunta1 == 'EUR':
        pregunta = int(input('Cuantos dolares quieres convertir a euros:'))
        conversion = lana['quotes']['USDEUR']
        resultado = pregunta * conversion
    elif pregunta1 == 'AUD': 
        pregunta = int(input('Cuantos dolares quieres convertir a dolar australiano:'))
        conversion = lana['quotes']['USDAUD']
        resultado = pregunta * conversion
    elif pregunta1 == 'CAD':
        pregunta = int(input ('Cuantos dolares quieres convertir a dolar canadiense'))
        conversion =lana['quotes']['USDCAD']
        resultado= pregunta * conversion
    print (resultado)   
divisas()  

# print (str(conversion) + " " +str(monedas1)) 
    # print (monedas1)
    # print (items)
    # print(lista)
    # source = MXN
    # currencies = USD,AUD,CAD,PLN
    # format = 1
    # print(solicitud)
    # print (monedas)  

# def trueque ():
#     divisa1 = input('Que tipo de moneda deseas cambiar EUR, AUD, CAD, MXN: ')
#     if divisa1 == EUR:
#         eurotrueque = input ('Cuantos euros tienes')
#         resultadoeuro = eurotrueque * items 
#     print (resultadoeuro)
# trueque()
# // Ivan, click on the URL above to get the most recent exchange
# // rates for USD, AUD, CAD, PLN and MXN