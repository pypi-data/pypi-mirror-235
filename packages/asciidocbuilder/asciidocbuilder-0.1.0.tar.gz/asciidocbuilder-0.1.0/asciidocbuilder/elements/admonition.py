# admonition.py

from core.base_elements import AsciiDocElement

class Admonition(AsciiDocElement):
    """
    Represents admonitions in the AsciiDoc document.
    Types can include NOTE, WARNING, TIP, IMPORTANT, etc.
    """

    NOTE = "NOTE"
    WARNING = "WARNING"
    TIP = "TIP"
    IMPORTANT = "IMPORTANT"
    CUSTOM = "CUSTOM"

    def __init__(self, type, text):
        super().__init__(text)
        self.type = type

    def render(self):
        return f"{self.type.upper()}: {self.content}\n\n"

# Example usage:
# note = Admonition('NOTE', 'This is a note')
