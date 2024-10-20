import time
import requests

# 定义登录信息
login_url = "https://www.paypal.com/pl/welcome/signup/#/login_info_phone"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义用户信息
email = "ttttttt@gmail.com"
phone_numbers = [
    "699512706",  # 第一组电话号码
    "699512706",  # 第二组电话号码
    "345678901",  # 第三组电话号码
    "456789012",  # 第四组电话号码
    "567890123"   # 第五组电话号码
]

# 创建一个session对象
session = requests.Session()
session.headers.update({'User-Agent': user_agent})

# 提交注册请求
for phone_number in phone_numbers:
    signup_data = {
        'email': email,
        'phone': phone_number,
        'country': 'po'  # 选择波兰
    }

    response = session.post(login_url, data=signup_data)

    # 检查响应状态
    if response.status_code == 200:
        print(f"注册成功，电话号码：{phone_number}")
    else:
        print(f"注册失败，状态码：{response.status_code}，电话号码：{phone_number}")

    # 等待5分钟
    time.sleep(30)
