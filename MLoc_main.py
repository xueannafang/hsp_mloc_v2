import numpy as np
import matplotlib.pyplot as plt
import MLoc_io

db_name, usr_input_data = 'db.csv', 'input_mloc_data.csv'

db, usr_input = MLoc_io.read_input_csv(db_name, usr_input_data)


