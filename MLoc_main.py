import MLoc_io
import MLoc_fetch_info
import MLoc_calc
from datetime import datetime
from datetime import date

#please edit if necessary

# name of database and input data
db_name, usr_input_data = 'db.csv', 'input_mloc_data.csv'

# hyperparameters for gradient descent
alpha = 0.01
n_max = 1000000
tol = 0.005

# prefix of output files
op_name_prefix = 'test'


# Main program below
db, usr_input = MLoc_io.read_input_csv(db_name, usr_input_data)

today = date.today()
now = datetime.now()
crt_time = today.strftime("%Y%m%d") + now.strftime("%H%M%S")

usr_data_with_hsp = MLoc_fetch_info.fetch_hsp(db, usr_input)

all_calc_vec = MLoc_fetch_info.fetch_calc_vec(usr_data_with_hsp)

calc_rslt_dict = MLoc_calc.calc_m(all_calc_vec, alpha, n_max, tol)

result_list = MLoc_fetch_info.calc_result_combine(calc_rslt_dict, usr_data_with_hsp)

asc_result_df = MLoc_io.list2df(result_list)

# MLoc_io.save_result_csv(asc_result_df, op_name_prefix, crt_time)
MLoc_io.save_results(asc_result_df, op_name_prefix, crt_time)