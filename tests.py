import unittest, datetime
import my_module
from my_module import MyClass, SomeOtherClass
from mock import patch, Mock


class SomeOtherClassTest(unittest.TestCase):
    @patch.object(my_module.MyClass, 'my_method')
    def test_my_method_shouldReturnTrue_whenMyMethodReturnsSomeValue(self, mock_my_method):
        # setup
        mock_my_method.return_value = True
        some_other_class = SomeOtherClass()

        # execute
        result = some_other_class.method_under_test()

        # assert
        self.assertTrue(result)

    @patch('my_module.MyClass')
    def test_my_method_shouldCallMyClassMethodMyMethod_whenSomeOtherClassMethodIsCalled(self, mock_my_class):
        # setup
        some_other_class = SomeOtherClass()

        # execute
        some_other_class.method_under_test()

        # assert
        self.assertTrue(mock_my_class.called)

    @patch('my_module.MyClass')
    def test_my_method_shouldReturnTrue_whenSomeOtherClassMethodIsCalledAndAReturnValueIsSet(self, mock_my_class):
        # setup
        mc = mock_my_class.return_value
        mc.my_method.return_value = True
        some_other_class = SomeOtherClass()

        # execute
        result = some_other_class.method_under_test()

        # assert
        self.assertTrue(result)

    @patch.object(my_module.MyClass, 'my_method')
    def test_my_method_shouldReturnMultipleValues_whenMyMethodReturnsSomeValue(self, mock_my_method):
        # setup
        list_of_return_values = [True, False, False]

        def side_effect():
            return list_of_return_values.pop()

        mock_my_method.side_effect = side_effect

        # execute
        some_other_class = SomeOtherClass()

        # assert
        self.assertFalse(some_other_class.method_under_test())
        self.assertFalse(some_other_class.method_under_test())
        self.assertTrue(some_other_class.method_under_test())


if __name__ == '__main__':
    unittest.main()