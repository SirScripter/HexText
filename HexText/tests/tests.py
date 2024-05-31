import unittest
from hextext import HexText

class TestHexText(unittest.TestCase):

    def setUp(self):
        self.hex_text = HexText()

    def test_solid_color(self):
        text = "Hello, World!"
        color = "#FF5733"
        colored_text = self.hex_text(text, color=color)
        expected_start = "\033[38;2;255;87;51m"
        expected_end = "\033[0m"
        self.assertTrue(colored_text.startswith(expected_start) and colored_text.endswith(expected_end))
        self.assertIn(text, colored_text)

    def test_gradient_single_color(self):
        text = "Hello, World!"
        gradient = ["#FF5733"]
        gradient_text = self.hex_text(text, gradient=gradient)
        expected_start = "\033[38;2;255;87;51m"
        expected_end = "\033[0m"
        self.assertTrue(gradient_text.startswith(expected_start) and gradient_text.endswith(expected_end))
        self.assertIn(text, gradient_text)

    def test_gradient_multiple_colors(self):
        text = "Hello"
        gradient = ["#FF5733", "#33FF57"]
        gradient_text = self.hex_text(text, gradient=gradient)
        self.assertTrue("\033[38;2;" in gradient_text)
        self.assertTrue(gradient_text.endswith("\033[0m"))
        self.assertIn("H", gradient_text)
        self.assertIn("e", gradient_text)
        self.assertIn("l", gradient_text)
        self.assertIn("o", gradient_text)

    def test_invalid_color(self):
        text = "Hello, World!"
        with self.assertRaises(ValueError):
            self.hex_text.hex_to_rgb("#ZZZZZZ")

    def test_apply_solid_color(self):
        text = "Hello"
        color = "#FF5733"
        colored_text = self.hex_text.apply_solid_color(text, color)
        expected_start = "\033[38;2;255;87;51m"
        expected_end = "\033[0m"
        self.assertTrue(colored_text.startswith(expected_start) and colored_text.endswith(expected_end))
        self.assertIn(text, colored_text)

    def test_apply_gradient(self):
        text = "Hello"
        gradient = ["#FF5733", "#33FF57"]
        gradient_text = self.hex_text.apply_gradient(text, gradient)
        self.assertTrue("\033[38;2;" in gradient_text)
        self.assertTrue(gradient_text.endswith("\033[0m"))
        self.assertIn("H", gradient_text)
        self.assertIn("e", gradient_text)
        self.assertIn("l", gradient_text)
        self.assertIn("o", gradient_text)

if __name__ == '__main__':
    unittest.main()
