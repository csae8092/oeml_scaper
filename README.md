# oeml_scraper

script to scrape and (typesens) index the [Österreichisches Musiklexikon](https://www.musiklexikon.ac.at)
* `make_url_list.py` creates `urls.txt` which is the starting point for
* `python download_obel.py` scrapes articles, takes some time

## ToDo
* `$ gdown https://drive.google.com/uc?id=1GqA4lKvMT7GpX9MclpyV0IdqZBZAX88w` to download scraped articles saved on gdrive -> wrap into some shellscript
* `python extract_md_and_typesense_index.py` writes some basic md into `info.csv` and populates typesense index
