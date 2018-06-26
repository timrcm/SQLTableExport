# Generates an HTML table from a SQL table
# 6.26.2018 TimRCM

import pyodbc
from flask_table import Table, Col

import config


class ItemTable(Table):
    Col0 = Col(config.columns[0])
    Col1 = Col(config.columns[1])
    Col2 = Col(config.columns[2])
    Col3 = Col(config.columns[3])
    Col4 = Col(config.columns[4])
    Col5 = Col(config.columns[5])
    Col6 = Col(config.columns[6])

class Item(object):
    def __init__(self, Col0, Col1, Col2, Col3, Col4, Col5, Col6):
        self.Col0 = Col0
        self.Col1 = Col1
        self.Col2 = Col2
        self.Col3 = Col3
        self.Col4 = Col4
        self.Col5 = Col5
        self.Col6 = Col6


conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+config.server+';DATABASE='+config.database+';UID='+config.username+';PWD='+config.password)
export = conn.cursor()
export.execute(config.query)

# items = [Item(export[0], export[1], export[2], export[3], export[4], export[5], export[6])]
items = [Item('item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7')]

table = ItemTable(items)
print(table.__html__())
