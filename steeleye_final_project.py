import csv
import logging
import os
import xml.etree.ElementTree as ET
import unittest

class TestXMLtoCSV(unittest.TestCase):    #implementing unittest
    
    def setUp(self):
        self.xml_file = "C:\\Users\\satya\\Downloads\\DLTINS_20210117_01of01\\DLTINS_20210117_01of01.xml"
        self.csv_file = "final_steeleyee.csv"
    
    def test_file_conversion(self):
        
        # Check that the CSV file was created
        self.assertTrue(os.path.exists(self.csv_file))
        
        # Check that the CSV file has data in it
        with open(self.csv_file, "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row
            self.assertGreater(len(list(reader)), 0)

# Define the headers for the CSV file
HEADERS = [
    "FinInstrmGnlAttrbts_Id",
    "FinInstrmGnlAttrbts_FullNm",
    "FinInstrmGnlAttrbts_ClssfctnTp",
    "FinInstrmGnlAttrbts_CmmdtyDerivInd",
    "FinInstrmGnlAttrbts_NtnlCcy",
    "Issr"
]

def main():
    #implementing logging
    logging.basicConfig(                      
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    
    """
    Extracting the data from an XML file and writes it to a CSV file.
    """
    # Create a CSV file and writing the headers to it
    with open("final_steeleyee.csv", "w") as csv_file:
        typer = csv.writer(csv_file)
        typer.writerow(HEADERS)
        
        # Parsing the XML file 
        try:
            tree = ET.parse("C:\\Users\\satya\\Downloads\\DLTINS_20210117_01of01\\DLTINS_20210117_01of01.xml")
            root = tree.getroot()
        except ET.ParseError as e:
            logging.exception("Error parsing XML file")
            return
        
        # Looping through each element in the XML file and extract the relevant data
        for temp in tree.iter('TermntdRcrd'):
            f_attr = temp.find("FinInstrmGnlAttrbts")
            if f_attr is not None:
                f_attr_Id = f_attr.find("Id").text
                f_attr_FullNm = f_attr.find("FullNm").text
                f_attr_ClssfctnTp = f_attr.find("ClssfctnTp").text
                f_attr_CmmdtyDerivInd = f_attr.find("CmmdtyDerivInd").text
                f_attr_NtnlCcy = f_attr.find("NtnlCcy").text
            else:
                f_attr_Id = ""
                f_attr_FullNm = ""
                f_attr_ClssfctnTp = ""
                Ff_attr_CmmdtyDerivInd = ""
                f_attr_NtnlCcy = ""
            
            Issr = temp.find("Issr").text
            
            row = [
                f_attr_Id,
                f_attr_FullNm,
                f_attr_ClssfctnTp,
                f_attr_CmmdtyDerivInd,
                f_attr_NtnlCcy,
                Issr
            ]
            
            # Write the data to the CSV file
            typer.writerow(row)
            
        logging.info("Successfully inserted the data")
        

if __name__ == "__main__":
    main()
    unittest.main()