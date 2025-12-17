import unittest

from ex4_325130417 import *

class MyTestCase(unittest.TestCase):
    class CountedString(str):
        # Global variable to track the count of string objects
        created_count = 0

        def __init__(self, value):
            self.value = value

        def __getitem__(self, index):
            # Check if a slice operation is being performed
            if isinstance(index, slice):
                CountedString.created_count += 1

            return CountedString(self.value[index])


    '''Question 1.a'''
    def test_fourbonacci_rec(self):
        ret_val = fourbonacci_rec(0)
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = fourbonacci_rec(12)
        answer = 1174
        self.assertEqual(answer, ret_val) # add assertion here
        ret_val = fourbonacci_rec(25)
        answer = 5953572
        self.assertEqual(answer, ret_val)  # add assertion here

    '''Question 1.b'''
    def test_k_bonacci(self):
        ret_val = k_bonacci(0 , 2)
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = k_bonacci(5 , 2)
        answer = 5
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = k_bonacci(8 , 2)
        answer = 21
        self.assertEqual(answer, ret_val) # add assertion here

        ret_val = k_bonacci(0, 3)
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = k_bonacci(5, 3)
        answer = 11
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = k_bonacci(8, 3)
        answer = 68
        self.assertEqual(answer, ret_val)

        ret_val = k_bonacci(0, 5)
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = k_bonacci(5, 5)
        answer = 10
        self.assertEqual(answer, ret_val)


    '''Question 2.a'''
    def test_climb_combinations(self):
        ret_val = climb_combinations(1)
        answer = 1
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = climb_combinations(5)
        answer = 8
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = climb_combinations(6)
        answer = 13
        self.assertEqual(answer, ret_val)  # add assertion here

        # Additional tests
        ret_val = climb_combinations(19)
        answer = 6765
        self.assertEqual(answer, ret_val)
        ret_val = climb_combinations(2)
        answer = 2
        self.assertEqual(answer, ret_val)

    '''Question 2.b'''
    def test_tomer_climb_combinations(self):
        ret_val = tomer_climb_combinations(6, [2,3])
        answer = 2
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = tomer_climb_combinations(3, [2])
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = tomer_climb_combinations(10, [5,2])
        answer = 2
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = tomer_climb_combinations(5, [5, 2, 1])
        answer = 9
        self.assertEqual(answer, ret_val)  # add assertion here

        # Additional tests

        ret_val = tomer_climb_combinations(5, [6])
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = tomer_climb_combinations(6, [5])
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = tomer_climb_combinations(10, [1])
        answer = 1
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = tomer_climb_combinations(10, [1,1])
        answer = 1024
        self.assertEqual(answer, ret_val)  # add assertion here


    '''Question 3.a'''
    def test_weigh_str(self):
        ret_val = weigh_str("a")
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str("aba")
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str("aa")
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str("AZ")
        answer = -1
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str("cba")
        answer = 1
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str("acsabdrZ")
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str("DDDDaaaa")
        answer = -4
        self.assertEqual(answer, ret_val)  # add assertion here

        # Additional tests
        ret_val = weigh_str("DDDDfffaaaa")
        answer = -4
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str("AAaa")
        answer = -2
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str("12.33")
        answer = -2
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str("babababababa")
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here

    '''Question 3.b'''
    def test_weigh_str_efficient(self):
        ret_val = weigh_str_efficient("a")
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str_efficient("aba")
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str_efficient("aa")
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str_efficient("AZ")
        answer = -1
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str_efficient("cba")
        answer = 1
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = weigh_str_efficient("acsabdrZ")
        answer = 0
        should_create = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        self.assertEqual(should_create, CountedString.created_count)  # add assertion here
        ret_val = weigh_str_efficient("DDDDaaaa")
        answer = -4
        should_create = 0
        self.assertEqual(answer, ret_val)   # add assertion here
        self.assertEqual(should_create, CountedString.created_count)    # add assertion here

        # Additional tests
        ret_val = weigh_str_efficient("DDDDfffaaaa")
        answer = -4
        should_create = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        self.assertEqual(should_create, CountedString.created_count)  # add assertion here
        ret_val = weigh_str_efficient("AAaa")
        answer = -2
        should_create = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        self.assertEqual(should_create, CountedString.created_count)  # add assertion here
        ret_val = weigh_str_efficient("12.33")
        answer = -2
        should_create = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        self.assertEqual(should_create, CountedString.created_count)  # add assertion here
        ret_val = weigh_str_efficient("babababababa")
        answer = 0
        should_create = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        self.assertEqual(should_create, CountedString.created_count)  # add assertion here


    '''Question 4.a'''
    def test_sum_nested(self):
        ret_val = sum_nested([1, 2, [3, 4], [5, [6, 7], 8], 9])
        answer = 45
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = sum_nested([1, 2, [-3, -4.5]])
        answer = 10.5
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = sum_nested([1, 2, [-3, -4.5], 'abc', [5, 'abc', [-4, 0.5]]])
        answer = 20.
        self.assertEqual(answer, ret_val)  # add assertion here

        # Additional tests
        ret_val = sum_nested([[[[[['a']]]]]])
        answer = 0
        self.assertEqual(answer, ret_val)
        ret_val = sum_nested([[[[[[1],1],1],1],1],1])
        answer = 6
        self.assertEqual(answer, ret_val)
        ret_val = sum_nested([[1,2.25,3,4.25,'a'],[-1.0,-2,-3.5,-4,'b'],0])
        answer = 21
        self.assertEqual(answer, ret_val)


    '''Question 4.b'''
    def test_count_construct(self):
        ret_val = count_construct('purple', ["purp", "p", "ur", "le", "purpl"])
        answer = 2
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = count_construct('abcdef', ["ab", "abc", "cd", "def", "abcd"])
        answer = 1
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = count_construct('aaaaaaaaaaaaaaaaaaaaaaaz', ["a", "aa", "aaa", "aaaa", "aaaaa"])
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here

        # Additional tests
        ret_val = count_construct('', ['a','b','c','d','1',1])
        answer = 1
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = count_construct('nah', [])
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = count_construct('twice', ['twice','twice'])
        answer = 2
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = count_construct('no space', ['no', 'space'])
        answer = 0
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = count_construct('yes space', ['yes', ' space'])
        answer = 1
        self.assertEqual(answer, ret_val)  # add assertion here


    '''Question 5'''
    def test_gcd(self):
        ret_val = gcd(98, 56)
        answer = 14
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = gcd(42, 56)
        answer = 14
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = gcd(3, 6)
        answer = 3
        self.assertEqual(answer, ret_val)  # add assertion here

        # Additional tests
        ret_val = gcd(17, 17)
        answer = 17
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = gcd(17, 19)
        answer = 1
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = gcd(36, 1)
        answer = 1
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = gcd(0, 1)
        answer = 1
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = gcd(-5, 5)
        answer = 5
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = gcd(-36, -24)
        answer = 12
        self.assertEqual(answer, ret_val)  # add assertion here
        ret_val = gcd(123456, 789012)
        answer = 12
        self.assertEqual(answer, ret_val)  # add assertion here





if __name__ == '__main__':
    unittest.main()
