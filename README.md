# XMLtoXSD Library

The `xmltoxsd` library is a Python tool designed to convert XML documents into XSD (XML Schema Definition) schemas automatically. It simplifies the process of generating XSD schemas from XML files, making it easier for developers to validate their XML data.

## Features

- **Automatic Type Inference**: Automatically determines the data types for XML elements and attributes.
- **Support for Complex XML Structures**: Handles nested elements and attributes with ease.
- **Customizable `minOccurs` Attribute**: Allows users to specify default values for `minOccurs` attribute in the generated XSD.

## Installation

Install `xmltoxsd` using pip:

```bash
pip install xmltoxsd
```

## Quick Start
Here's how to quickly get started with xmltoxsd:
```
from xmltoxsd import XSDGenerator

generator = XSDGenerator()
xsd_schema = generator.generate_xsd("path/to/your/xml_file.xml")
print(xsd_schema)
```

## Usage
To generate an XSD schema from an XML file:
```
with open("output.xsd", "w") as f:
    f.write(xsd_schema)
```

## Contributing
We welcome contributions to the xmltoxsd library. Please read our CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
If you have any questions or encounter issues using the library, please open an issue on my GitHub repository.
