from py_clob_client.client import ClobClient
import os

host = "https://clob.polymarket.com"
chain_id = 137  # Polygon mainnet
private_key = os.getenv("PRIVATE_KEY")

client = ClobClient(host, key=private_key, chain_id=chain_id)

# Get existing API key, or create one if none exists
user_api_creds = client.create_or_derive_api_creds()

print("API Key:", user_api_creds.api_key)
print("Secret:", user_api_creds.api_secret)
print("Passphrase:", user_api_creds.api_passphrase)
