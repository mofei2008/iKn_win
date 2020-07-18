# coding=utf-8
# !usr/bin/python
from ddt import ddt,data,unpack
import unittest
import requests
from public import base
from oper import read_Config
from oper import read_excel
# testcasefile = 'test_data.xlsx'
# product = read_excel.XLDatainfo.get_sheet_data(testcasefile,'product')


def test() :
    # url = 'https://pbsapi.aikenong.com.cn/boss/locations/company/'
    # par = {"username": '13611112222', "password": 'akn2019666'}
    # s = requests.session()
    # resp = s.post('https://pbsapi.aikenong.com.cn/boss/login/',data=par)
    # print(resp)
    # a = resp['data']['token']
    # print(a)
    # print('测试开始！')
    #
    # headers = {"Authorization": a}
    # resp1 = requests.get('https://pbsapi.aikenong.com.cn/boss/locations/company/',headers=headers)

    header = {  # 登录抓包获取的头部
        "User-Agent": "PostmanRuntime/7.26.1",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive"
    }

    body = {"username": '13611112222', "password": 'akn2019666'}  # 这里账号密码就是抓包的数据
    s = requests.session()
    login_url = "https://pbsapi.aikenong.com.cn/boss/login/"  # 自己找带token网址
    login_ret = s.post(login_url, headers=header, data=body)
    # 这里token在返回的json里，可以直接提取
    token = login_ret.json()['data']["token"]
    print(token)
    # 这是登录后发的一个post请求
    post_url = "https://pbsapi.aikenong.com.cn/boss/locations/company/"
    # 添加token到请求头
    header["Authorization"] = token
    print(header)
    # 如果这个post请求的头部其它参数变了，也可以直接更新

    post_ret = requests.get(post_url, headers=header)
    print(post_ret)
if __name__ == "__main__":
    test()

