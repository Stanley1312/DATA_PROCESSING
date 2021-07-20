"""
Data Processing
===============

This file is used for create a dummy json file containing box information

Reference:

"""
__author__ = 'Khoa Tran'
__email__ = 'thdkhoa1312@gmail.com'
__date__ = '2021/07/13'
__status__ = 'development'


# =============================================================================


import json
import os
import logging

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s')


# =============================================================================

def create_dummy_json():
    """
    JSON format:
    {
        'filename' : 'test1.jpg'
        'image_size' : 640, 480
        'box': [']
    }
    """
    pass

    anno = dict()
    anno['filename'] = 'test1.jpg'
    anno['image_size'] = (640,480,3)
    anno['box'] = [[10, 20, 40, 60], [300, 250, 400, 320]]

    anno_json = json.dumps(anno, indent= 4)
    
    os.makedirs('annotaions', exist_ok=True)
    with open('annotaions/test.json', "w") as f:
        f.write(anno_json)
    
    logging.info('[INFOR]: Convert Done!')


# =============================================================================


def main():
    create_dummy_json()


# =============================================================================

if __name__ == '__main__':
    logging.info('Task: Create dummy box json')

    main()

    logging.info('Process Done')

