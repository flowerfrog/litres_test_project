import os

from dotenv import load_dotenv


load_dotenv()

context = os.getenv('context', 'bstack')
username = os.getenv('USER_NAME')
access_key = os.getenv('ACCESS_KEY')
remote_browser_url = os.getenv('REMOTE_BROWSER_URL')
