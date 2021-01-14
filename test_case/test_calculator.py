import unittest
from calculator import Caltulator

class TestCalculator(unittest.TestCase):

  def test_add(self):
    c = Caltulator(3, 5)
    result = c.add()
    print(result)
    self.assertEqual(result, 9)
  
  def test_sub(self):
    c = Caltulator(7, 2)
    result = c.sub()
    self.assertEqual(result, 6)


    
def test_mul():
  c = Caltulator(3, 3)
  result = c.mul()
  assert result == 3, 'Multiplication failed'

def test_div():
  c = Caltulator(6, 2)
  result = c.div()
  assert result == 2, 'Division operation failed'


if __name__ == '__main__':
  #unittest.main()
  test_mul()
  test_div()





