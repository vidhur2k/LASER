import requests
import numpy as np
url = "http://128.61.32.139:80/vectorize"
params = {"q": "Hey, how are you?\nI'm OK and you?", "lang": "en"}
resp = requests.get(url=url, params=params).json()
print(resp["embedding"])