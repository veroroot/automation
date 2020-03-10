# (pandas, xlrd, sqlalchemy) pip install library_name

import os
import pandas as pd
from sqlalchemy import create_engine

# 1. read excel file

file_path = 'insert file directory and file name' # file directory and file
# ex) 'C:\\ai\\workspace\\directory\\file_name.xlsx'

df_dict = pd.read_excel(file_path, sheet_name=None)
# only 1 sheet in excel file
if len(df_dict) == 1: 
    df = pd.read_excel(file_path)
    print('single db')
    print('='*50)
    print(df.head())
# multi sheets in excel file
else : 
    for k in df_dict.keys() :
        globals()['df{}'.format(k)] = df_dict[k]
        print('multi sheet')
        print('='*50)
        print(globals()['df{}'.format(k)].head())
        print('='*50)
# db = pd.read_csv(file_path) # csv file

# 2. connect to db

# cf) https://docs.sqlalchemy.org/en/13/core/engines.html describe engine

db_kind = 'insert to use db_kind_name'
id_name = 'insert to connect db id'
password = 'insert to connect db password'
host = 'insert to connect db about host name or ip address and port'
db_name = 'insert to connect db_name'

# connect to db
engine = create_engine(f'{db_kind}://{id_name}:{password}@{host}/{db_name}')

# 3. df to db

table_name = 'insert table name' # table name in db
table_name_list = ['insert table name1', 'insert table name2'] # tables name in db

if len(df_dict) == 1: # excel sheet 1
    df.to_sql(table_name, engine, index=False)
else :
    for i in range(len(table_name_list)):
        for k in df_dict.keys() : # multi excel sheets
            globals()['df{}'.format(k)].to_sql(table_name_list[i], engine, index=False)

# if script dodn't work because of connection to db, insert 41 line code before to_sql code(49 line and 53 line)