# Generates an HTML table from a SQL table using pandas 
# 6.26.2018 TimRCM

import os
import pyodbc
import pandas

import config


def connect_windows():
    '''Create a connection to the SQL database using pyodbc & the SQL Server Native Client 11.0 
    driver in Windows 10, then executes the SQL query to establish a Pandas DataFrame'''

    try:
        conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+config.server+';DATABASE='+config.database+';UID='+config.username+';PWD='+config.password)
    except:
        print("Unknown connection error.")
        exit(1)

    export = conn.cursor()
    # Execute the query in config.py 
    export.execute(config.query)
    # Establish a pandas DataFrame using from_records, which accepts 
    # the list of tuples that will be contained in export
    df = pandas.DataFrame.from_records(export)

    return df


def connect_unix():
    df = print("Not yet functional on *nix/MacOS.")
    exit(1)
    return df


def export_html(df):
    df.columns = config.columns
    # Dump the data to an HTML table 
    df.to_html("export.html", border=1, justify='left', index=False)


if __name__ == '__main__':
    if os.name == 'nt':
        df = connect_windows()
        export_html(df)
    else:
        df = connect_unix()
        export_html(df)
