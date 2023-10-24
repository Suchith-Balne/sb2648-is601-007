import pytest
# make sure there's an __init__.py in this test folder and that
# the test folder is in the same folder as the mini project content
from PumpkinMachine import PumpkinMachine
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
# this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    return PumpkinMachine()

# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("done")
    machine.handle_pay(2, "2")
    return machine

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order):
    first_order.handle_pumpkin_choice("Large Pumpkin")
    first_order.handle_face_stencil_choice("Spooky Face")
    first_order.handle_face_stencil_choice("Toothy Face")
    first_order.handle_face_stencil_choice("next")
    first_order.handle_extra_choice("LED Candle")
    first_order.handle_extra_choice("Dry Ice")
    first_order.handle_extra_choice("done")
    first_order.handle_pay(5.5,"5.5")
    return first_order

#add required test cases below

#  UCID: sb2648 Date:10/23/23
def test_pumpkin_must_be_first_selection(machine):
    
    # Attempt to select a face stencil without first selecting a pumpkin
    with pytest.raises(InvalidStageException):
        machine.handle_face_stencil_choice("Happy Face")
    
    # Attempting to raise an extra without first selecting a pumpkin
    with pytest.raises(InvalidStageException):
        machine.handle_extra_choice("Small Candle")
        
#  UCID: sb2648 Date:10/23/23
# Define a test case to check if you can only add face stencils if they're in stock
def test_can_only_add_face_stencils_if_in_stock(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    # Reducing the quantity of a face stencil to zero to simulate it being out of stock
    for face_stencil in machine.face_stencils:
        face_stencil.quantity = 0
    
    # Attempting to raise an out-of-stock face stencil
    with pytest.raises(OutOfStockException):
        machine.handle_face_stencil_choice("Happy Face")
        
#  UCID: sb2648 Date:10/23/23
# Define a test case to check if you can only add extras if they're in stock
def test_can_only_add_extras_if_in_stock(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("next")
    # Reduce the quantity of an extra to zero to simulate it being out of stock
    for extra in machine.extras:
        extra.quantity = 0
    
    # Attempt to select an out-of-stock extra
    with pytest.raises(OutOfStockException):
        machine.handle_extra_choice("Small Candle")

#  UCID: sb2648 Date:10/23/23
def test_can_add_up_to_3_face_stencils(machine):
    
    # Select 3 face stencils in different combinations
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("Toothy Face")
    assert machine.remaining_uses == machine.USES_UNTIL_CLEANING - 3  # Checking remaining uses
    assert machine.remaining_stencils == machine.MAX_STENCILS - 3  # Checking remaining stencils
    
#  UCID: sb2648 Date:10/23/23
# Define a test case to check if you can add up to 3 extras of any combination
def test_can_add_up_to_3_extras(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("next")
    # Select 3 extras in different combinations
    machine.handle_extra_choice("LED Candle")
    machine.handle_extra_choice("Small Candle")
    machine.handle_extra_choice("Spooky Sound Effects")
    assert machine.remaining_extras == machine.MAX_EXTRAS - 3  # Checking remaining extras

#  UCID: sb2648 Date:10/23/23
# Defining a list of pumpkins
pumpkins_list = ["Mini Pumpkin", "Small Pumpkin", "Medium Pumpkin", "Large Pumpkin"]
# Defining a parameterized test case to check cost calculation with different pumpkin permutations
@pytest.mark.parametrize("permutation", pumpkins_list)
def test_cost_calculation(permutation, machine):
    for pumpkin in pumpkins_list:  # Selecting three valid pumpkins in different permutations
        machine.pick_pumpkin(pumpkin)
    
    expected_cost = 0.0  # Calculating the expected cost
    for pumpkin in pumpkins_list:
        expected_cost += machine.pumpkins[pumpkins_list.index(pumpkin)].cost
    
    actual_cost = machine.calculate_cost() # Calculating the actual cost
    
    # Checking whether the PumpkinMachine calculates the cost properly and in currency format
    assert actual_cost == expected_cost
    
#  UCID: sb2648 Date:10/23/23
#Define a list of valid pumpkins
valid_pumpkins = ["Mini Pumpkin","Small Pumpkin"]

# Define a parameterized test case to check total sales calculation with different pumpkin permutations
@pytest.mark.parametrize("permutation", valid_pumpkins)
def test_total_sales_calculation(permutation, machine):
    
    # Select three valid pumpkins in different permutations
    for pumpkin in valid_pumpkins:
        machine.pick_pumpkin(pumpkin)
    
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("done")
    # Calculate the expected total sales
    expected_total_sales = 0
    for pumpkin in valid_pumpkins:
        expected_total_sales += machine.pumpkins[valid_pumpkins.index(pumpkin)].cost
    
    # Calculate the actual total sales
    machine.handle_pay(machine.calculate_cost(), "3")  # This will update the internal total_sales variable
    actual_total_sales = machine.total_sales
    
    # Ensure that the PumpkinMachine calculates the total sales properly
    assert actual_total_sales == expected_total_sales
    
#  UCID: sb2648 Date:10/23/23
# Define a test case to check if the total_products variable increments properly
def test_total_products_increment(machine):
    
    # Keep track of the initial total_products value
    initial_total_products = machine.total_products
    
    # Select a valid pumpkin to make a purchase
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("done")
    machine.handle_pay(machine.calculate_cost(), "1")
    
    # Ensure that the total_products variable has incremented
    assert machine.total_products == initial_total_products + 1




