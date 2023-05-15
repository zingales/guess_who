# Custom Guess Who Generator


### Requirements 
* Python
* PIL package installed for python


## How to use
1. Expected folder structure
    - assets
        -- Universe1
            --- options.json
            --- character-name.png
        -- Universe2
            --- options.json
            --- character-name.png
1. Inside `options.json` it expects a json with two keys `universe` and `border_color`. `border_color` is a valid color in PIL.
1. Run main.py passing in the input folder, output folder, and new image size in inches as a tuple. 


