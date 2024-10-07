import re
import pymysql
from pymysql.cursors import DictCursor


#用户名检验
def check_user(username):
    if len(username) < 5 or len(username) > 12:
        return False

    if username[0] >= '0' and username[0] <= '9':
        return False

    for char in username:
        if ord(char) in range(65,91) or ord(char) in range(97,123) or ord(char) in range(48,58):
            return True

    return True

#检查密码
def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    lower = 0
    upper = 0
    digit = 0

    for char in password:
        if char >= 'A' and char <= 'Z':
            upper += 1
        elif char >= 'a' and char <= 'z':
            lower += 1
        elif char >= '0' and char <= '9':
            digit += 1

    if upper < 1 or lower < 1 or digit < 1:
        return False

    return True

#检查手机号码
def check_phone(phone_number):
    pattern = "^1[3-9]\d{9}$"
    if re.match(pattern,phone_number):
        return True
    else:
        return False

# 全自动化单元测试代码
def test_driver(func,expect,*args):
    actual = func(*args)
    if actual == expect:
        print("测试 %s：成功" % func.__name__)
    else:
        print("测试 %s: 失败" % func.__name__)

# 针对数据库连接进行的封装操作(异常处理)
def query_mysql(sql):
    try:
        conn = pymysql.connect(host='localhost',user='admin',password='123456',database='learn',charset='utf-8')
        curser = conn.cursor(DictCursor)
        curser.execute(sql)
        result = curser.fetchall()
        return result
    except:
        raise Exception("数据库连接异常") # 主动抛出异常
    finally:
        conn.close()

def update_mysql(sql):
    conn = pymysql.connect(host='localhost',user='admin',password='123456',database='learn',charset='utf-8',autocommit=True)
    curser = conn.cursor()
    curser.execute(sql)
    conn.close()

if __name__ == '__main__':
    pass
