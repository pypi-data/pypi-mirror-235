from asciidocbuilder.core.builder import AsciiDocBuilder
from asciidocbuilder.elements.text import TextElement, BoldTextElement, ItalicTextElement, MonospaceTextElement
from asciidocbuilder.elements.structure import Section, SubSection
from asciidocbuilder.elements.admonition import Admonition
from asciidocbuilder.elements.list import ListElement
from asciidocbuilder.elements.media import ImageElement

def create_simple_document():
    # Create a new AsciiDoc document
    doc = AsciiDocBuilder("sample_output.adoc")
    
    # Add global attributes to the document
    doc.add_attribute("toc", "")
    doc.add_attribute("sectnums", "")
    
    # Create and add a main section
    section1 = Section("Introduction", 1)
    
    # Add text elements to this section
    section1.add_element(TextElement(f"This is a {BoldTextElement('bold').render()} statement."))
    section1.add_element(TextElement(f"This is an {ItalicTextElement('italic').render()} statement."))
    section1.add_element(TextElement(f"This showcases {MonospaceTextElement('monospace').render()} font."))
    
    # Add admonitions to this section
    section1.add_element(Admonition("NOTE", "This is just a simple note."))
    section1.add_element(Admonition("WARNING", "This is a warning. Proceed with caution!"))
    
    # Create and add a subsection
    subsection1 = SubSection("Details", 2)
    subsection1.add_element(TextElement("Here are more details about the topic."))
    subsection1.add_element(ListElement(["Point 1", "Point 2", "Point 3"], ordered=True))  # Ordered list
    section1.add_element(subsection1)
    
    # Add an image
    section1.add_element(ImageElement("sample_image.png", alt="Sample Image"))
    
    # Add main section to the document
    doc.root.add_element(section1)
    
    # Save the document to a file
    doc.save()

if __name__ == "__main__":
    create_simple_document()
