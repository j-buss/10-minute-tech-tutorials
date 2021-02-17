import requests
import datetime
import os

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def downloadWebpage(url, filename):
    result = requests.get(url, headers=headers)
    with open(filename, "w") as text_file:
        text_file.write(result.content.decode())

if __name__ == "__main__":
    filename = datetime.datetime.utcnow().isoformat()
    url = 'https://www.roguefitness.com/stainless-steel-ohio-bar'
    links = [{'url':'https://www.roguefitness.com/stainless-steel-ohio-bar','name':'Stainless Ohio Bard'},{'url':'https://www.roguefitness.com/the-ohio-bar-cerakote'}]
    #downloadWebpage(url, filename)
