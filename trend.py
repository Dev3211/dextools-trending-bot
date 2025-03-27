import requests

def check_dextools_trending(token_address):
    url = f"https://api.dextools.io/v1/token/{token_address}/trending"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data["trending"]:
            print(f"🔥 Token {token_address} is trending on DEXTools!")
        else:
            print(f"📉 Token {token_address} is not trending yet.")
    else:
        print("❌ Error fetching data from DEXTools API.")

# Example usage
check_dextools_trending("0xYourTokenAddressHere")
