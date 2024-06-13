from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import tldextract
import pycountry
import pandas as pd





def cylus(el, df, name, driver):
    elements = driver.find_elements(By.CLASS_NAME, el)
    texts = [elem.text for elem in elements]
    df[f'{name}'] = texts
    return df

def get_country_from_url(url):
    extracted = tldextract.extract(url)
    suffix = extracted.suffix
    country = pycountry.countries.get(alpha_2=suffix.upper())
    return country.name

def parcer(url, df):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get(url)
        cylus("sc-dmyCSP", df, "Name", driver)
        cylus("sc-guDLey", df, "Brand", driver)
        cylus("sc-hhyKGa.sc-gYrqIg.iwwcvf.dOVzXZ", df, "Price",driver)
        cylus("sc-hhyKGa.sc-cCzLxZ.jOWcPO.ieEJyY", df, "Currency",driver)
        links = driver.find_elements(By.CSS_SELECTOR, "a.sc-jdHILj")
        linksall = []
        for link in links:
            l = link.get_attribute('href')
            linksall.append(l)
        df['Links'] = linksall

        imgs = driver.find_elements(By.CLASS_NAME, 'sc-iKOmoZ')
        imgsall =[]
        for i in imgs:
            img = i.get_attribute('src')
            imgsall.append(img)
        df['IMG'] = imgsall

        df['Country'] = get_country_from_url(url)
        df['Scraped_at '] = datetime.now()
        print(df)
        return df

    finally:
        driver.quit()



def scraper(link):
    df = parcer(f"{link}", pd.DataFrame())
    return df

def csv_format(scraper):
    file = scraper.to_csv('notino_transformed.csv', index=False)
    return file





