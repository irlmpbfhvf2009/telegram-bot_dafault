import sqlite3,json,time
from decimal import Decimal
from common.enum import DBHPEnum

'''
sqlite3數據操作封裝
'''
class DBHP():
    def __init__(self,db_name=None):
        db_name = DBHPEnum.DB_NAME.value
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
    '''
    創建表格
    @:param table_name 表名
    @:param field_list 字段列表,例如：["name","age","gender"]
    @:return 
    '''
    def create_tables(self,table_name:str,field_list:list)->bool:
        try:
            fields=",".join([field+" TEXT" for field in field_list])
            sql = f"CREATE TABLE {table_name} ({fields});"
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception:
            return False
    '''
    插入數據，根據傳入的數據類型進行判斷，自動選擇插入方式
    @:param table_name 表名
    @:param data 要插入的數據
    '''
    def insert_data(self,table_name:str,data)->bool:
        try:
            if isinstance(data,list):
                for item in data:
                    keys = ",".join(list(item.keys()))
                    values = ",".join([f"'{x}'" for x in list(item.values())])
                    sql = f"INSERT INTO {table_name} ({keys}) VALUES ({values});"
                    self.cursor.execute(sql)
            elif isinstance(data,dict):
                keys = ",".join(list(data.keys()))
                values = ",".join([f"'{x}'" for x in list(data.values())])
                sql = f"INSERT INTO {table_name} ({keys}) VALUES ({values});"
                self.cursor.execute(sql)
            return True
        except Exception as ex:
            return False
        finally:
            self.conn.commit()
    # 更新数据
    def update(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()

    # 删除数据
    def delete(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()
        return '退出成功'
    '''
    查詢數據
    @:param 要查詢的sql語句
    '''
    def select_all_tasks(self,sql:str)->list:
        try:
            self.cursor = self.conn.execute(sql)
            results = self.cursor.fetchall()
            return results
        except:
            return []

    '''
    關閉數據庫連接
    '''
    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as ex:
            raise Exception("關閉數據庫連接失敗")
