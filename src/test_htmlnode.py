import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is a HTML node", "Test")
        node2 = HTMLNode("This is a HTML node", "Test")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("This is a text node", "Test")
        node2 = HTMLNode("This is a text node", "Test2")
        self.assertNotEqual(node, node2)
    
    def test_not_children(self):
        node = HTMLNode("This is a text node", "Test", "Test2")
        node2 = HTMLNode("This is a text node", "Test" )
        self.assertNotEqual(node, node2)
    
    


if __name__ == "__main__":
    unittest.main()