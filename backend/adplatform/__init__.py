import pymysql

# 让 Django 的 MySQL 后端使用 PyMySQL 驱动
pymysql.install_as_MySQLdb()
