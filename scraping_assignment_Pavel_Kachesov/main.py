from scraper import csv_format, scraper
import pandas as pd


if __name__ == '__main__':
    alllinks = ["https://www.notino.de/zahnpasten/", "https://www.notino.fr/dentifrices/", "https://www.notino.at/zahnpasten/"]
    done = scraper("https://www.notino.cz/zubni-pasty/")
    for link in alllinks:
        df = scraper(link)
        done = pd.concat([done, df], ignore_index=True)
    print(done)
    csv_format(done)


