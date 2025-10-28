import requests
from dotenv import load_dotenv
import re
import os

load_dotenv()

def login(url_check="http://connectivitycheck.gstatic.com/generate_204"):
    url = None
    response = requests.get(url_check, allow_redirects=True)
    if response.status_code == 200:
        match = re.search(r'window.location="(.*?)"', response.text)
        if match:
            url = match.group(1)
            magic_match = re.search(r'fgtauth\?(.*?)$', url)
            if magic_match:
                magic = magic_match.group(1)
        else:
            url = None

    if url is None:
        return 0

    else:
        session = requests.Session()
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": url,
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = session.get(url, headers=header)
        magic_match = re.search(r'name="magic" value="(.*?)"', response.text)
        if magic_match:
            magic = magic_match.group(1)
        else:
            with open("error.log", "w") as f:
                f.write("Magic token not found in response.\n")
            return -1


        logindata = {
            'username' : os.getenv("USERNAME"),
            'password' : os.getenv("PASSWORD"),
            '4Tredir' : 'http://www.gstatic.com/generate_204',
            'magic' : magic
        }

        response = session.post(url, data=logindata, headers=header)

        if "keepalive" in response.text:
            return 1
        else:
            with open("error.log", "w") as f:
                f.write(response.text)
            return -1
        
if __name__ == "__main__":
    print(login())