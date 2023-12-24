from time import sleep
 
def test_lambdatest_todo_app(page):
    assert page.get_hello() == "Hello world"
    sleep(5)
