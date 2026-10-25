import unittest
from lxml import etree
from xmltoxsd.xsd_generator import XSDGenerator

class TestXSDGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = XSDGenerator()

    def test_generate_xsd_basic(self):
        """Test generating XSD from a basic XML file."""
        xsd_schema = self.generator.generate_xsd('tests/xml_files/nested_elements.xml', min_occurs="0")
        self.assertIn('<xs:schema', xsd_schema, "Generated XSD does not contain schema definition.")

    def test_generated_xsd_compiles(self):
        """Test that the generated XSD is itself a valid schema."""
        xsd_schema = self.generator.generate_xsd('tests/xml_files/nested_elements.xml', min_occurs="0")
        # Raises XMLSchemaParseError if the schema is invalid
        etree.XMLSchema(etree.fromstring(xsd_schema.encode()))

    # Add more tests for different XML structures and min_occurs configurations

if __name__ == '__main__':
    unittest.main()
