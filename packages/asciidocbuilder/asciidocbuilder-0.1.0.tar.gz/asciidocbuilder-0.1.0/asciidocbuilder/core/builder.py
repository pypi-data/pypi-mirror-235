# builder.py
from elements.structure import Section

class AsciiDocBuilder:
    """
    Main builder class to construct and export AsciiDoc documents.
    """

    def __init__(self, filename):
        self.filename = filename
        # Use the Section class to represent the root of the document
        self.root = Section("", 0)
        self.attributes = {}

    def add_attribute(self, name, value):
        """
        Add an attribute to the document header.
        """
        self.attributes[name] = value

    def add_section(self, section):
        """
        Add a section or subsection to the root.
        """
        self.root.add_element(section)

    def render(self):
        """
        Render the entire document as a string.
        """
        # Render attributes first
        rendered_attributes = "\n".join([f":{name}: {value}" for name, value in self.attributes.items()])
        rendered_content = self.root.render()

        return f"{rendered_attributes}\n\n{rendered_content}"

    def save(self):
        """
        Save the rendered document to the specified file.
        """
        with open(self.filename, 'w') as f:
            f.write(self.render())

# Assuming the Section and other elements classes are imported from their respective modules.
