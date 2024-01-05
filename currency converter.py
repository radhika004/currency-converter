import requests

def get_exchange_rate(base_currency, target_currency):
    api_key = 'YOUR_API_KEY'  
    url = f'https://open.er-api.com/v6/latest/{base_currency}?apikey={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][target_currency]
        return rate
    except (requests.ConnectionError, requests.Timeout, requests.RequestException) as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def convert_currency():
    print("Welcome to the Currency Converter!")
    
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
    
    base_currency = input("Enter the source currency code (e.g., USD): ").upper()
    target_currency = input("Enter the target currency code (e.g., EUR): ").upper()

    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        print(f"\n{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
        print(f"Exchange rate: 1 {base_currency} = {exchange_rate} {target_currency}")
    else:
        print("Unable to perform the currency conversion. Please try again.")

if __name__ == "__main__":
    convert_currency()
