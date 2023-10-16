# media.py

from core.base_elements import AsciiDocElement

class ImageElement(AsciiDocElement):
    """
    Represents an image in the AsciiDoc document.
    """

    def __init__(self, path, **attributes):
        super().__init__("", **attributes)
        self.path = path

    def render(self):
        return f"image::{self.path}{self.render_attributes()}[]\n\n"

# Future media types can be added here. For demonstration:
class VideoElement(AsciiDocElement):
    """
    Represents a video in the AsciiDoc document.
    Note: This is just a demonstration. Actual AsciiDoc specifications may vary.
    """

    def __init__(self, path, **attributes):
        super().__init__("", **attributes)
        self.path = path

    def render(self):
        return f"video::{self.path}{self.render_attributes()}[]\n\n"

# More media types, such as audio, can be added as the project evolves.
