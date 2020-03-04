import unittest
import myGlobal
import stack


class TestCaseStack(unittest.TestCase):
    def test_a_pushStack_global_stack_push_123_expect_123_pushed(self):
        stack.initStack(myGlobal.myStack)       # Clear the element in stack
        stack.pushStack(myGlobal.myStack, "123")  # Push the data as first element
        self.assertEqual("123", myGlobal.myStack[0])  # Verify the first element

    def test_b_popStack_stack_given_123_456_expected_pop_456_123(self):
        # Stack is Last In First Out (LIFO)
        # Thus, the last element in the stack will be pop out first
        localStack = [123, 456]
        self.assertEqual(456, stack.popStack(localStack))
        self.assertEqual(123, stack.popStack(localStack))


if __name__ == '__main__':
    unittest.main()
