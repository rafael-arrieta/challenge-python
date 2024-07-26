import unittest

def is_balanced(string):
 
  stack = []
  opening_brackets = {
    "(": ")",
    "{": "}",
    "[": "]"
  }

  closing_brackets = set(opening_brackets.values())

  for char in string:
    if char in opening_brackets:
            stack.append(char)
    elif char in closing_brackets:
      if not stack or opening_brackets[stack.pop()] != char:
        return False

  return not stack

class TestBalance(unittest.TestCase):
    def test_balanced_strings(self):
        self.assertTrue(is_balanced(" { [ ( ) ] } "))
        self.assertTrue(is_balanced("(abc1234)"))

    def test_unbalanced_strings(self):
        self.assertFalse(is_balanced("{ [ ) — ( ] }"))
        self.assertFalse(is_balanced("([)]"))
        self.assertFalse(is_balanced("}{"))

if __name__ == '__main__':
    unittest.main()
