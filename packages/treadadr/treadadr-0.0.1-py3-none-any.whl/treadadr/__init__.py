#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd

# �� SQLite ���ݿ�
conn = sqlite3.connect('example.db')

# ѡ��Ҫת���ı�
cursor = conn.cursor()
cursor.execute('SELECT * FROM table_name')

# �����ת��Ϊ DataFrame
df = pd.DataFrame(cursor.fetchall())

print(df)

# �ر����ݿ�����
conn.close()
