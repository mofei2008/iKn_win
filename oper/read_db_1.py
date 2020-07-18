#!/usr/bin/python
# -*- coding: UTF-8 -*-
import records
from oper import read_Config
config = read_Config.ReadConfig()

# encoding=utf-8
def db_read():
    host = config.get_config_str('DATABASE', 'host')
    # port = config.get_config_int('DATABASE', 'port')
    port = config.get_config_str('DATABASE', 'port')#这里端口号因为是跟其他参数一个整体，都是str型
    user = config.get_config_str('DATABASE', 'user')
    password = config.get_config_str('DATABASE', 'password')
    dbname = config.get_config_str('DATABASE', 'dbname')
    charset = config.get_config_str('DATABASE', 'charset')
    table = config.get_config_str('DATABASE', 'table')

    # # 获取数据库
    # db = records.Database('mysql+pymysql://root:@localhost:3306/dev01_git')
    # db_url = 'mysql+pymysql://' + user + ':' + passwd + '@' + str(host) + ':' + str(port) + '/' + db
    db_url = 'mysql+pymysql://' + user + ':' + password + '@' + host + ':' + port + '/' + dbname + '?' + 'charset' + '=' + charset
    print(db_url)
    # connect = records.Database('mysql+pymysql://用户名:密码@sqlURl:sql端号/库名')
    # db = records.Database(db_url,connect_args={'charset' : 'utf8'})
    db = records.Database(db_url)
    # 查询
    # rows = db.query('select * from test_data where name = "李德涛";')
    sql1 = 'select * from '+ table + ';'
    # sql = 'select * from '+ table + ' where name = "李德涛";'
    print(sql1)
    rows = db.query(sql1)
    prin
    # print(rows.all().encode('utf-8').decode('unicode_escape'))
    # print(rows.all())
    # #导出为excel
    # xlsx_rows = rows.export('xlsx')
    # # xlsx = xlsx_rows.encode()
    # with open('test.xlsx','wb') as f:
    #     f.write(xlsx_rows)
    # print(rows.first())
    # print(rows.all(as_dict=True))
    #导出为json
    # json_rows = rows.export('yaml')
    # json = json_rows.encode()
    # with open('aaa.yaml','wb') as f:
    #     f.write(json)
    # print(json)
    #导出为json
    # json_rows = rows.export('json')
    # # json = json_rows.encode()
    # with open('aaa.json','w') as f:
    #     f.write(json_rows)
    # print(json_rows)
def db_insert():
    host = config.get_config_str('DATABASE', 'host')
    # port = config.get_config_int('DATABASE', 'port')
    port = config.get_config_str('DATABASE', 'port')#这里端口号因为是跟其他参数一个整体，都是str型
    user = config.get_config_str('DATABASE', 'user')
    password = config.get_config_str('DATABASE', 'password')
    dbname = config.get_config_str('DATABASE', 'dbname')
    charset = config.get_config_str('DATABASE', 'charset')
    table = config.get_config_str('DATABASE', 'table')

    # # 获取数据库
    # db = records.Database('mysql+pymysql://root:@localhost:3306/dev01_git')
    # db_url = 'mysql+pymysql://' + user + ':' + passwd + '@' + str(host) + ':' + str(port) + '/' + db
    db_url = 'mysql+pymysql://' + user + ':' + password + '@' + host + ':' + port + '/' + dbname + '?' + 'charset' + '=' + charset
    print(db_url)
    # connect = records.Database('mysql+pymysql://用户名:密码@sqlURl:sql端号/库名')
    # db = records.Database(db_url,connect_args={'charset' : 'utf8'})
    db = records.Database(db_url)
    # 查询
    data = {
        'name': '李德涛',
        'income': 6000
    }
    # rows = db.query('select * from test_data where name = "李德涛";')
    # sql = 'select * from '+ table + ' where name =: name and incom =: income',**data
    # print(sql)
    rows = db.query('select * from '+ table + ' where name =: name and incom =: income',**data)

    # print(rows.all().encode('utf-8').decode('unicode_escape'))
    print(rows.all())
    #导出为excel
    xlsx_rows = rows.export('xlsx')
    # xlsx = xlsx_rows.encode()
    with open('test.xlsx','wb') as f:
        f.write(xlsx_rows)
def db_xlsx():
    rows = [
        {"x": 1, "y": 2},
        {"x": 2, "y": 3},
        {"x": 3, "y": 4},
        {"x": 4, "y": 5}
    ]
    results = records.RecordCollection(iter(rows))
    with open('demo.xlsx', 'wb') as f:
        f.write(results.export('xlsx'))




if __name__ == "__main__":
    db_read()
