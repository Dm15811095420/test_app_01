import allure


class Test001:
    @allure.step("下单")
    def test_001(self):
        allure.attach("买一个手机","附件")  # 添加步骤描述信息
    @allure.step("登录")
    def test_002(self):
        allure.attach("用户名：popo,密码：123456", "附件")  # 添加步骤描述信息



    @allure.step("支付")
    def test_003(self):
        allure.attach("买一个手机", "附件")  # 添加步骤描述信息


    @allure.step("查询")
    def test_004(self):
        allure.attach("买一个手机", "附件")  # 添加步骤描述信息
        print("hahaa")
