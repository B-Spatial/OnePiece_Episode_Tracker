import pandas as pd
from episode_scraper import episode_scrape

def main():
   url_list = ["https://en.wikipedia.org/wiki/Lists_of_One_Piece_episodes",
               "https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_1%E2%80%938)#Series_overview", 
               "https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_9%E2%80%9314)",
               "https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_15%E2%80%9319)#Season_18:_Zou_(2016%E2%80%9317)",
               "https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_20%E2%80%93present)"
               ]
   episode_scrape(url_list)


if __name__ == "__main__":
    main()
