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


def list2df(result_list):

    result_df = pd.DataFrame(result_list)
    asc_result = result_df.sort_values(by="R")
    print('Please find the result spreadsheet here:')
    print(asc_result)
    print('The best solvent is: ' + asc_result.iloc[1]["Solvent"] + ". CAS: " + asc_result.iloc[1]["CAS"])

    return asc_result


def save_result_csv(asc_result_df, pref, suf):
    path_name = pref + '_' + suf + '.csv'
    asc_result_df.to_csv(path_name)
    crt_cwd = os.getcwd()
    print('csv file saved here:')

    print(crt_cwd)
    print(path_name)


def plot_hsp(asc_result_df, pref, suf):
    path_name = pref + '_' + suf + '.png'





    crt_cwd = os.getcwd()
    print('png file saved here:')

    print(crt_cwd)
    print(path_name)


