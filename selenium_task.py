from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import pandas 

def scraping():
    driver_path = ChromeDriverManager().install()
    options = ChromeOptions()
    #options.add_argument("--headless") #Chromeを起動するときのオプション。例えば、headlessは、表示させない
    #options.add_argument("--user-agent=")
    driver = Chrome(driver_path)
    driver.get("https://gyoumu-kouritsuka-pro.site/")

    df = pandas.DataFrame() #DataFrame型のdfを用意（まだ空）
    while True:
        article_elms = driver.find_elements_by_css_selector(".entry-card-wrap.a-wrap.border-element.cf")
        for article_elm in article_elms:
            # print(article_elm.text)
            title = article_elm.find_element_by_tag_name("h2").text
            post_date = article_elm.find_element_by_class_name("post-date").text
            article_link = article_elm.get_attribute("href") #属性を取得
            print(title, post_date, article_link) #カンマ区切りでprint関数を使うと、スペースがあく

            #dfは、dictionary形式で書く。キーがcolumn名、valueがその下の値
            df = df.append({
                    "タイトル": title,
                    "投稿日": post_date,
                    "リンク": article_link
                }, ignore_index = True)

        try:
            driver.find_element_by_css_selector(".pagination-next-link.key-btn").click()
        except:
            print("最終ページです")
            break #ループから抜ける

    df.to_csv("article.csv", encoding="utf-8-sig")


scraping()