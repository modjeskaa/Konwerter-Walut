import requests

nbp_api_url = 'https://api.nbp.pl/api/exchangerates/tables/a?format=json'
kursy_z_api = requests.get(nbp_api_url)
kursy_walut = kursy_z_api.json()
kursy_walut = kursy_walut[0]['rates']

for waluta in kursy_walut:
    if waluta["code"] == 'USD':
        kursUSD = waluta['mid']

    elif waluta["code"] == 'EUR':
        kursEUR = waluta['mid']

ile = int(input("Ile masz złotówek? "))
waluta = input("Chcesz wymienić na EUR czy USD? ")

if waluta.upper() == "USD":
    converted = round(ile / kursUSD, 2)
    print(f'Wymienisz na {converted} USD')

elif waluta.upper() == "EUR":
    converted = round(ile / kursEUR, 2)
    print(f'Wymienisz na {converted} EUR')



