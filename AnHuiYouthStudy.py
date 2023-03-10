# coding:utf-8
import json
from urllib import response

import requests
import re
import pathlib
import os
import datetime
os.chdir(os.path.dirname(__file__))
# 读取配置文件,要是Linux定时运行请设置绝对路径
date_path = "./AnHuiUserDate.json"

# 图片下载路径
save_img_path = "./img/任务完成.jpg"

# 获取accesToKen
# appid,callback,sign可以自己抓包过去,然后就可以不去改变 (你若是安徽青年大学习可以不用修改)
def get_access_token(openid):
    get_token_url = "http://dxx.ahyouth.org.cn/api/userInfo"
    get_token_params = {
        'callback': 'test',
        'appid': 'test',
        'openid': "", # 用户的openid 必要
        'sign': 'test',
    }
    get_token_params["openid"] = openid
    resource = requests.get(get_token_url, params=get_token_params)
    access_token = re.findall(
        "\('accessToken', '(.*?)'\)", response.text, re.S)[0]
    return access_token


# 获取最新课程
def get_course(access_token):
    course_url = "test.com"+access_token
