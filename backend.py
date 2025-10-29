import requests
from requests.exceptions import ConnectionError
from dotenv import dotenv_values
import logging
import re

config = dotenv_values(r".\.env")

LOG_FILE = "error.log"

logging.basicConfig(
    filename=LOG_FILE,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def login(url_check="http://connectivitycheck.gstatic.com/generate_204"):
    try:
        USERNAME=config["USERNAME"]
        PASSWORD=config["PASSWORD"]
    except KeyError:
        logging.warning("Either no .env file or no USERNAME/PASSWORD field made in .\\.env.")
        return -2
    
    try:
        response = requests.get(url_check, allow_redirects=True)
        if response.status_code == 200:
            match = re.search(r'window\.location\s*=\s*["\']([^"\']+)["\']', response.text)
            if match:
                url = match.group(1)
                magic = url.split('?')[-1]
            else:
                logging.error("Redirect error, URL fetch error or magic value not found.")
                logging.info(f"Response: {response.text}")
                return -3
        else:
            logging.info("Already connected and autheticated to the network.")
            return 0

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": url,
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        logindata = {
            'username' : USERNAME,
            'password' : PASSWORD,
            '4Tredir' : 'http://www.gstatic.com/generate_204',
            'magic' : magic
        }
        
        session = requests.Session()
        response = session.post(url, data=logindata, headers=headers)

        if "keepalive" in response.text:
            logging.info("Connected and authenticated successfully.")
            return 1
        else:
            logging.error("Login failed due to server-side fault. Please check the browser portal for more info.")
            return -4
        
    except ConnectionError:
        logging.error("No wifi/ethernet connection available.")
        return -1
        
if __name__ == "__main__":
    print(login())