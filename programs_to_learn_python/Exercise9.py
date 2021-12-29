import requests
import json
import time
def read(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

# read("Mai huun jiyan")
if __name__ == '__main__':
 read("Whats up people...")
 read("Welcome to daily news by karthik shetty...")
 # time.sleep(1)
 read("lets begin..")
 r=requests.get("https://newsapi.org/v2/everything?q=apple&from=2021-09-24&to=2021-09-24&sortBy=popularity&apiKey=714d888d4f4540838e62373ffa9cacd9")
 data=r.text
 js_content=json.loads(data)
 for article in js_content['articles']:
     read(article['title'])     read("Moving on..")
 read("Thats it for the day people..Thank you for listening, hope you enjoyed it....Stay safe, Stay cool, bye bye ")