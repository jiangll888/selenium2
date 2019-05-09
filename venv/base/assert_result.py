from page.register_page import RegisterPage

def assert_result(driver,expect,expect_method):
    expect_method_list = expect_method.split(">")
    c = eval(expect_method_list[0])
    ob = c(driver)
    func = getattr(ob,expect_method_list[1])
    res = func()
    if expect == res:
        return True
    else:
        return False


