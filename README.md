# hsp_mloc_v2
 MLoc_2.0

The background of this HSP project can be found [here](https://github.com/xueannafang/HSP_toolkit_docs).


## Key update (2023/07/11)
 
 - Detached from SolvPred.
 - Input database updated.
 - Input spreadsheet updated - no longer require manual check of No_db column.
 - Improved 3D plot.


## Run MLoc(v2)

### Packages

matplotlib.pyplot, pandas, datetime, seaborn, numpy

### Input

User can edit calculation parameters (same as the last version) in the first block of "MLoc_main.py"

```
db_name, usr_input_data = 'db.csv', 'input_mloc_data.csv' # name of database file and input data.
alpha = 0.01 # learning rate
n_max = 10000 # maximum iteration steps
tol = 0.00001 # tolerance of convergence
op_name_prefix = 'test' # prefix of output result file
```

And the input file with experimental solubility data: [input_mloc_data.csv](https://github.com/xueannafang/hsp_mloc_v2/blob/main/input_mloc_data.csv).

The calculation is mainly based on the "CAS" and "Indicator" column.

- Please make sure the CAS No. is correctly filled. 
- The "Indicator" column corresponds to the solubility indicator, which could be spectroscopic absorbance feature. Must be float.
- The "Solvent" column will appear on the output figure and results spreadsheet. 

To run:
 ```
 python MLoc_main.py
 ```

### Output

A csv file and png file will be stored under a new folder named with the test time (a 14-digit folder).

The path will be present in the terminal.

#### Example output

```
Initial guess of D, P, H:
17.624036448962748 12.229303813451438 11.720284952257254
Converge after 241 iteration steps
D, P, H of your material:
17.550229115216222 12.675853058467672 10.519465443674356
Please find the result spreadsheet here:
          CAS                 Solvent  Indicator   idx          D          P          H          T       e_D        e_P        e_H        e_T          R
16        NaN                       M        NaN   NaN  17.550229  12.675853  10.519465  24.069627  0.000000   0.000000   0.000000   0.000000   0.000000
6     68-12-2       Dimethylformamide    3.01000   6.0  17.400000  13.700000  11.300000  24.862421  0.150229  -1.024147  -0.780535  -0.792794   1.322266
11   127-19-5   N,N-Dimethylacetamide    2.45000  11.0  16.800000  11.500000  10.200000  22.771254  0.750229   1.175853   0.319465   1.298373   1.932890
1    872-50-4  1-Methyl-2-pyrrolidone    2.57000   1.0  18.000000  12.300000   7.200000  22.959312 -0.449771   0.375853   3.319465   1.110315   3.459666
5     67-68-5      Dimethyl sulfoxide    0.85000   5.0  18.400000  16.400000  10.200000  26.675082 -0.849771  -3.724147   0.319465  -2.605455   4.106065
2    616-47-7       1-Methylimidazole    3.06000   2.0  19.700000  15.600000  11.200000  27.511634 -2.149771  -2.924147  -0.680535  -3.442007   5.244027
13   109-99-9         Tetrahydrofuran    1.04000  13.0  16.800000   5.700000   8.000000  19.460987  0.750229   6.975853   2.519465   4.608640   7.567140
3     75-05-8            Acetonitrile    0.60000   3.0  15.300000  18.000000   6.100000  24.398770  2.250229  -5.324147   4.419465  -0.329143   8.254232
12   108-32-7     Propylene carbonate    1.55000  12.0  20.000000  18.000000   4.100000  27.217825 -2.449771  -5.324147   6.419465  -3.148198   9.672724
7     64-17-5                 Ethanol    3.21000   7.0  15.800000   8.800000  19.400000  26.522443  1.750229   3.875853  -8.880535  -2.452816  10.302395
0    123-91-1             1,4-Dioxane    0.72000   0.0  19.000000   1.800000   7.400000  20.469489 -1.449771  10.875853   3.119465   3.600138  11.680008
10    67-56-1                Methanol    0.75000  10.0  15.100000  12.300000  22.300000  29.607263  2.450229   0.375853 -11.780535  -5.537636  12.764668
15  1330-20-7                  Xylene    0.51000  15.0  17.600000   1.000000   3.100000  17.898883 -0.049771  11.675853   7.419465   6.170744  13.834158
14   108-88-3                 Toluene    0.77000  14.0  18.000000   1.400000   2.000000  18.164801 -0.449771  11.275853   8.519465   5.904826  14.161050
4    110-82-7             Cyclohexane    0.48000   4.0  16.800000   0.000000   0.200000  16.801190  0.750229  12.675853  10.319465   7.268437  16.414018
8     56-81-5                Glycerol    0.23000   8.0  17.400000  12.100000  29.300000  36.161582  0.150229   0.575853 -18.780535 -12.091955  18.791763
9   7732-18-5                   Water    0.00023   9.0  15.500000  16.000000  42.300000  47.807322  2.050229  -3.324147 -31.780535 -23.737695  32.215929
The best solvent is: Dimethylformamide. CAS: 68-12-2
Creat folder:  20230711132253
csv file saved here:
C:\Users\...\hsp_mloc_v2
20230711132253/test_20230711132253.csv
20230711132253  Folder exists.
3d png figure saved here:
C:\Users\...\hsp_mloc_v2
20230711132253/test_20230711132253.png

```

The data can be copied to a separate plotting software to customise the details.

A scheme of 3D Hansen space with all the tested data will also be saved.

<p>

 <img src=https://github.com/xueannafang/hsp_mloc_v2/blob/main/test_20230708170620.png width=800>

</p>



-------------------------------
This project is licensed under GPL-3.0
