"""
Data Processing
===============

This file is used for parse json to xml file

Reference:

"""
__author__ = 'Khoa Tran'
__email__ = 'thdkhoa1312@gmail.com'
__date__ = '2021/07/20'
__status__ = 'development'


# =============================================================================


import json
import os
import logging
from pascal_voc_io import PascalVocWriter

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s')


# =============================================================================


def parse_json_to_xml(json_file, classes):

    #read json data
    with open(json_file, 'r') as f:
        data = json.loads(f.read())
    
    folder_name = os.path.dirname(json_file)
    file_name = data['filename']
    image_size = data['image_size']
    boxes = data['box']

    #init parser
    parser = PascalVocWriter(folder_name, file_name, image_size)
    for b in boxes:
        parser.add_bnd_box(b[0], b[1], b[2], b[3], classes, 0)
    parser.save()


# =============================================================================


def main():
    parse_json_to_xml('annotaions/test.json', 'person')


# =============================================================================

if __name__ == '__main__':
    logging.info('Task: Parse json to xml')

    main()

    logging.info('Process Done')
