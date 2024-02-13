import re

def infer_type(text):
    """
    Infers the XML Schema data type based on the text content.

    Parameters:
    - text (str): Text content of an XML element or attribute.

    Returns:
    - str: Suggested XSD data type (e.g., xs:string, xs:date, xs:dateTime).
    """

    # Check for boolean values first
    if isinstance(text, bool):
        return "xs:boolean"

    # Ensure the input is a string before trying to strip it
    if not isinstance(text, str):
        text = str(text)
        
    cleaned_text = text.strip('\'"')

    date_pattern = r"^\d{4}-\d{2}-\d{2}$"
    datetime_pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}([+-]\d{2}:\d{2}|Z)?$"
    
    if re.match(date_pattern, cleaned_text):
        return "xs:date"
    elif re.match(datetime_pattern, cleaned_text):
        return "xs:dateTime"
    elif cleaned_text.isdigit():
        return "xs:integer"
    elif re.match(r"^\d+\.\d+$", cleaned_text):
        return "xs:decimal"
    return "xs:string"

if __name__ == "__main__":
    test_strings = ["2023-11-27", "2023-11-27T21:30:00+08:00", "123", "true", "example text"]
    for text in test_strings:
        print(f"Text: {text} inferred as {infer_type(text)}")