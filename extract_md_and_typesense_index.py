import pandas as pd
import glob
import os
from acdh_cfts_pyutils import CFTS_COLLECTION
from bs4 import BeautifulSoup
from tqdm import tqdm


def get_fulltext(soup):
    main_div = soup.find("div", {"id": "Langtext"})
    for div in main_div.find_all("div"):
        div.decompose()
    text = main_div.get_text("\n").replace('\xa0', '\n')
    return " ".join(text.split())


files = sorted(glob.glob("./data/**/*.html"))
data = []
cfts_records = []

for x in tqdm(files, total=len(files)):
    _, tail = os.path.split(x)
    if "Verweis" in tail:
        continue
    item = {}
    item["f_name"] = tail
    item["gnd"] = None
    item["doi"] = None
    item["name"] = None
    item["fulltext"] = None
    try:
        with open(x, "r") as f:
            soup = BeautifulSoup(f, "html.parser")
            item["name"] = soup.find("meta", {"name": "DC.Title"}).get("content")
            full_text = get_fulltext(soup)
            for x in soup.find("div", {"id": "docNavi2"}).findChildren("a"):
                href = x.get("href")
                if "d-nb.info" in href:
                    if not 'Familie' in tail:
                        item["gnd"] = href
                if "//dx.doi.org/" in href:
                    item["doi"] = href
                    cfts_record = {
                        'project': 'oeml',
                    }
                    cfts_record['id'] = tail
                    cfts_record['resolver'] = href
                    cfts_record['rec_id'] = tail
                    cfts_record['title'] = item["name"]
                    cfts_record['full_text'] = full_text
                    cfts_records.append(cfts_record)
    except Exception as e:
        print(x, e)
        continue

    data.append(item)
make_index = CFTS_COLLECTION.documents.import_(cfts_records, {'action': 'upsert'})
print(make_index)

df = pd.DataFrame(data)
df.to_csv("info.csv", index=False)
