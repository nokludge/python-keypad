import unittest
from mock import MagicMock
from tests.KeypadGPIOStub import KeypadGPIOStub
from keypad.MatrixKeypad import MatrixKeypad


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        key_map = [
            [1, 2, 3, "A"],
            [4, 5, 6, "B"],
            [7, 8, 9, "C"],
            ["*", 0, "#", "D"]
        ]
        rows = [29, 31, 33, 35]
        columns = [37, 36, 38, 40]
        self.gpio = KeypadGPIOStub()
        self.key_matrix = MatrixKeypad(key_map, rows, columns, self.gpio)

    def test_init(self):
        key_map = [
            [1, 2, 3, "A"],
            [4, 5, 6, "B"],
            [7, 8, 9, "C"],
            ["*", 0, "#", "D"]
        ]
        rows = []
        columns = []
        self.gpio.setmode = MagicMock()
        self.key_matrix = MatrixKeypad(key_map, rows, columns, self.gpio)
        self.gpio.setmode.assert_called_with("")

    def test_get_key_gpio_setup(self):
        self.gpio.setup = MagicMock()
        self.key_matrix.get_key()

        expected_setup = [
            "call([37, 36, 38, 40], 'out')",
            "call([29, 31, 33, 35], '', pull_up_down='')",
            "call(29, '', pull_up_down='')",
            "call(31, '', pull_up_down='')",
            "call(33, '', pull_up_down='')",
            "call(35, '', pull_up_down='')",
            "call([37, 36, 38, 40], '', pull_up_down='')",
        ];

        for item in self.gpio.setup.call_args_list:
            self.assertIn(str(item), expected_setup, "Setup of " + str(item) + " not found.")

        self.assertEquals(4, self.gpio.setup.call_count)

    def test_get_key_gpio_output(self):
        self.gpio.output = MagicMock()
        self.key_matrix.get_key()

        expected_output = [
            "call(37, 0)",
            "call(36, 0)",
            "call(38, 0)",
            "call(40, 0)",
        ];

        for item in self.gpio.output.call_args_list:
            self.assertIn(str(item), expected_output)

        self.assertEquals(4, self.gpio.output.call_count)

    @staticmethod
    def my_side_effect(*args, **kwargs):
        if args[0] == 29:
            return 0
        elif args[0] == 37:
            return 1
        else:
            return 2

    def test_get_key_reads_input(self):
        self.gpio.input = MagicMock(side_effect=self.my_side_effect)
        self.key_matrix.get_key()

        self.assertEquals(8, self.gpio.input.call_count)

    def test_get_key_one_one(self):
        self.gpio.input = MagicMock(side_effect=self.my_side_effect)
        pressed_key = self.key_matrix.get_key()

        self.assertEquals(1, pressed_key)

    def test_get_key_round_trip(self):
        self.gpio.input = MagicMock(side_effect=self.my_side_effect)
        self.gpio.setup = MagicMock()
        self.gpio.output = MagicMock()
        self.key_matrix.get_key()

        self.assertEquals(8, self.gpio.input.call_count)
        self.assertEquals(5, self.gpio.output.call_count)
        self.assertEquals(6, self.gpio.setup.call_count)


if __name__ == '__main__':
    unittest.main()
