# hkcc-moodle-autoattend
利用 Python 和 Selenium 自動登入 [香港專上學院 Moodle](https://moodle.cpce-polyu.edu.hk/) 並自動出席當天課程，並將訊息透過 webhook 發佈到 Discord 上。

## 例子
<img src="https://i.imgur.com/IfQns5P.png" width="250">

# 開始使用
## 環境需求
- [Python 3.8.0+](https://www.python.org/)
- [Google Chrome](https://www.google.com/chrome/) + [WebDriver](https://chromedriver.storage.googleapis.com/index.html)

## 安裝方式
1. 若要執行 hkcc-moodle-autoattend，需要安裝額外的套件，使用終端機至此專案的資料夾中執行此指令：

```
pip install -r requirements.txt
```
或
```
pip3 install -r requirements.txt
```

2. **請將 Chrome WebDriver 設定至環境變數中**

## 設定
用任意的文字編輯器開啟 `autoattend.py`，在
```py
account = ""
password = ""
discord_webhook_url = ""
```
輸入帳號密碼及 Discord 的 webhook 連結，如下：
```py
account = "XXXXXXXXA"
password = "abc123456"
discord_webhook_url = "https://discord.com/api/webhooks/.../..."
```

## 使用方式
使用終端機至專案資料夾執行此指令：
```
python autoattend.py
```
或
```
python3 autoattend.py
```
