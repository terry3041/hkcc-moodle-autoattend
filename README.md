# hkcc-moodle-autoattend
利用 Python 和 Selenium 自動登入 [香港專上學院 Moodle](https://moodle.cpce-polyu.edu.hk/) 並自動出席當天課程。

## 例子
<img src="https://i.imgur.com/BwnUWcN.png" width="250"><img src="https://i.imgur.com/05RSTb3.png" width="250">

# 開始使用
## 環境需求
- [Java 8+](https://www.java.com/zh-TW/download/)
- [Python 3.8.0+](https://www.python.org/)
- [Selenium 伺服器](https://www.selenium.dev/downloads/)
- [HtmlUnitDriver](https://github.com/SeleniumHQ/htmlunit-driver/releases)

## 安裝方式
1. 若要執行 hkcc-moodle-autoattend，需要安裝額外的套件，使用終端機至此專案的資料夾中執行此指令：

```
pip install -r requirements.txt
```
或
```
pip3 install -r requirements.txt
```

2. 使用終端機執行此指令，以運行 Selenium 伺服器與 HtmlUnitDriver

Windows:
```
java -cp "htmlunit-driver-jar-with-dependencies.jar;selenium-server-standalone.jar" org.openqa.grid.selenium.GridLauncherV3
```

Linux / macOS:
```
java -cp "htmlunit-driver-jar-with-dependencies.jar:selenium-server-standalone.jar" org.openqa.grid.selenium.GridLauncherV3
```

## 設定
用任意的文字編輯器開啟 `autoattend.py`，在
```py
account = ""
password = ""
webdriver_port = "4444"
discord_webhook_url = ""
```
輸入帳號密碼，Selenium 伺服器端口及 Discord 的 webhook 連結，如下：
```py
account = "2020XXXXA"
password = "Abc123456!"
webdriver_port = "4444"
discord_webhook_url = "https://discord.com/api/webhooks/......."
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
