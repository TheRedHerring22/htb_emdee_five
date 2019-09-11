import hashlib
import requests

url = "http://docker.hackthebox.eu:12345/"
r = requests.session()

html = r.get(url).text
initial_string = html[167:187] #instead of searching with regex, just use the exact position of the string in the html
encrypted_string = hashlib.md5(initial_string.encode('utf-8')).hexdigest()

data = {"hash":encrypted_string}
print (r.post(url = url, data = data).text)