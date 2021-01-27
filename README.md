# hkcc-moodle-autoattend


## 例子
<img src="" width="250">

# 開始使用
## 環境需求
- [Python 3.8.0+](https://www.python.org/)
- [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) / [Google Chrome WebDriver](https://chromedriver.storage.googleapis.com/index.html)

## 安裝方式
若要執行 hkcc-moodle--autoattend，需要安裝額外的套件，使用終端機至此專案的資料夾中下此指令：

```
pip install -r requirements.txt
```
或
```
pip3 install -r requirements.txt
```

## 設定
用任意的文字編輯器開啟 "autoattend.py"，在
```py
account = ""
password = ""
```
插入帳號密碼，如下：
```py
account = "2020XXXXA"
password = "Abc123456!"
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
