import requests
import datetime
filename = datetime.datetime.utcnow().isoformat()
url = [
        {
            'page':'https://www.roguefitness.com/stainless-steel-ohio-bar',
            'name':'stainless'
        }
    ]'https://www.roguefitness.com/rogue-ohio-bar-black-oxide']
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
with open(filename, "w") as text_file:
    text_file.write(result.content.decode())
