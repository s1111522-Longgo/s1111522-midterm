# api.py
import requests
import csv

# 向 API 發送請求
url = "https://randomuser.me/api/?results=10"
response = requests.get(url)
data = response.json()

# 提取使用者資料
users = data["results"]

# 準備 CSV 檔案
with open("api.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "性別", "Email", "國籍"])

    for user in users:
        full_name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
        gender = user["gender"]
        email = user["email"]
        country = user["location"]["country"]

        writer.writerow([full_name, gender, email, country])

print("已成功輸出 api.csv！")

