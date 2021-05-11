from __future__ import annotations
from typing import Union

class Tag:
    def __init__(self, name = "", parent: Tag = None) -> None:
        self.name = name
        self.parent = parent
        self.attributes: dict[str, str] = {}
        self.children: list[Tag] = []
        self.content = ""
        self.last_attribute = ""
    def addChild(self, tag: Tag):
        self.children.append(tag)
        tag.parent = self
    def add_attribute(self, name: str, value: str = ""):
        self.attributes[name] = value
        self.last_attribute = name
    def get_last_attribute(self) -> str:
        return self.attributes[self.last_attribute]

class Parser:
    ignore_tags = ['?']
    in_tag = False
    current_tag: Tag = None
    in_attribute = False
    current_attribute = ""
    soon_attribute = False
    def parse(self, s: str) -> Union[Tag, list[Tag]]:
        for l in s:
            if l == '<' and not self.in_tag:
                self.in_tag = True
            elif l == '>' and self.in_tag:
                self.in_tag = False
                self.soon_attribute = False
                self.in_attribute = False
            elif self.in_tag:
                if l == '"':
                    if self.in_attribute:
                        self.current_tag.attributes[self.current_tag.last_attribute] = self.current_attribute
                        self.current_attribute = ""
                        self.soon_attribute = False
                        self.in_attribute = False
                    else:
                        self.in_attribute = True
                elif not self.in_attribute and l == " ":
                    self.soon_attribute = True
                elif l.isalnum():
                    if self.soon_attribute:
                        self.current_attribute += l
                    else:
                        