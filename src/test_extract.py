import unittest

from extract import *

class TestExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )
    def test_extract_title(self):
        header = extract_title("# Hello\n\n # Hello2")
        self.assertEqual("Hello", header)

    def test_extract_title(self):
        header = extract_title("? Hello\n\n# Hello2")
        self.assertEqual("Hello2", header)
if __name__ == "__main__":
    unittest.main()