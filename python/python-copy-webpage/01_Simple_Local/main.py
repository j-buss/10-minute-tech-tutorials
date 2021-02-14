import requests
res = requests.get('https://www.roguefitness.com/stainless-steel-ohio-bar')
res.status_code()
playFile = open('stainlessOhio.txt','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
