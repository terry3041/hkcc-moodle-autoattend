# hkcc-moodle-autoattend
在 Raspberry Pi 4 上，利用 Python 和 Selenium 自動登入 [香港專上學院 Moodle](https://moodle.cpce-polyu.edu.hk/) 並自動出席當天課程，並將訊息透過 webhook 發佈到 Discord 上。

## 例子
<img src="https://i.imgur.com/IfQns5P.png" width="250">

# 開始使用
## 環境需求
- [Raspberry Pi OS](https://www.raspberrypi.org/software/) / [Ubuntu for ARM](https://ubuntu.com/download/raspberry-pi)

## 安裝方式
1. 若要執行 hkcc-moodle-autoattend，需要安裝額外的套件，使用終端機至此專案的資料夾中執行此指令：

```
sudo apt -y install chromium-chromedriver chromium-browser python3 python3-pip
pip3 install -r requirements.txt
```

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
python3 autoattend.py
```
