Hirst Spot Painting with Python Turtle
This project recreates Damien Hirst's famous spot paintings using Python's Turtle module. Every time the script is run, a 10x10 grid of random colored spots is generated, mimicking the artist's iconic style. The colors used in this recreation are extracted from an original Hirst painting using the colorgram module.

How it Works
The project utilizes the Turtle module to draw colored dots on the screen.
Colors for the spots were extracted from the original painting using the colorgram module and stored in a list.
Each dot is randomly assigned a color from the pre-extracted palette, ensuring a unique composition every time the script is run.
The grid is 10x10 with each dot being 20 units in diameter and spaced 50 units apart.
Requirements
Python 3.x
Turtle module (included in standard Python library)
colorgram module (for color extraction, though not necessary to run the provided code)
How to Run
Clone the repository:
git clone https://github.com/MorielMauni/PictuerMaker
Run the Python script:
python hirst_spot_painting.py
Customization
The colors can be modified by updating the color_list.
Adjust the grid size by changing num_dots and adjusting the loop logic.
