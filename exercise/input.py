from exercise.common import check_user,check_phone,check_password
def input_username():
    username = input("请输入用户名：")
    if check_user(username):
        print("用户名正确")
        return username
    else:
        print("用户名错误")
        input_username()  #递归调用函数自身，完成循环的功能，达到输错就重新输入的功能
def input_password():
    password = input("请输入密码：")
    if check_password(password):
        print("密码正确")
        return password
    else:
        print("密码错误")
        input_password()
def input_phone():
    phone = input("请输入手机号：")
    if check_phone(phone):
        print("手机号正确")
        return phone
    else:
        print("手机号错误")
        input_phone()

def do_reg():
    username = input_username()
    password = input_password()
    phone = input_phone()

    user_list = []
    end = {"username":username,"password":password,"phone":phone}
    user_list.append(end)
    print(user_list)

if __name__ == '__main__':
    do_reg()

