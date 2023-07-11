import os
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import seaborn as sns



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


def save_path(suf):

    log_folder_name = str(suf)
    check_folder = os.path.isdir(log_folder_name)

    if not check_folder:
        os.makedirs(log_folder_name)
        print('Creat folder: ', log_folder_name)
    
    else:
        print(log_folder_name, ' Folder exists.')
    
    return log_folder_name


def save_result_csv(asc_result_df, pref, suf):
    csv_name = pref + '_' + suf + '.csv'
    log_folder = save_path(suf)
    log_path_name = '/'.join([log_folder, csv_name])
    asc_result_df.to_csv(log_path_name)
    crt_cwd = os.getcwd()
    print('csv file saved here:')
    print(crt_cwd)
    print(log_path_name)


def plot_detail(df):
    
    if df['Solvent'] == 'M':
        c_out = 'r'
        m_out = '*'
        s_out = 100
        t_out = 'M'
        l_out_1 = 'Target'
        
    else:
        c_out = 'g'
        m_out = 'o'
        s_out = 20

        idx_round = round(df['idx'])
        t_out = str(idx_round)
        l_out_1 = str(round(df['idx']))
        
    l_out_2 = df['Solvent']
    l_out = l_out_1 + ': ' + l_out_2
    
    return c_out, m_out, l_out, s_out, t_out



def plot_hsp(asc_result_df, pref, suf):

    png_name = pref + '_' + suf + '.png'
    log_folder = save_path(suf)
    log_path_name = '/'.join([log_folder, png_name])
    crt_cwd = os.getcwd()
    print('3d png figure saved here:')
    print(crt_cwd)
    print(log_path_name)

    sns.set_style("whitegrid")

    fig = plt.figure(figsize=(10,6))
    ax = plt.axes(projection = '3d')

    label_delta = 0.1

    for i, row in asc_result_df.iterrows():
        
        c_out, m_out, l_out, s_out, t_out = plot_detail(row)
        
        # print(row['Solvent'])

        x = row['D']
        y = row['P']
        z = row['H']
        
        ax.scatter(x, y, z, s = s_out, marker = m_out, label = l_out)

        # ax.scatter(x, y, z, c = c_out, l = l_out)

        # ax.annotate(row['Solvent'], (x, y))
        ax.text(x + label_delta, y + label_delta, z + label_delta, t_out)
        
    ax.set_xlabel('D')
    ax.set_ylabel('P')
    ax.set_zlabel('H', rotation = 90)
    ax.zaxis.labelpad=-1

    # Shrink current axis by 20%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])

    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1.1, 0.5))

    # ax.legend(loc="right")

    plt.savefig(log_path_name)
    plt.show()



def save_results(asc_result_df, pref, suf):

    save_result_csv(asc_result_df, pref, suf)
    plot_hsp(asc_result_df, pref, suf)

