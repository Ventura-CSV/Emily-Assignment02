import pytest
import main
import io
import sys
import re


@pytest.mark.basic
def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '40 \n 40 \n 20'
    # sys.stdin = io.StringIO(datastr)

    ret1, ret2 = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search(r'[\w,\W]*[h,H]ello[\w,\W]*[w,W]orld', ret1)
    print(res.group())
    assert res is not None, 'Expect Hello World!'


@pytest.mark.edge
def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '40 \n 40 \n 20'
    # sys.stdin = io.StringIO(datastr)

    ret1, ret2 = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search(r'[\w,\W]*CS[\w,\W]*V11', ret2)
    print(res.group())
    assert res is not None, 'Expect Hello World!'

@pytest.mark.bonus
def test_main_3():
    assert True, 'This is a bonus test that always passes. You can add more complex logic here if needed.'
