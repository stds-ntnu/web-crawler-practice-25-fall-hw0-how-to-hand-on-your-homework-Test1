import pytest
from st import add

def test_add():
    assert add(1, 2) == 3, "應該返回兩個數字的和"
    assert add(-1, 1) == 0, "正負數相加應該為0"
    assert add(-1, -1) == -2, "兩個負數相加的結果檢查"