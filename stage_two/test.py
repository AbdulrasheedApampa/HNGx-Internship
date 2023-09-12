import requests

BASE = "https://fantastic-space-palm-tree-554vpr7rwxp2p6p7-5000.app.github.dev/"

response = requests.get(BASE + "helloword")
print(response.json())
