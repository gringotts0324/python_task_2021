from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scraping():
    driver_path = ChromeDriverManager().install()
    options = ChromeOptions
    driver = Chrome(driver_path)
    driver.get("https://spl.stanford.edu/projects")

    df = pd.DataFrame()
    ariticle_elm = driver.find_element_by_css_selector(".tex2jax_process")
    titles = ariticle_elm.find_elements_by_tag_name("h2")
    for title in titles:
        print(title.text)

        df = df.append({
            "Project title": title.text,
        }, ignore_index = True)

    df.to_csv("PsychophysiologyLab.csv")
if __name__ == "__main__":
    scraping()


