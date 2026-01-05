import pandas as pd


def episode_scrape(url_dict):
    for url, table_slice in url_dict.items():
        tables = pd.read_html(
            url,
            flavor="lxml",
            storage_options={"User-Agent": "Chrome/120.0.0.0"}
        )

        # Apply the slice for this URL
        tables = tables[table_slice]

        name = url.split("/")[-1]

        for i, df in enumerate(tables, start=1):
            filename = f"{name}_table_{i}.csv"
            df.to_csv(filename, index=False, encoding="utf-8-sig")
            print(f"Saved {filename}")

    