import unittest
from xmltoxsd.schema_inferer import infer_type

class TestSchemaInferer(unittest.TestCase):
    def test_infer_type_date(self):
        self.assertEqual(infer_type("2023-01-01"), "xs:date", "Failed to infer xs:date type.")

    def test_infer_type_datetime(self):
        self.assertEqual(infer_type("2023-01-01T12:00:00Z"), "xs:dateTime", "Failed to infer xs:dateTime type.")

    def test_infer_type_integer(self):
        self.assertEqual(infer_type("12345"), "xs:integer", "Failed to infer xs:integer type.")

    def test_infer_type_string(self):
        self.assertEqual(infer_type("Some text"), "xs:string", "Failed to infer xs:string type.")

    def test_infer_type_string(self):
        self.assertEqual(infer_type(True), "xs:boolean", "Failed to infer xs:boolean type.")

if __name__ == '__main__':
    unittest.main()
