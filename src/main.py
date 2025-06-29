from textnode import TextType, TextNode

def main():
    node = TextNode("BootDev rules!", TextType.BOLD, "http://boot.dev")
    print(node)


main()
