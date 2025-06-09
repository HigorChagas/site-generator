import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_com_tag_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_com_tag_a_e_props(self):
        node = LeafNode("a", "Google", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">Google</a>')

    def test_to_html_com_multiplos_props(self):
        props = {"href": "https://google.com", "target": "_blank"}
        node = LeafNode("a", "Google", props)
        self.assertEqual(node.to_html(), '<a href="https://google.com" target="_blank">Google</a>')

    def test_to_html_sem_tag(self):
        node = LeafNode(None, "Texto puro")
        self.assertEqual(node.to_html(), "Texto puro")

    def test_erro_se_value_for_none(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

    def test_to_html_com_tag_b(self):
        node = LeafNode("b", "Negrito")
        self.assertEqual(node.to_html(), "<b>Negrito</b>")
    
if __name__ == "__main__":
    unittest.main()
    print("✅ Todos os testes passaram!")
    