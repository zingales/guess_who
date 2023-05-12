from guess_who import *
import json


add_slash = os.path.join


def main():
    input_folder = "assets"
    output_folder = "output"

    all_characters = dict()
    # for folder in folders 
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
            character.create_output_image(output_path, border_color=border_color)
            characters.append(character)
        all_characters[universe] = characters
            


if __name__ == "__main__":
    main()


