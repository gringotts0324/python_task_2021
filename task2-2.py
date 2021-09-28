import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import datetime
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

#ログファイルのパスとファイル名
LOG_FILE_PATH = "./log/log_{datetime}.log" 
EXP_CSV_PATH = "task2_list_{search_keyword}_{datetime}.csv"
logtime = datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")
log_file_path = LOG_FILE_PATH.format(datetime=logtime) #変数LOG_FILE_PATHの{datetime}にlogtimeを代入

# Chromeを起動する関数
def set_driver(driver_path, headless_flg):
    if "chrome" in driver_path:
        options = ChromeOptions()
    else:
      options = Options()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    if "chrome" in driver_path:
        return Chrome(driver_path,options=options)
        #return Chrome(executable_path=os.getcwd() + "/" + driver_path,options=options)
    else:
        return Firefox(executable_path=os.getcwd()  + "/" + driver_path,options=options)

# ログに関する処理
def log(txt):
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    logtxt = f"{now},{txt}"
    with open(log_file_path, "a", encoding = "utf-8_sig") as file:
        file.write(logtxt + "\n")
    print(logtxt)


# main処理
def main():
    log("処理開始")
    search_keyword = "高収入"
    #search_keyword = input("検索キーワードを入力してください")
    log(f"検索ワードは、{search_keyword}です")

    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        path = ChromeDriverManager().install() #追加
        driver = set_driver(path, False) #変更
        #driver = set_driver("chromedriver", False)
    # Webサイトを開く
    driver.get("https://tenshoku.mynavi.jp/")
    time.sleep(5)
    # ポップアップを閉じる
    driver.execute_script('document.querySelector(".karte-close").click()')
    time.sleep(5)
    # ポップアップを閉じる
    driver.execute_script('document.querySelector(".karte-close").click()')

    # 検索窓に入力
    driver.find_element_by_class_name("topSearch__text").send_keys(search_keyword)
    # 検索ボタンクリック
    driver.find_element_by_class_name("topSearch__button").click()
    #driver.implicitly_wait(10)

    #URLを用いる場合
    #driver.get(f"https://tenshoku.mynavi.jp/list/kw{search_keyword}/?jobsearchType=14&searchType=18")

    # ページ終了まで繰り返し取得
    # 検索結果の一番上の会社名を取得
    #name_list = driver.find_elements_by_class_name("cassetteRecruit__name")
        
    # 空のDataFrame作成
    df = pd.DataFrame()

    #ログ用のカウント
    count = 0
    success = 0
    fail = 0

    #print(len(name_list))
    while True:
        elements = driver.find_elements_by_class_name("cassetteRecruit__content")
        for element in elements:
            # DataFrameに対して辞書形式でデータを追加する
            name = element.find_element_by_class_name("cassetteRecruit__name")
            title = element.find_element_by_class_name("cassetteRecruit__copy")
            df = df.append(
                {"会社名": name.text, 
                "求人タイトル": title.text}, 
                ignore_index=True)
            log(f"{count}件目追加成功：{name.text}")
            count+=1
        #次ページ 
        next_page_count = driver.find_elements_by_class_name("iconFont--arrowLeft")
        if len(next_page_count) > 10:
            next_page = driver.find_element_by_class_name("iconFont--arrowLeft")
            next_page_url = next_page.get_attribute("href")
            driver.get(next_page_url)
        else:
            print("最後のページです。終了します")
            break #ループから抜ける

    #csv出力
    print(df)
    df.to_csv("task2_list.csv")
    exp_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    df.to_csv(EXP_CSV_PATH.format(search_keyword=search_keyword, datetime=exp_time), encoding = "utf-8-sig")
    log(f"処理完了")


# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()