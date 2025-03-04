import requests

cookies = {
    'CSRF-TOKEN': '440e9a9a8fadcb2c2ca557f52896208b3de495f379c91828a2d75906a8e5a8b1',
    'PHPSESSID': '7ocv987uq8sa1gmfcto3too49v',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://www.google.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    # 'Cookie': 'CSRF-TOKEN=440e9a9a8fadcb2c2ca557f52896208b3de495f379c91828a2d75906a8e5a8b1; PHPSESSID=7ocv987uq8sa1gmfcto3too49v',
}

response = requests.get('http://apfoodvn.com/', cookies=cookies, headers=headers, verify=False)
with open("output.html" , 'w', encoding='utf-8') as file:
    file.write(response.text)

