import calculator

def test_add():
    assert calculator.add(0,0) == 0
    
     
def test_add_2():
    assert calculator.add(-1,-1) == -2

def test_add_3():
    assert calculator.add(4,5) == 9

def test_add_4():
    assert calculator.add(1,2,3,4) == 10

def test_multiply():
    assert calculator.multiply(1,2) == 2

def test_multiply_1():
    assert calculator.multiply(1,2,3,4) == 24 
  