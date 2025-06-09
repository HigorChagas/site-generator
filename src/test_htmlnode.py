from htmlnode import HTMLNode

def test_props_to_html_with_multiple_props():
    node = HTMLNode(
        tag="a",
        value="Google",
        props={"href": "https://www.google.com", "target": "_blank"}
    )
    result = node.props_to_html()
    expected = ' href="https://www.google.com" target="_blank"'
    assert result == expected, f"Esperado: {expected}, mas retornou: {result}"

def test_props_to_html_with_no_props():
    node = HTMLNode(tag="p", value="Sem props")
    result = node.props_to_html()
    expected = ''
    assert result == expected, f"Esperado: '{expected}', mas retornou: '{result}'"

def test_repr_returns_string():
    node = HTMLNode(tag="h1", value="Título", props={"class": "heading"})
    result = repr(node)
    assert isinstance(result, str), "O __repr__ deveria retornar uma string"

if __name__ == "__main__":
    test_props_to_html_with_multiple_props()
    test_props_to_html_with_no_props()
    test_repr_returns_string()
    print("✅ Todos os testes passaram!")
