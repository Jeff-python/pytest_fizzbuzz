import pytest
import sys

# L = []
# @pytest.fixture(params=[1,2,3,4,5])
# def populate_list(request):
#   L.append(request.param)
#   return L
  
# @pytest.fixture(params=[1,2,3,4,5])
# def get_num(request):
#   return request.param
  
# def test_L(populate_list, get_num):
#   assert get_num in populate_list


# @pytest.mark.skipif(sys.version_info < (3, 0), reason="requires python3.0 or higher")
# def test_version():
#     return True 



def fizzbuzz(self, val):  
    for i in range(0,100):
        if val % 3 == 0 and val % 5 == 0:
            print("fizzbuzz")
        elif val % 3 == 0:
            print("fizz")
        elif val % 5 == 0:
            print("buzz")
        else:
            print(i)  

          
@pytest.fixture(params=[i for i in range(0,100,15)])
def multiple_15():
    return 
def test_fizzbuzz(multiple_15):
    assert fizzbuzz(multiple_15) == "fizzbuzz"



# @pytest.fixture(params=[i for i in range(0,100)])
# def part_a(request):
#   return request.param

# def test_fizzbuzz(part_a):
#     if part_a % 3 == 0 and part_a % 5 == 0:
#         return "fizzbuzz"

# def test_fizz(part_a):
#     if part_a % 3 == 0:
#         return "fizz"

# def test_buzz(part_a):
#     if part_a % 5 == 0:  
#         return "buzz"     

# def test_number(part_a):
#     if part_a % 5 == 0:  
#         return part_a     
