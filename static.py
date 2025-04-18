# static.py
import requests
from bs4 import BeautifulSoup
import csv
import json

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

results = []

quotes = soup.find_all("div", class_="quote")
for q in quotes:
    text = q.find("span", class_="text").get_text(strip=True)
    author = q.find("small", class_="author").get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in q.find_all("a", class_="tag")]
    
    results.append({
        "quote": text,
        "author": author,
        "tags": tags
    })

# 寫入 JSON 檔案
with open("static.json", "w", encoding="utf-8") as f_json:
    json.dump(results, f_json, ensure_ascii=False, indent=2)

# 寫入 CSV 檔案
with open("static.csv", "w", newline='', encoding="utf-8") as f_csv:
    writer = csv.DictWriter(f_csv, fieldnames=["quote", "author", "tags"])
    writer.writeheader()
    for item in results:
        writer.writerow({
            "quote": item["quote"],
            "author": item["author"],
            "tags": ", ".join(item["tags"])  # 轉成字串
        })

print("已成功輸出 static.json 與 static.csv！")

