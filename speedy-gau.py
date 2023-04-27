from selenium import webdriver
import argparse
import datetime
import re
import json
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
parser.add_argument('-o', '--output', type=str, default=f"urls_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt", help='output file path')


args = parser.parse_args()

url = f"https://web.archive.org/cdx/search/cdx?url={args.url}/*&output=text&fl=original&collapse=urlkey"
url2 = f"https://otx.alienvault.com/api/v1/indicators/domain/{args.url}/url_list?limit=500&page=%d"
url3 = f"https://otx.alienvault.com/api/v1/indicators/hostname/{args.url}/url_list?limit=500&page=%d"
url4 = f"https://urlscan.io/api/v1/search/?q=domain:{args.url}&size=2000"


driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
page_source = driver.page_source

with open('wayback.txt', "w", encoding="utf-8") as file:
    file.write(page_source)

driver.get(url2)
driver.implicitly_wait(10)
page_source2 = driver.page_source

with open(("alien1.json"), "w", encoding="utf-8") as file:
    file.write(page_source2)

driver.get(url3)
driver.implicitly_wait(10)
page_source3 = driver.page_source

with open(("alien2.json"), "w", encoding="utf-8") as file:
    file.write(page_source3)
    
driver.get(url4)
driver.implicitly_wait(10)
page_source4 = driver.page_source

with open(("urlscan.json"), "w", encoding="utf-8") as file:
    file.write(page_source4)

with open('alien1.json', 'r') as f:
    file1_data = f.read()

with open('alien2.json', 'r') as f:
    file2_data = f.read()

with open('urlscan.json', 'r') as f:
    file3_data = f.read()

combined_data = file1_data + file2_data + file3_data

with open('urls.json', 'w') as f:
    f.write(combined_data)

with open('urls.json') as f:
    json_text = f.read()

urls = re.findall(r'"url":\s*"(.*?)"', json_text)

with open('alien+urlscan.txt', 'w') as f:
    for url in urls:
        f.write(url + '\n')

with open('wayback.txt', 'r') as f:
    file4_data = f.read()

with open('alien+urlscan.txt', 'r') as f:
    file5_data = f.read()
    
combined_data2 = file4_data + file5_data

with open(args.output, 'w') as f:
    f.write(combined_data2)
    
driver.quit()

files_to_delete = ['alien1.json', 'alien2.json', 'urlscan.json', 'urls.json', 'wayback.txt' , 'alien+urlscan.txt']

[os.remove(file) for file in files_to_delete]

print("All URLs saved to", args.output)
