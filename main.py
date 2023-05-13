import json
import os

from guess_who import *

add_slash = os.path.join


def process_images(input_folder, output_folder):
    all_characters = dict()

    all_images = list()
    for afolder in os.listdir(input_folder):
        if afolder.startswith("."):
            continue

        universe_folder = add_slash(input_folder, afolder)
        ouput_universe_folder = add_slash(output_folder, afolder)
        os.makedirs(ouput_universe_folder, exist_ok=True)
        options_path = add_slash(universe_folder, "options.json")
        options = json.load(open(options_path, 'r'))

        characters = list()
        universe = options["universe"]
        border_color = options["border_color"]
        print(f'Entering Universe "{ universe }"')

        for afile in os.listdir(universe_folder):
            if afile == "options.json" or afile.startswith("."):
                continue

            name = os.path.splitext(afile)[0]
            input_path = add_slash(universe_folder, afile)
            
            print("working on ", input_path)
            character = Character(image_path=input_path, universe=universe, name=name)
            output_path = add_slash(ouput_universe_folder, os.path.splitext(afile)[0]+".png")
            new_image = character.create_output_image(output_path, border_color=border_color)
            all_images.append(new_image)
            characters.append(character)
        all_characters[universe] = characters

    return all_images, all_characters
            

def main():
    input_folder = "assets"
    output_folder = "output"
    images, characters = process_images(input_folder, output_folder)

    pdf_maker = PDFMaker(US_LETTER_IN[0], US_LETTER_IN[1])
    pdf_maker.save_images(images, "output")

if __name__ == "__main__":
    main()


