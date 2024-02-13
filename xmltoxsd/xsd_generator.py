from lxml import etree
from .xml_parser import load_xml
from .schema_inferer import infer_type

class XSDGenerator:
    def __init__(self):
        self.ns_map = {"xs": "http://www.w3.org/2001/XMLSchema"}
        self.xsd = None

    def generate_xsd(self, xml_path, min_occurs="0"):
        """
        Generates an XSD schema for the given XML file.

        Parameters:
        - xml_path (str): Path to the XML file.
        - min_occurs (str): Default minOccurs value for elements.
        """
        xml_tree = load_xml(xml_path)
        if xml_tree is not None:
            self.xsd = etree.Element("{http://www.w3.org/2001/XMLSchema}schema", nsmap=self.ns_map)
            self.process_element(xml_tree.getroot(), self.xsd, min_occurs=min_occurs)
            return etree.tostring(self.xsd, pretty_print=True).decode()
        else:
            return "Failed to generate XSD schema."

    def process_element(self, element, parent, min_occurs="1"):
        """
        Recursively processes an XML element to generate its XSD representation.

        Parameters:
        - element (etree.Element): The current XML element.
        - parent (etree.Element): The parent element in the XSD schema.
        - min_occurs (str): The minOccurs value for the element.
        """
        ns = "{http://www.w3.org/2001/XMLSchema}"
        element_name = element.tag.split('}')[-1]
        element_def = etree.SubElement(parent, f"{ns}element", name=element_name, minOccurs=min_occurs, maxOccurs="1")
        
        if len(element) > 0 or len(element.attrib):
            complex_type = etree.SubElement(element_def, f"{ns}complexType")
            sequence = etree.SubElement(complex_type, f"{ns}sequence")
            for child in element:
                self.process_element(child, sequence, min_occurs)
            for attr_name, attr_value in element.attrib.items():
                attr_type = infer_type(attr_value)
                etree.SubElement(complex_type, f"{ns}attribute", name=attr_name, type=attr_type)
        else:
            element_def.set('type', infer_type(element.text))

if __name__ == "__main__":
    generator = XSDGenerator()
    xml_path = "tests/xml_files/valid_basic.xml"  # Update this path to your XML file.
    xsd_schema = generator.generate_xsd(xml_path, min_occurs="0")
    if xsd_schema:
        # print("XSD Schema Generated Successfully:")
        print(xsd_schema)
    else:
        print("Failed to generate XSD schema.")