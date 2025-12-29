import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_1%E2%80%938)#Series_overview"
all_tables = pd.read_html(url, storage_options={
        "User-Agent": "Chrome/120.0.0.0"})

#print(all_tables[1])
df = all_tables[2]
df.to_csv("one_piece_season_1.csv", index=False)
