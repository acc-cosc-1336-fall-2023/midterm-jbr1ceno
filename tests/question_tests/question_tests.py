#write function tests here, don't add input('') statements here!
import unittest


#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import reverse_string
from src.question_b.question_b import get_miles_per_hour

class Test_Config(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual("dlrow olleh", reverse_string("hello world"))
        print(reverse_string("hello world"))

    def test_get_miles_per_hour(self):
        self.assertEqual(19.883872, get_miles_per_hour(32, 60))
        print(get_miles_per_hour(32, 60))