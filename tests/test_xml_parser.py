import unittest
from xmltoxsd.xml_parser import load_xml

class TestXMLParser(unittest.TestCase):
    def test_load_xml_valid(self):
        """Test loading a valid XML file."""
        xml_tree = load_xml('tests/xml_files/valid_basic.xml')
        self.assertIsNotNone(xml_tree, "Failed to load a valid XML file.")

    def test_load_xml_invalid(self):
        """Test loading an invalid XML file."""
        xml_tree = load_xml('tests/xml_files/invalid.xml')
        self.assertIsNone(xml_tree, "Incorrectly loaded an invalid XML file.")

if __name__ == '__main__':
    unittest.main()
