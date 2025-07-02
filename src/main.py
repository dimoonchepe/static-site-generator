import re
from textnode import TextType, TextNode
from leafnode import LeafNode


def main():
    node = TextNode("BootDev rules!", TextType.BOLD, "http://boot.dev")
    print(node)


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.PLAINTEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Unknown text node type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.PLAINTEXT:
            result.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) % 2 != 1:
                raise Exception(f"Wrong markdown format: there's no closing delimiter '{delimiter}' in node '{node.text}'")
            res_nodes = []
            for i in range(0, len(parts) - 1, 2):
                res_nodes.append(TextNode(parts[i], TextType.PLAINTEXT))
                res_nodes.append(TextNode(parts[i + 1], text_type))
            last_part = parts[len(parts) - 1]
            if (len(last_part) > 0):
                res_nodes.append(TextNode(last_part, TextType.PLAINTEXT))
            result.extend(res_nodes)
    return result   


def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images


def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links


def split_node_with_item(node, delimiter, item, item_type):
    if not node.text:
        return []
    if node.text_type == TextType.IMAGE or node.text_type == TextType.LINK:
        return[node]
    
    parts = node.text.split(delimiter, 1)
    if len(parts) < 2:
        return[node]

    result = []
    if len(parts[0]) > 0:
        result.append(TextNode(parts[0], node.text_type))
    result.append(TextNode(item[0], item_type, item[1]))
    if len(parts[1]) > 0:
        result.append(TextNode(parts[1], node.text_type))

    return result


def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if not node.text:
            continue

        extracted = extract_markdown_images(node.text)
        if not extracted:
            result.append(node)
            continue
        
        node_result = [node]
        for img in extracted:
            new_result = []
            for n in node_result:
                new_result.extend(split_node_with_item(n, f"![{img[0]}]({img[1]})", img, TextType.IMAGE))
            node_result = new_result
        result.extend(node_result)

    return result   


def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if not node.text:
            continue

        extracted = extract_markdown_links(node.text)
        if not extracted:
            result.append(node)
            continue
        
        node_result = [node]
        for link in extracted:
            new_result = []
            for n in node_result:
                new_result.extend(split_node_with_item(n, f"[{link[0]}]({link[1]})", link, TextType.LINK))
            node_result = new_result
        result.extend(node_result)

    return result   


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.PLAINTEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes


def markdown_to_blocks(text):
    return list(filter(lambda t: len(t) > 0, map(lambda s: s.strip(), text.split('\n\n'))));


main()


