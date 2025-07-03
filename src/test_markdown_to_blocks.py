import unittest

from textnode import TextType, TextNode
from textblocks import BlockType, block_to_block_type, markdown_to_blocks
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_blocktype(self):
        md = """
>This is some quote block
>It has several lines

>This is some fake quote block
It has not all lines srarting with '>'
>Some other lines are like that though

```
    def somefunc(): # this is a code block
        print("hello")
```

```
    This block starts with three backticks but ends with none

- this
- is
- an unordered list

- this is
a broken list
- so it isn't a list

# This is a Heading

## This is also a Heading

###this isn't a heading though

##### A heading again

this is just a paragraph
it has some lines
ans ends with backticks for no reason ```

1. this is an ordered list
2. it's elements are in order
3. no gaps, no unordered indices

1. this one is broken though
2. it looks like a good one
4. but it isn't
"""
        blocks = markdown_to_blocks(md)

        self.assertEqual(block_to_block_type(blocks[0]), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(blocks[1]), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(blocks[2]), BlockType.CODE)
        self.assertEqual(block_to_block_type(blocks[3]), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(blocks[4]), BlockType.ULIST)
        self.assertEqual(block_to_block_type(blocks[5]), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(blocks[6]), BlockType.HEADING)
        self.assertEqual(block_to_block_type(blocks[7]), BlockType.HEADING)
        self.assertEqual(block_to_block_type(blocks[8]), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(blocks[9]), BlockType.HEADING)
        self.assertEqual(block_to_block_type(blocks[10]), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(blocks[11]), BlockType.OLIST)
        self.assertEqual(block_to_block_type(blocks[12]), BlockType.PARAGRAPH)


    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()



