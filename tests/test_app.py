import pytest
import webtest

from myapp import app 
from webtest import TestApp

app = TestApp(app.app)

def test_that_pytest_works():

    assert 1 == 1

@pytest.mark.fodat
def test_hello():
    resp = app.get('/hello')
    resp.status == '200 OK'

@pytest.mark.webdriver
def test_no_hello():
    with pytest.raises(webtest.app.AppError) as err:
        resp = app.get('/no_hello')

    assert '404 Not Found' in err.value.args[0]


def test_follow_yooli():
    resp = app.get('/follow/yooli')
    resp.status == '200 OK'

    assert "Follow yooli" == resp.body.decode()
