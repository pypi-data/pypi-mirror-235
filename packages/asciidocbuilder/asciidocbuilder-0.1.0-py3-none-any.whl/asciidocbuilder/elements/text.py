# text.py

from core.base_elements import TextElement

class BoldTextElement(TextElement):
    """
    Represents bold text in the document.
    """

    def render(self):
        return f"*{self.content}*"


class ItalicTextElement(TextElement):
    """
    Represents italicized text in the document.
    """

    def render(self):
        return f"_{self.content}_"


class MonospaceTextElement(TextElement):
    """
    Represents monospaced (code-like) text in the document.
    """

    def render(self):
        return f"`{self.content}`"
