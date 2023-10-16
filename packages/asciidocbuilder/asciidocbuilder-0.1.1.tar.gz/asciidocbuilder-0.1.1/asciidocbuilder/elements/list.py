# list.py

from core.base_elements import ContainerElement, TextElement

class ListElement(ContainerElement):
    """
    Represents generic lists in the AsciiDoc document, including unordered, ordered, and checklists.
    """

    def __init__(self, items, ordered=False, checklist=False):
        super().__init__()
        self.ordered = ordered
        self.checklist = checklist
        for item in items:
            self.add_element(TextElement(item))

    def render(self):
        prefix = "* "
        if self.ordered:
            prefix = ". "
        elif self.checklist:
            prefix = "- [ ] "

        return prefix + prefix.join([item.render() for item in self.elements]) + "\n\n"


class OrderedListElement(ListElement):
    """
    Represents ordered lists in the AsciiDoc document.
    """

    def __init__(self, items):
        super().__init__(items, ordered=True)


class UnorderedListElement(ListElement):
    """
    Represents unordered lists in the AsciiDoc document.
    """

    def __init__(self, items):
        super().__init__(items)


class ChecklistElement(ListElement):
    """
    Represents checklist in the AsciiDoc document.
    """

    def __init__(self, items):
        super().__init__(items, checklist=True)

