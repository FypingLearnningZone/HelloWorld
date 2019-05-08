import csv
import os

headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
         ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
         ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]
print(os.path.exists('receive_user.csv2'))
with open('a.csv') as f:
    f_csv = csv.reader(f) 
    # headers = next(f_csv)去除表头
    for row in f_csv:
        print(row)

with open('receive_user.csv','a') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)