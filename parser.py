#!/bin/python3
import re


def parse_nwodkram(text):
    """Rewrites a text written in Nwodkram and returns the text in corresponding HTML"""

    text = re.sub(r"<(.+?)>\(w=(\d+),h=(\d+)",
        r"<img src=\"\1\" width=\"\2\" height=\"\3\">", text)           # images

    text = re.sub(r"(?!\\)\%(.+?[^\\])\%", r"<b>\1</b>", text)          # bold
    text = re.sub(r"(?!\\)\*(.+?[^\\])\*", r"<i>\1</i>", text)          # italic
    text = re.sub(r"\\(\%|\*)", r"\1", text)                            # removing backslashes

    text = re.sub(r"\[(.+?)\]\(((:?https?:\/\/)?www\.[\w()?$|]+\.[\w/]+?)\)",     # hyperlinks
        r"<a href='http://\2'>\1</a>", text)
    text = re.sub(r"http://(https?://)", r"\1", text)                   # ensure there is not double http://

    text = re.sub(r">>(.+?)\n", r"<blockquote>\1</blockquote>", text)   # blockquote

    text = re.sub(r"\[wp:(.+?)\]",                                      # wikipedia query
        r"<a href='https://en.wikipedia.org/w/index.php?title=Special:Search&search=\1'>wp:\1</a>",
        text)

    return text
