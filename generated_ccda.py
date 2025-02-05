import xml.etree.ElementTree as ET

def generate_ccda(file_name="generated_ccda.xml"):
    root = ET.Element("ClinicalDocument", xmlns="urn:hl7-org:v3")

    title = ET.SubElement(root, "title")
    title.text = "Patient Health Summary"

    recordTarget = ET.SubElement(root, "recordTarget")
    patientRole = ET.SubElement(recordTarget, "patientRole")
    ET.SubElement(patientRole, "id", extension="12345")

    patient = ET.SubElement(patientRole, "patient")
    name = ET.SubElement(patient, "name")
    ET.SubElement(name, "given").text = "John"
    ET.SubElement(name, "family").text = "Doe"

    ET.SubElement(patient, "birthTime", value="1980-01-01")
    ET.SubElement(patient, "administrativeGenderCode", code="M")

    # Convert to XML string and save
    tree = ET.ElementTree(root)
    tree.write(file_name, encoding="utf-8", xml_declaration=True)
    print(f"CCDA file '{file_name}' generated successfully!")

generate_ccda()
