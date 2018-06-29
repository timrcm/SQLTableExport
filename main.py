# Generates an HTML table from a SQL table using pandas 
# 6.26.2018 TimRCM

import pyodbc
import pandas

import config

# Create a connection to the SQL database using pyodbc
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+config.server+';DATABASE='+config.database+';UID='+config.username+';PWD='+config.password)
export = conn.cursor()
# Execute the query in config.py 
export.execute(config.query)

# Establish a pandas DataFrame using from_records, which accepts 
# the list of tuples that will be contained in export
df = pandas.DataFrame.from_records(export)
df.columns = config.columns


# Dump the data to an HTML table 
html = df.to_html("export.html", border=1, justify='left', index=False)
