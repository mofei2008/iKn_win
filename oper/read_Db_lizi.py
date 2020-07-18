# python + selenium利用records进行数据库操作
#
# yunjians0人评论456人阅读2020 - 04 - 01
# 16: 20:29
import records


class ConnectDb:
    """
    利用records连接数据库
    """

    @staticmethod
    def connect(filepath=None) -> records.Database:
        """
        :param filepath: 配置文件
        :return: <Database open=True> 数据库对象
        """
        if filepath is None:
            file = INIFILEPATH
        else:
            file = filepath
        host = Readini.getvalue("Database", "dbhost", file)
        port = Readini.getvalue("Database", "dbport", file)
        user = Readini.getvalue("Database", "dbusername", file)
        passwd = Readini.getvalue("Database", "dbpasswd", file)
        db = Readini.getvalue("Database", "dbname")
        db_url = 'mysql+pymysql://' + user + ':' + passwd + '@' + str(host) + ':' + str(port) + '/' + db
        # connect = records.Database('mysql+pymysql://用户名:密码@sqlURl:sql端号/库名')
        connect = records.Database(db_url)

        return connect


def insert_run_record(self, project_name, device_sn, device_static, run_value):
    """
    插入数据
    :param project_name: 项目名称，取config文件中的项目名称，字段 PROJECTNAME
    :param device_sn: 设备号
    :param device_static: 设备状态
    :param run_value: 运行内容
    """
    try:
        value = {
            'device_sn': device_sn,
            'device_static': device_static,
            'run_value': run_value,
            'create_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        connect.query(
            "insert into selenium_chanpin_znsd_runvalue(project_id, device_sn,device_static,run_value,create_time) "
            "values(:project_id," +
            "(SELECT project_id FROM selenium_project where project_name = '" + project_name + "')" +
            ",:device_static, :run_value, :create_time)", **value)
    except Exception as e:
        print("sql运行失败" + str(e))


def select_run_value(self, device_sn) -> str:
    """
    通过设备编号查询最新一条运行数据的内容
    :param device_sn: 设备sn
    :return: 运行内容
    """
    try:

        select_value_sql = "SELECT run_value FROM selenium_chanpin_znsd_runvalue where device_sn='" + device_sn + \
                           " 'ORDER BY create_time DESC limit 1"
        rows = connect.query(select_value_sql)
        return rows.first(as_ordereddict=True)["run_value"]
    except Exception as e:
        print("执行sql失败" + str(e))