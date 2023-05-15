import json
import os

from guess_who import *

add_slash = os.path.join

def load_universes(input_folder):

    universes = list()
    for afolder in os.listdir(input_folder):
        if afolder.startswith("."):
            continue

        universe_folder = add_slash(input_folder, afolder)
        options_path = add_slash(universe_folder, "options.json")
        options = json.load(open(options_path, 'r'))


        universe_name = options["universe"]
        border_color = options["border_color"]
        uni = Universe(universe_name, border_color)
        universes.append(uni)

        print(f'Entering Universe "{ universe_name }"')

        for afile in os.listdir(universe_folder):
            if afile == "options.json" or afile.startswith("."):
                continue

            name = os.path.splitext(afile)[0]
            input_path = add_slash(universe_folder, afile)

            print("loading ", input_path)
            character = Character(image_path=input_path, universe=uni, name=name)
            uni.add(character)
            
    return universes  
  

def main():
    # new_size = CARD_SIZE_IN
    new_size = GUESS_WHO_SIZE_IN
    input_folder = "assets"
    output_folder = "output/images"
    
    universes = load_universes(input_folder)
    all_images = list()
    for universe in universes:
        all_images.extend(universe.generate_images(add_slash(output_folder, universe.name), new_size))

    pdf_maker = PDFMaker(US_LETTER_IN[0], US_LETTER_IN[1])
    pdf_maker.save_images(all_images, "output", new_size)

if __name__ == "__main__":
    main()


