import xml.etree.ElementTree as ET
import os
import pandas as pd
import logging


# =============================================================================


logging.basicConfig(level=logging.INFO, 
                format='%(asctime)s [%(levelname)s] %(message)s')


# =============================================================================


def write_xml_to_csv(csv_name, xml_path):

    # Create dataframe 
    df = pd.DataFrame()

    # Load xml file and add data to .csv file 
    for name in os.listdir(xml_path):
        full_path = os.path.join(xml_path, name)
        root = ET.parse(full_path).getroot()
        
        width = [width.text for width in root.iter('width')][0]
        height = [height.text for height in root.iter('height')][0]
        _class = [_class.text for _class in root.iter('name')][0]
        image = [image.text for image in root.iter('path')][0].split("/")[6]
        
        for xmin,ymin,xmax,ymax in zip(root.iter("xmin"),root.iter("ymin"),root.iter("xmax"),root.iter("ymax")):
            row = [image, int(xmin.text), int(ymin.text), int(xmax.text), int(ymax.text), _class, int(width), int(height)]
            row_series = pd.Series(row)
            df = df.append(row_series,ignore_index=True)
        
        # Save to .csv file 
        df.to_csv(csv_name,header=False,index=False)
        #show the data frame 
        df.head(10) 

        logging.info('[INFOR]: Convert Done!')


# =============================================================================

def main():
    xml_path = 'test.xml'
    csv_name = 'test.csv'
    write_xml_to_csv(csv_name, xml_path)

if __name__ == "__main__":
    logging.info('Task: Convert xml to csv file')

    main()

    logging.info('Process Done')