import requests

def get_exchange_rates():
    nbp_api_url = 'https://api.nbp.pl/api/exchangerates/tables/a?format=json'
    response = requests.get(nbp_api_url)
    exchange_rates = response.json()
    return {rate["code"]: rate['mid'] for rate in exchange_rates[0]['rates']}

currency_rates = get_exchange_rates()

def get_currency(currency_code):
    return currency_rates.get(currency_code.upper())

def get_amount_and_currency():
    amount = float(input("Ile masz pieniędzy (kwota)? "))
    currency = input("Podaj kod waluty [EUR, USD, CHF itp.] ").upper()
    return amount, currency

def convert_to_foreign_currency(amount, currency):
    rate = get_currency(currency)
    converted = round(amount / rate, 2)
    print(f"Wymienisz na {converted} {currency}")

def convert_to_pln(amount, currency):
    rate = get_currency(currency)
    convert_to_pln = round(amount * rate, 2)
    print(f"Wymienisz na {convert_to_pln} PLN")

def main():
    ask = input("1. Chcę wymienić złotówki na obcą walutę\n2. Chcę wymienić obcą walutę na złotówki\nWybierz: ")

    if ask == "1":
        amount, currency = get_amount_and_currency()
        convert_to_foreign_currency(amount, currency)
    elif ask == "2":
        amount, currency = get_amount_and_currency()
        convert_to_pln(amount, currency)
    else:
        print("Wybierz opcję 1 lub 2.")

if __name__ == "__main__":
    main()
