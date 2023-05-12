import sys
import os
from PIL import Image, ImageOps, ImageFont,  ImageDraw 


CM_TO_IN = 0.3937008

GUESS_WHO_SIZE_CM = (2.9, 3.4)
GUESS_WHO_SIZE_IN = (GUESS_WHO_SIZE_CM[0]* CM_TO_IN, GUESS_WHO_SIZE_CM[1] * CM_TO_IN)

A4_SIZE_IN = (8.27, 11.7)

OUTPUT_DPI = 150


class Character(object):
    original_image_path:str
    name:str
    universe:str
    sized_image_path:str

    def __init__(self, image_path, name, universe):
        self.original_image_path = image_path
        self.name = name
        self.universe = universe
        self.sized_image_path = ""


    def create_output_image(self, output_path, border_color):

        # open imge
        img = Image.open(self.original_image_path)
        new_image = shrink_image(img, GUESS_WHO_SIZE_IN)
        new_image = add_border(new_image, border_color)
        new_image = add_name(new_image, self.name)



        new_image.save(output_path, dpi=(OUTPUT_DPI,OUTPUT_DPI))
        self.sized_image_path = output_path
        return new_image
        

    def __repr__(self) -> str:
        return f"{self.universe}:{self.name}--{self.original_image_path}"

def calculate_new_image_size(original_dpi, original_size_pixels, new_size_in):
    original_size_in = (original_size_pixels[0]/original_dpi[0], original_size_pixels[1]/original_dpi[1])
    
    new_pixels_0 = int((new_size_in[0]/original_size_in[0]) * original_size_pixels[0])
    new_pixels_1 = int((new_size_in[1]/original_size_in[1]) * original_size_pixels[1])


    return (new_pixels_0, new_pixels_1)


def add_border(img, border_color):
    x,y = img.size
    
    smaller_image = img.crop(box=(10,10,x-10,y-10))
    return ImageOps.expand(smaller_image,  10, fill = border_color)


MAX_FONT_SIZE = 40
def add_name(img:Image, name:str):
    draw = ImageDraw.Draw(img)
    fontname = "Keyboard.ttf"
    # font = ImageFont.truetype(<font-file>, <font-size>)
    x,y = img.size

    fontsize=10
    font = ImageFont.truetype(fontname , fontsize)
    while font.getlength(name) < 0.9 * img.size[0] and fontsize< MAX_FONT_SIZE:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype(fontname, fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1

    _, _, w, h = draw.textbbox(xy= (0, 0), text=name, font=font)

    draw.text(((x-w)/2, y-h-10),name,fill='white', font=font,
       stroke_width=2, stroke_fill='black')
    return img


def shrink_image(img:Image, new_size_in:tuple[int, int]):
    x = int(new_size_in[0]* OUTPUT_DPI)
    y = int(new_size_in[1]*OUTPUT_DPI)
    return img.resize(size=(x,y))
