import requests
import argparse
import datetime
import json
import re
import os

print("\033[94m  ____  ____  ____  ____  ____  _  _       ___   __   _  _   \033[0m")
print("\033[94m / ___)(  _ \(  __)(  __)(    \( \/ )___  / __) / _\ / )( \  \033[0m")
print("\033[94m \___ \ ) __/ ) _)  ) _)  ) D ( )  /(___)( (_ \/    \) \/ (  \033[0m")
print("\033[94m (____/(__)  (____)(____)(____/(__/       \___/\_/\_/\____/  \033[0m")
print("")
print("                     \033[91mCreated by: t4ps3c\033[0m")
print("")

parser = argparse.ArgumentParser(description='Help options')
parser.add_argument('-u', '--url', type=str, help='URL to fetch')
parser.add_argument('-o', '--output', type=str, default=f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt", help='output file path')

args = parser.parse_args()
url_without_prefix = args.url.replace('https://', '').replace('*.', '').replace('http://', '')
output_file = url_without_prefix  +"-"+ args.output
url = f"https://web.archive.org/cdx/search/cdx?url={args.url}/*&output=text&fl=original&collapse=urlkey"
response1 = requests.get(url)

with open(output_file, 'w') as f:
    f.write(response1.text)

url2 = f"https://otx.alienvault.com/api/v1/indicators/domain/{args.url}/url_list?limit=500&page=%d"
response2 = requests.get(url2)

url3 = f"https://otx.alienvault.com/api/v1/indicators/hostname/{args.url}/url_list?limit=500&page=%d"
response3 = requests.get(url3)

url4 = f"https://urlscan.io/api/v1/search/?q=domain:{args.url}&size=2000"
response4 = requests.get(url4)

data = {
    'response2': response2.text,
    'response3': response3.text,
    'response4': response4.text,
}

with open('urls.json', 'w') as f:
    json.dump(data, f)

urls = []
with open('urls.json', 'r') as f:
    data = json.load(f)
    for key in data:
        urls.extend(re.findall('"url": "(.*?)"', data[key]))

with open(output_file, 'a') as f:
    f.write('\n'.join(urls))

os.remove('urls.json')

print("All URLs saved to", output_file)
