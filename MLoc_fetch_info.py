def fetch_hsp(db, usr_data):

    usr_data_with_hsp = usr_data

    all_cas_found = 1

    for i, usr_data_dict in enumerate(usr_data):

        crt_cas = usr_data_dict['CAS']
        usr_data_dict['idx'] = i

        cas_found = 0

        for j, solv_db_dict in enumerate(db):

            if solv_db_dict['CAS'] == crt_cas:

                cas_found = 1

                usr_data_with_hsp[i]['D'] = solv_db_dict['D']
                usr_data_with_hsp[i]['P'] = solv_db_dict['P']
                usr_data_with_hsp[i]['H'] = solv_db_dict['H']
            
        if cas_found == 0:

            print('CAS not found. \nError CAS:')
            print(crt_cas)
            all_cas_found = 0
    
    print('Fetching HSP done.')
    print(usr_data_with_hsp)

    if all_cas_found == 0:

        print('Please double check the CAS No. in all your input entries and try again.')
        # exit()
        raise ValueError("CAS No. Not Found.")

    return usr_data_with_hsp
        

def fetch_calc_vec(usr_data_with_hsp):

    all_calc_vec_dict = {
        'all_idxs' : [],
        'all_ds' : [],
        'all_ps' : [],
        'all_hs' : [],
        'all_indicators' : []

    }

    for i, entry in enumerate(usr_data_with_hsp):

        crt_indicator = entry['Indicator']
        crt_d = entry['D']
        crt_p = entry['P']
        crt_h = entry['H']
        crt_idx = entry['idx']

        all_calc_vec_dict['all_ds'].append(crt_d)
        all_calc_vec_dict['all_ps'].append(crt_p)
        all_calc_vec_dict['all_hs'].append(crt_h)
        all_calc_vec_dict['all_indicators'].append(crt_indicator)
        all_calc_vec_dict['all_idxs'].append(crt_idx)
    
    # print(all_calc_vec_dict)

    return all_calc_vec_dict

        
def calc_result_combine(calc_result_dict, usr_input_df):

    result_detail_df = usr_input_df

    for i, idx in enumerate(calc_result_dict['all_idxs']):

        for j, entry in enumerate(usr_input_df):

            if entry['idx'] == idx:
                result_detail_df[j]['T'] = calc_result_dict['all_ts'][idx]
                result_detail_df[j]['e_D'] = calc_result_dict['e_d'][idx]
                result_detail_df[j]['e_P'] = calc_result_dict['e_p'][idx]
                result_detail_df[j]['e_H'] = calc_result_dict['e_h'][idx]
                result_detail_df[j]['e_T'] = calc_result_dict['e_t'][idx]
                result_detail_df[j]['R'] = calc_result_dict['R'][idx]
    
    entry_m = {
        'Solvent' : 'M',
        'D' : calc_result_dict['dm'],
        'P' : calc_result_dict['pm'],
        'H' : calc_result_dict['hm'],
        'T' : calc_result_dict['tm'],
        'e_D' : 0,
        'e_P' : 0,
        'e_H' : 0,
        'e_T' : 0,
        'R' : 0
    }

    result_detail_df.append(entry_m)


    # print(result_detail_df)
    return result_detail_df



