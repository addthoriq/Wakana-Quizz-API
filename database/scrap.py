import requests
from bs4 import BeautifulSoup
import csv
import time
import pprint
import re

url = "https://en.wiktionary.org/wiki/Appendix:1000_Japanese_basic_words"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
# response = requests.get(url, headers=headers)
response = open('/home/thoriq/wiktionary.htm')

# if response.status_code == 200:
soup = BeautifulSoup(response, 'html.parser')
body = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
data = []
for val in body:
    li = val.find_all('li')
    for extr in li:
        try:
            the_text = extr.text
            jpn_txt = the_text.split('–')[0].strip()
            hiragana = jpn_txt.split('、')[0].strip()
            pattern_romaji = r'\(([^()]+)\)$'
            pattern_translate = r'–\s*(.*?)\s*\('
            match_romaji = re.search(pattern_romaji, the_text)
            match_translate = re.search(pattern_translate, the_text)
            # if match:
            #     print(match.group(1))  # Output: dokoro
                    # print(matches)
            data.append(
                {
                    "word": hiragana,
                    "romaji": match_romaji.group(1),
                    "translate": match_translate.group(1)
                }
            )
        except AttributeError:
            continue  # Lewati elemen yang tidak memiliki tag <a>
    # with open('basic_japanese_words.csv', 'w', newline='', encoding='utf-8') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['Kanji/Kana', 'Romaji', 'Meaning'])  # Header kolom
        
    #     # Loop melalui tabel
    #     for table in tables:
    #         rows = table.find_all('tr')  # Ambil semua baris di tabel
            
    #         for row in rows[1:]:  # Lewati header tabel
    #             cells = row.find_all('td')
    #             if len(cells) >= 3:  # Pastikan ada setidaknya 3 kolom
    #                 kanji_kana = cells[0].text.strip()
    #                 romaji = cells[1].text.strip()
    #                 meaning = cells[2].text.strip()
    #                 writer.writerow([kanji_kana, romaji, meaning]) 
import pprint
pprint.pprint(data)