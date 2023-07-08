import os
import pandas as pd


def rec_dataset(csv_name):

    ds = pd.read_csv(csv_name)
    df = pd.DataFrame(ds)
    df_dict = df.to_dict('records')

    return df_dict

def read_input_csv(db_name = 'db.csv', usr_data_name = 'input_mloc_data.csv'):

    rec_db = rec_dataset(db_name)
    rec_usr_data = rec_dataset(usr_data_name)

    # print(rec_db, rec_usr_data)

    return rec_db, rec_usr_data


