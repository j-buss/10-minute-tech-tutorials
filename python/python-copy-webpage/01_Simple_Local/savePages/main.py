import requests
import datetime
import os

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def saveWebpage(url, filename, timestamp):
    result = requests.get(url, headers=headers)
    folder = "rawData"
    with open(folder + "/" + filename + "_" + timestamp + ".html", "w") as text_file:
        text_file.write(result.content.decode())

if __name__ == "__main__":
    ts = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    sets = [{'url':'https://www.roguefitness.com/stainless-steel-ohio-bar','name':'OhioBarStainless'},\
            {'url':'https://www.roguefitness.com/the-ohio-bar-2-0-e-coat','name':'OhioBarECoat'},\
            {'url':'https://www.roguefitness.com/rogue-ohio-bar-black-oxide','name':'OhioBarBlackOxide'},\
            {'url':'https://www.roguefitness.com/the-ohio-bar-black-zinc','name':'OhioBarBlackZinc'},\
            {'url':'https://www.roguefitness.com/the-ohio-bar-cerakote','name':'OhioBarCerakote'}]
    for set in sets:
        saveWebpage(set['url'],set['name'], ts)
