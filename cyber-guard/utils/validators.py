import re


def validate_username(username):
    # 用户名必须是3-20个字符，包含字母、数字和下划线
    return bool(re.match(r'^[a-zA-Z0-9_]{3,20}$', username))


def validate_email(email):
    # 简单的邮箱格式验证
    return bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email))


def validate_password(password):
    # 密码至少8个字符，包含至少一个字母和一个数字
    if len(password) < 8:
        return False
    if not re.search(r'[A-Za-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True