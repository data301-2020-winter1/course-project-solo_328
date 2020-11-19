import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
          .dropna()
          .reset_index(drop=True)
    )
    df2 = (
        df1.loc[lambda x: ~df1['title'].str.contains('Deleted video')]
        .drop(columns = ["video_id", "description", "ratings_disabled", "tags", "comments_disabled", "thumbnail_link"])
        .assign(Count_Upper = df1['title'].str.count(r"[A-Z]"))
    )
    

    df3 = df2[df2['video_error_or_removed'] == False].drop(columns = ["video_error_or_removed"])
    
    return df3




    