# hkcc-moodle-autoattend
利用 Python 和 Selenium 自動登入 [香港專上學院 Moodle](https://moodle.cpce-polyu.edu.hk/) 並自動出席當天課程。

## 例子
<img src="https://i.imgur.com/BwnUWcN.png" width="250"><img src="https://i.imgur.com/05RSTb3.png" width="250">

# 開始使用
## 環境需求
- [Python 3.8.0+](https://www.python.org/)
- [Microsoft Edge](https://www.microsoft.com/zh-tw/edge) / [Google Chrome](https://www.google.com/chrome/)
- 與瀏覽器版本吻合的 [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) / [Google Chrome WebDriver](https://chromedriver.storage.googleapis.com/index.html)

## 安裝方式
1. 若要執行 hkcc-moodle-autoattend，需要安裝額外的套件，使用終端機至此專案的資料夾中下此指令：

```
pip install -r requirements.txt
```
或
```
pip3 install -r requirements.txt
```

2. 將下載的 `chromedriver.exe` 或 `msedgedriver.exe` 放至與腳本同一目錄

## 設定
用任意的文字編輯器開啟 "autoattend.py"，在
```py
account = ""
password = ""
browser = "chrome" # edge or chrome
```
輸入帳號密碼及所喜好的瀏覽器（目前僅支援 Chrome / Edge），如下：
```py
account = "2020XXXXA"
password = "Abc123456!"
browser = "edge" # edge or chrome
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
