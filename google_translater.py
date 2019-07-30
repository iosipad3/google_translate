from requests_html import HTMLSession
from googletrans import Translator

import re

text = "Хакеры против хакеров. Группировка Intrusion Truth деанонимизировала участников китайской APT17"
session = HTMLSession()
translator = Translator()

resp = session.get('https://xakep.ru/2019/07/25/apt17-deanon/')


# for i in range(10):
# 	title = resp.html.xpath(f'//*[@id="post-2421"]/div')
# 	print(title)

try:
	about = resp.html.find(f'div.bdaia-post-content:nth-child(1)', first=True)
	result = about.text
	russian = translator.translate(text, dest='en')
	spain = translator.translate(russian.text, dest='es')
	russian2 = translator.translate(russian.text, dest='en')
	russian5 = translator.translate(result, dest='en')
	print(russian.text)
except:
	pass


#about2 = resp.html.xpath('span[contains()]/following::*text()')
######
#res = about.html
#post = re.findall(r'\bpost-\w+', res)
#ДОДЕЛАТЬ ПОИСК ЭЛЕМЕНТА!!! - http://qaru.site/questions/2026048/how-to-find-a-word-that-starts-with-a-specific-character
#print(post)
####



