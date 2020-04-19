# Import libraries 
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 

def showClass(filename):
    pages = convert_from_path(filename, 500)
    Class = 'null'
    for page in pages:
        # page = pages[0]
        temp_file = './temp/temp_page.jpg'
        page.save(temp_file, 'JPEG')
        text = str(((pytesseract.image_to_string(Image.open(temp_file)))))
        # print(text)
        filter_list = ['2015', '2016', '2017', '2018', '2019', '2020']
        flag = 0
        for filter_sub in filter_list:
            if filter_sub in text:
                flag = 1
                Class = filter_sub
                break
        if flag == 1:
            break
    return Class
        
    
