#write function tests here, don't add input('') statements here!
import unittest

from src.question_a.question_a import reverse_string
from src.question_b.question_b import get_miles_per_hour
from src.question_c.question_c import get_bonus_pay_amount
from src.question_d.question_d import get_person_category


#follow this example to add questions b, c, and d for testing including their functions


class Test_Config(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual("dlrow olleh", reverse_string("hello world"))
        print(reverse_string("hello world"))

    def test_get_miles_per_hour(self):
        self.assertEqual(19.883872, get_miles_per_hour(32, 60))
        print(get_miles_per_hour(32, 60))

    def test_get_bonus_pay_amount(self):
        self.assertEqual("Invalid", get_bonus_pay_amount(-1))
        self.assertEqual(10, get_bonus_pay_amount(200))
        self.assertEqual(36, get_bonus_pay_amount(600))
        self.assertEqual(70, get_bonus_pay_amount(1000))
        self.assertEqual(120, get_bonus_pay_amount(1500))
        #self.assertEqual(0, get_bonus_pay_amount(0))
        self.assertEqual("Invalid", get_bonus_pay_amount(2000))
        #print(get_bonus_pay_amount(0))

    def test_get_person_category(self):
        self.assertEqual("infant", get_person_category(1))
        self.assertEqual("child", get_person_category(2))
        self.assertEqual("teenager", get_person_category(14))
        self.assertEqual("adult", get_person_category(20))
        #print(get_person_category(20))