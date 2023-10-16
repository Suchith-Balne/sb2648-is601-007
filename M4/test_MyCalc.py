import pytest
from MyCalc import MyCalc

'''
UCID: sb2648
Defined a function called calc_instance which helps us to create instance of the MyCalc class.
In order to use this instance for other testcases, a decorator @pytest.fixture is added for the function calc_instance().
This function returns the instance of the class as output.
'''
@pytest.fixture
def calc_instance():
    return  MyCalc()

'''
UCID: sb2648
Date: 10/16/23
Here, we are providing the calc_instance as an input for the test_number_add_number method where calc() function can be accessed.
Added few assertions to test the working of addition operation for given inputs. 
In assertions, we are testing the addition operation on different values to check actual and expected values.
In this function we are adding two number.
'''
def test_number_add_number(calc_instance):
    assert calc_instance.add(2, 2) == 4
    assert calc_instance.add(2, -2) == 0
    assert calc_instance.add(-2, 2) == 0
    assert calc_instance.add(-2, -2) == -4
    
'''
UCID: sb2648
Date: 10/16/23
Here, we are providing the calc_instance as an input for the below method test_ans_add_number where calc() function can be accessed.
Added few assertions to test the working of addition operation for given inputs.
In assertions, we are testing the addition operation on different values to check actual and expected values.
In this function we are adding the ans variable with a number.
'''
def test_ans_add_number(calc_instance):
    assert calc_instance.add(2, 2) == 4
    assert calc_instance.add(calc_instance.ans, -2) == 2
    assert calc_instance.add(calc_instance.ans, +2) == 4
'''
UCID: sb2648
Date: 10/16/23
Here, we are providing the calc_instance as an input for the test_number_sub_number method where calc() function can be accessed.
Added few assertions to test the working of subtraction operation for given inputs. 
In assertions, we are testing the subtraction operation on different values to check actual and expected values.
In this function we are adding two number.
'''
def test_number_sub_number(calc_instance):
    assert calc_instance.sub(10, 5) == 5
    assert calc_instance.sub(12, -2) == 14
    assert calc_instance.sub(-14, 2) == -16
    assert calc_instance.sub(-14, -2) == -12
    
'''
UCID: sb2648
Date: 10/16/23
Here, we are providing the calc_instance as an input for the below method test_ans_sub_number where calc() function can be accessed.
Added few assertions to test the working of subtraction method for given inputs and operand.
In assertions, we are testing the subtraction operation on different values to check actual and expected values.
In this function, we are subracting a number from ans variable.
'''
def test_ans_sub_number(calc_instance):
    assert calc_instance.sub(10, 5) == 5
    assert calc_instance.sub(calc_instance.ans, -2) == 7
    assert calc_instance.sub(calc_instance.ans, 2) == 5
    
'''
UCID: sb2648
Date: 10/16/23
Here, we are providing the calc_instance as an input for the test_number_mul_number method where calc() function can be accessed.
Added few assertions to test the working of multiplication operation for given inputs. 
In assertions, we are testing the subtraction operation on different values to check actual and expected values.
In this function we are multiplying two number.
'''
def test_number_mul_number(calc_instance):
    assert calc_instance.mult(10, 5) == 50
    assert calc_instance.mult(12, -2) == -24
    assert calc_instance.mult(-14, 2) == -28
    assert calc_instance.mult(-14, -2) == 28
    
'''
UCID: sb2648
Date: 10/16/23
Here, we are providing the calc_instance as an input for the below function test_ans_mul_number where calc() function can be accessed.
Added few assertions to test the working of multiplication operation for given inputs and operand.
In assertions, we are testing the multiplication operation on different values to check actual and expected values.
In this function, we are multiplying a number with ans variable.
'''
def test_ans_mul_number(calc_instance):
    assert calc_instance.mult(10, 5) == 50
    assert calc_instance.mult(calc_instance.ans, -2) == -100
    assert calc_instance.mult(calc_instance.ans, 2) == -200
    
'''
UCID: sb2648
Date: 10/16/23
Here, we are providing the calc_instance as an input for the test_number_div_number method where calc() function can be accessed.
Added few assertions to test the working of division operation for given inputs. 
In assertions, we are testing the division operation on different values to check actual and expected values.
In this function we are performing division on two number.
'''
def test_number_div_number(calc_instance):
    assert calc_instance.div(10, 5) == 2
    assert calc_instance.div(12, -2) == -6
    assert calc_instance.div(-14, 2) == -7
    assert calc_instance.div(-14, -2) == 7
    
'''
UCID: sb2648
Date: 10/16/23
Here, we are providing the calc_instance as an input for the below function test_ans_div_number where calc() function can be accessed.
Added few assertions to test the working of division operation for given inputs.
In assertions, we are testing the multiplication operation on different values to check actual and expected values.
In this function, we are performing division of a number upon ans variable.
'''
def test_ans_div_number(calc_instance):
    assert calc_instance.div(10, 5) == 2
    assert calc_instance.div(calc_instance.ans, -2) == -1
    assert calc_instance.div(calc_instance.ans, 2) == -0.5
    


