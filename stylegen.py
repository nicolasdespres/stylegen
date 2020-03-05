#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""Generate random penalties for office training class in primary school.
"""


import sys
import argparse
import random


COLORS = tuple("blue red green black cyan magenta".split())
FONT_SIZE = (50, 100, 200)
FORMATTINGS = ("b", "i", "u", None)


def read_text_file(path):
    title = None
    text = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if title is None:
                title = line
            elif not text and not line:
                pass
            else:
                text.append(line)
    return (title, text)

def write_text_file(path, content):
    with open(path, "w") as fout:
        fout.write(content)

def tag(tag, content=None, **attrs):
    s = [f"<{tag}"]
    if attrs:
        s.append(" ")
        for name, value in attrs.items():
            s.append(f'{name}="{value}"')
    if content is None:
        s.append("/>")
    else:
        s.append(">")
        s.append(content)
        s.append(f"</{tag}>")
    return "".join(s)

DEFAULT_RANDOM_PART = 0.70

def generate_body(text, random_part=DEFAULT_RANDOM_PART):
    s = []
    for line in text:
        if line:
            s.append("<div>")
            for word in line.split():
                if random.random() > 1 - random_part:
                    color = random.choice(COLORS)
                    font_size = random.choice(FONT_SIZE)
                    formatting = random.choice(FORMATTINGS)
                else:
                    color = "black"
                    font_size = 100
                    formatting = None
                word = tag("span", word + " ",
                           style=f"color:{color};font-size:{font_size}%")
                if formatting is not None:
                    word = tag(formatting, word)
                s.append(word)
            s.append("</div>")
        else:
            s.append(tag("br"))
    return "\n".join(s)

def generate(text, title, **kwargs):
    header = f"""\
<!DOCTYPE html>
<html>
  <meta charset="UTF-8">
  <head>
    <title>{title}</title>
  </head>
  <body>
  <h1>{title}</h1>
"""
    body = generate_body(text, **kwargs)
    footer = """\
  </body>
</html>
"""
    return header + body + footer

def build_cli():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "--random-part",
        action="store",
        type=float,
        default=DEFAULT_RANDOM_PART,
        help="Percentage of word formatted randomly (between 0 and 1)")
    parser.add_argument(
        "input_file",
        action="store",
        help="The base text file.")
    parser.add_argument(
        "output_file",
        action="store",
        help="The base text file.")
    return parser

def main(argv):
    cli = build_cli()
    options = cli.parse_args(argv[1:])
    random.seed()
    title, text = read_text_file(options.input_file)
    output = generate(text, title, random_part=options.random_part)
    write_text_file(options.output_file, output)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
