import logging
import xml.etree.ElementTree as ET
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def group_number(xml_path: Path, group_number: str):

    tree = ET.parse(xml_path)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")
        if number is not None and number.text == group_number:
            timing = group.find("timingExbytes")
            if timing is not None:
                incoming = timing.find("incoming")
                if incoming is not None:
                    return incoming.text
    return None

xml_file = Path("/Users/yehor.bulhakov/PycharmProjects/hillel_2025/lesson_13/homework13/13_3_xml/groups.xml")

#group_num = ("4")
group_num = ("3")
incoming_value = group_number(xml_file, group_num)

if incoming_value is not None:
    logging.info(f"For group/number={group_num} value timingExbytes/incoming: {incoming_value}")
else:
    logging.info(f"Group with number={group_num} not found or missing incoming")