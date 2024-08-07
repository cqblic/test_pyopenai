import os
from azure.identity import ClientSecretCredential
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("AZURE_CLIENT_ID")
client_secret = os.getenv("AZURE_CLIENT_SECRET")
tenant_id = os.getenv("AZURE_TENANT_ID")

print(client_id)

# set up authority 
authority = "https://login.microsoftonline.com"
credential = ClientSecretCredential(
        tenant_id = tenant_id,
        client_id = client_id,
        client_secret = client_secret,
        authority=authority
        )

# get bearer token 
token = credential.get_token("https://cognitiveservices.azure.com/.default")
print(token.token)
