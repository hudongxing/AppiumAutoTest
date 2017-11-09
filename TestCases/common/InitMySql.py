
import pymysql
import pymysql.cursors

def operationMySql(name):

    conn = pymysql.connect(host='192.168.188.1', port=3306, user='root', passwd='cocloud', db='smarthome',
                           charset='utf8')
    cursor = conn.cursor()
    # 创建游标
    sql = "SELECT * FROM cld_folder WHERE folder_name ='%s' " % (name,)
    effect_row = cursor.execute(sql)
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return effect_row

if __name__ == "__main__":

    operationMySql("醉红颜77")

#
#     # 关闭游标
#     cursor.close()
#     # 关闭连接
#     conn.close()