import xml.etree.ElementTree as ET
import os
import pandas as pd


# Create dataframe 
df = pd.DataFrame()
df


# Load xml file and add data to .csv file 
xml_path = r""
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
df.to_csv("train_8_1_2020_huy.csv",header=False,index=False)
# df.head(10) 