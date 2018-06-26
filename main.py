# Generates an HTML table from a SQL table
# 6.26.2018 TimRCM

import pyodbc
from flask_table import Table, Col

import config

conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+config.server+';DATABASE='+config.database+';UID='+config.username+';PWD='+config.password)
export = conn.cursor()
export.execute(config.query)

for row in export:
    print(f'{row}')