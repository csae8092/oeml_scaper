# oeml_scraper

script to scrape and (typesens) index the [Österreichisches Musiklexikon](https://www.musiklexikon.ac.at)
* `make_url_list.py` creates `urls.txt` which is the starting point for
* `python download_obel.py` scrapes biographies, takes some time

## ToDo
* `./download_data` downloads zipped biographies from gdrive and unzippes them
* `python extract_md_and_typesense_index.py` writes some basic md into `info.csv` and populates typesense index