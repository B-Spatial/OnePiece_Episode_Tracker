import pandas as pd
'''
url = "https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_1%E2%80%938)#Series_overview"
all_tables = pd.read_html(url, storage_options={
        "User-Agent": "Chrome/120.0.0.0"})

#print(all_tables[1])
df = all_tables[7]
df.to_csv("one_piece_season_6.csv", index=False)
'''

def episode_scrape(url_links):
    for url in url_links:
        table = pd.read_html(url, flavor="lxml", storage_options={"User-Agent": "Chrome/120.0.0.0"})

        df = pd.concat(table, ignore_index=True)

        name = url.split("/")[-1]
        df.to_csv(f"{name}.csv", index=False, encoding="utf-8-sig")

        print(f"Saved {name}.csv")
    