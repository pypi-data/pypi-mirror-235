# structure.py

from .base_elements import ContainerElement

class Section(ContainerElement):
    """
    Represents a section in the AsciiDoc document.
    """

    def __init__(self, title, level=1):
        super().__init__(title)
        self.level = level

    def render(self):
        section_header = f"{'='*self.level} {self.content}\n\n"
        return section_header + self.render_children()


class SubSection(Section):
    """
    Represents a subsection in the AsciiDoc document.
    """

    def __init__(self, title):
        super().__init__(title, level=2)


class SubSubSection(Section):
    """
    Represents a sub-subsection in the AsciiDoc document.
    """

    def __init__(self, title):
        super().__init__(title, level=3)


class Paragraph(ContainerElement):
    """
    Represents a paragraph in the AsciiDoc document.
    """

    def render(self):
        return f"{self.content}\n\n"

# More structural elements can be added as needed.
