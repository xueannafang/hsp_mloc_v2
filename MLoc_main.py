import numpy as np
import matplotlib.pyplot as plt
import MLoc_io
import MLoc_fetch_info

db_name, usr_input_data = 'db.csv', 'input_mloc_data.csv'

db, usr_input = MLoc_io.read_input_csv(db_name, usr_input_data)

MLoc_fetch_info.fetch_hsp(db, usr_input)
