from lxml import etree

def load_xml(xml_path):
    """
    Loads and parses an XML file.

    Parameters:
    - xml_path (str): The path to the XML file to be loaded.

    Returns:
    - etree.ElementTree: The parsed XML tree, or None if an error occurs.
    """
    try:
        return etree.parse(xml_path)
    except (etree.XMLSyntaxError, FileNotFoundError) as e:
        print(f"Failed to load or parse XML file: {e}")
        return None
    
if __name__ == "__main__":
    xml_path = "tests/xml_files/valid_basic.xml"  # Adjust the path to your test XML file.
    xml_tree = load_xml(xml_path)
    if xml_tree is not None:
        print("XML loaded successfully.")
        # Optionally, print out the root element tag to demonstrate successful loading.
        print("Root element:", xml_tree.getroot().tag)
    else:
        print("Failed to load XML.")