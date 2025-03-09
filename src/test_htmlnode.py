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
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello World")
        self.assertEqual(node.to_html(), "<p>Hello World</p>")
    
    def test_leaf_to_html_None(self):
        node = LeafNode(None, "Hello World")
        self.assertEqual(node.to_html(), "Hello World")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Link", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Link</a>')

if __name__ == "__main__":
    unittest.main()