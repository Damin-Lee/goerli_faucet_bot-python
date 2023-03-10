from twocaptcha import TwoCaptcha
from dotenv import load_dotenv
import requests
import schedule
import time
import os

load_dotenv()

ADDRESS = os.environ.get('ADDRESS')
API_KEY = os.environ.get('2CAPTCHA_API_KEY')
SITE_KEY = os.environ.get('SITE_KEY')

BASE_URL = 'https://goerlifaucet.org/'

def get_captcha():
  solver = TwoCaptcha(API_KEY)
  result = solver.recaptcha(sitekey=SITE_KEY, url=BASE_URL)
  code = result['code']

  return code

def claim():
  captcha = get_captcha()

  url = BASE_URL + "claim.php"
  payload='address=' + ADDRESS+  '&captcha=' + captcha
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }

  try:
    requests.request("POST", url, headers=headers, data=payload)
  except Exception as e:
    print('error: ' + e)

def main():
  ## claim every 24 hours (1440 minutes) + 5 minutes
  schedule.every(1445).minutes.do(claim)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
  main()