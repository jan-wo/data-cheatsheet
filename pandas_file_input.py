"""
Covered data cources:
--------------------
- CSV
- Excel
- HTML
- SQL
"""

import pandas as pd

# -----------------------------------------------------
# Dummy SQL basis:
from sqlalchemy import create_engine
# create simple sql engine in memory
engine = create_engine('sqlite:///:memory:')




# -----------------------------------------------------
# CSV file
df1 = pd.read_csv(r'data-cheatsheet\data_files\test.csv')
df1.to_csv(r'data-cheatsheet\data_files\csv_out.scv',
           index=False)

# Excel file
df2 = pd.read_excel(r'data-cheatsheet\data_files\test.xlsx',
                    sheetname='Sheet1')
df2.to_excel(r'data-cheatsheet\data_files\xlsx_out.xlsx',
             sheet_name='Sheet1')

# HTML:
# This method is looking for the table markers. Not table 'tables'
# can be problematic. Result is a list. in this case df will be if __name__ == '__main__':
# the df3[0].

df3 = pd.read_html(r'https://www.worldometers.info/gdp/gdp-by-country/')

# SQL (use last df, just put it into the SQL database)
df3[0].to_sql('test_tbl', engine)

df4 = pd.read_sql('test_tbl', con=engine)

print(df4)
