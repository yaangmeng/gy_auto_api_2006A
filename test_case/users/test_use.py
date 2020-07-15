import random

import allure
import requests

from config.conf import API_URL
from tools.api import request_tool


@allure.feature('用户管理')  # 一级分类
@allure.story('充值提现')  # 二级分类
@allure.title("扣款接口-账户余额不足")  # 修改用例标题
def test_czmk(pub_data, db):
    # 执行sql
    with allure.step("第一步,执行sql语句"):
        res = db.select_execute(
            "SELECT account_name FROM `t_cst_account` WHERE `status` =0 AND `account_name`IS NOT NULL;")
    # 从查询结果随机获取一条数据，取第一个
    with allure.step("第二步,查询结果随机取值,取第一个数据"):
        account_name = random.choice(res)[0]
    # 准备请求数据
    with allure.step("第三步,准备数据"):
        data = {
            "accountName": account_name,
            "changeMoney": 50000
        }
    # 使用requests框架发送HTTP请求
    with allure.step("第四步,发送请求"):
        r = requests.post(API_URL + "/acc/charge", json=data)
    with allure.step("第五步,获取请求内容"):
        allure.attach(r.request.method, "请求方法", allure.attachment_type.TEXT)
        allure.attach(r.request.url, "请求url", allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers), "请求头", allure.attachment_type.TEXT)
        allure.attach(r.request.body, "请求内容", allure.attachment_type.TEXT)
    # print(r.request.url)
    with allure.step("第六步,查看响应"):
        allure.attach(str(r.status_code), "响应状态码", allure.attachment_type.TEXT)
        allure.attach(str(r.headers), "响应头", allure.attachment_type.TEXT)
        allure.attach(r.text, "响应正文", allure.attachment_type.TEXT)
        # print(r.text)
    with allure.step("第七步,断言"):
        allure.attach(r.text, "实际结果", allure.attachment_type.TEXT)
        allure.attach("账户余额不足", "预期结果", allure.attachment_type.TEXT)
        assert "账户余额不足" in r.text




    '''
pytest test_case/test_use.py --alluredir=reports/xml
allure generate reports/xml -o reports/html
    '''
    pass
