#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd

# 打开 SQLite 数据库
conn = sqlite3.connect('example.db')

# 选择要转换的表
cursor = conn.cursor()
cursor.execute('SELECT * FROM table_name')

# 将结果转换为 DataFrame
df = pd.DataFrame(cursor.fetchall())

print(df)

# 关闭数据库连接
conn.close()
