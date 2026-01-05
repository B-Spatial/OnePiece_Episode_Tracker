import pandas as pd
from episode_scraper import episode_scrape

def main():
   
   url_dict = {"https://en.wikipedia.org/wiki/Lists_of_One_Piece_episodes": slice(0, 1),
               "https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_1%E2%80%938)#Season_1:_East_Blue_(1999%E2%80%932001)": slice(2, 10),
               "https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_9%E2%80%9314)": slice(1, 7),
               "https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_15%E2%80%9319)#Season_18:_Zou_(2016%E2%80%9317)": slice(1, 6),
               "https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_20%E2%80%93present)": slice(1, 3)
               }

   episode_scrape(url_dict)


if __name__ == "__main__":
    main()
