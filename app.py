from lxml import html,etree
import requests
from fake_useragent import UserAgent

ua = UserAgent()

headers = {
    'User-Agent': ua.random
}
i = 2200
all_img_url = []
counter_404 = 0
while(True):
    resp = requests.get(f"https://xkcd.com/{i}/",headers=headers)
    tree = html.fromstring(html=resp.content)
    img_url = tree.xpath("//div[@id='comic']/img/@src")
    try:
       if tree.xpath("//body/center[1]/h1/text()")[0] =="404 Not Found":
            counter_404 = counter_404 + 1
            if counter_404 <= 200:
                print(f"I am in page {i}")
                i = i + 1
                continue
            else:
                break
    except IndexError:
        try:
            if len(img_url) != 0:
                try: 
                    if img_url[0] != '':
                        print(f"I am in page {i}")
                        all_img_url.append(img_url[0])
                except IndexError:
                    if tree.xpath("//div[@id='comic']/a/img/@src")[0] != '':
                        print(f"I am in page {i}")
                        all_img_url.append(tree.xpath("//div[@id='comic']/a/img/@src")[0])
                    else:
                        break
        except IndexError:
            print(f"I am in page {i}{i}")
            continue
    i = i + 1

print("The Total Number of Image Source present in list : ",len(all_img_url))
out = input("Want to see all image source url : (Y/N) ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
if out.lower() == "y":
    for result in all_img_url:
        print(result)
else:
    print("Thank you for using xkcd image scraping utility !!!")       