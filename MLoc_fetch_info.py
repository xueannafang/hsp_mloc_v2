def fetch_hsp(db, usr_data):

    usr_data_with_hsp = usr_data

    for i, usr_data_dict in enumerate(usr_data):

        crt_cas = usr_data_dict['CAS']

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
    
    print('Fetching HSP done.')
    print(usr_data_with_hsp)

    return usr_data_with_hsp
        


