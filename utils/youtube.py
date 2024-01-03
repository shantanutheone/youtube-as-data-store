import requests
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials


YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
CLIENT_SECRET_FILE = 'data/database/secrets/client_secret_1028750880943-e2mtu969qf6rpa35pqvhb32b2imgtmbf.apps.googleusercontent.com.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
TOKEN_LOCATION = "data/database/secrets/token.json"

def get_token():
    # Check if token.json exists
    if os.path.exists(TOKEN_LOCATION):
        credentials = Credentials.from_authorized_user_file(TOKEN_LOCATION)
    else:
        # Create or load credentials
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        credentials = flow.run_local_server(port=8080, open_browser=True)

        # Save the credentials for future use
        with open(TOKEN_LOCATION, 'w') as token:
            token.write(credentials.to_json())

    # Check if the access token is expired
    if credentials.expired:
        # Refresh the access token using the refresh token
        credentials.refresh(requests.Request())
        # Save the updated credentials
        with open(TOKEN_LOCATION, 'w') as token:
            token.write(credentials.to_json())

    return credentials