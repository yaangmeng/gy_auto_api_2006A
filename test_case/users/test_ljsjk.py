import random

from tools.api import request_tool


def test_czmk(pub_data,db):
    res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE `status` =0 AND `account_name`IS NOT NULL;")
    pub_data["accountname"] = random.choice(res)[0]
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''{
  "accountName": "${accountname}",
  "changeMoney": 50000
}
'''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
