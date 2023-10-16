# base_elements.py

class AsciiDocElement:
    """
    Base class for all AsciiDoc elements.
    Provides common methods and attributes shared across different elements.
    """

    def __init__(self, content, **attributes):
        self.content = content
        self.attributes = attributes

    def render_attributes(self):
        """
        Render element attributes as a string.
        """
        return "".join([f"[{key}={value}]" for key, value in self.attributes.items()])

    def render(self):
        """
        Render the element as a string.
        Should be overridden by derived classes.
        """
        pass


class TextElement(AsciiDocElement):
    """
    Represents plain text in the document.
    """

    def __init__(self, text):
        super().__init__(text)

    def render(self):
        return self.content


class ContainerElement(AsciiDocElement):
    """
    Base class for elements that can contain other elements.
    E.g., Sections or complex blocks.
    """

    def __init__(self, content="", **attributes):
        super().__init__(content, **attributes)
        self.elements = []

    def add_element(self, element):
        """
        Add a child element to this container.
        """
        self.elements.append(element)

    def render_children(self):
        """
        Render all child elements as a string.
        """
        return "\n".join([element.render() for element in self.elements])
