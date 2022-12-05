import requests

page = 'https://imgs.xkcd.com/comics/python.png'

r = requests.get(page)

with open('comic.png', 'wb') as f:  # write the image on a file (download)
    f.write(r.content)

print(r.status_code)
print(r.ok)
print(r.headers)
print(r.url)
#print(r.content)