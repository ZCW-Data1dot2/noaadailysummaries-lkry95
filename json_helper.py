import pandas as pd
import os
import json

def read_json(file_path):
    path = file_path
    f = open(path, 'r')
    return json.load(f)

def read_all_json_files(JSON_ROOT):
    df_ex = pd.DataFrame()
    path = JSON_ROOT
    files = os.listdir(path)
    for i in files:
        if ".json" in i:
            df = pd.DataFrame(read_json(path + i)['results'])
            df_ex = df_ex.append(df, ignore_index=True)
    return df_ex

