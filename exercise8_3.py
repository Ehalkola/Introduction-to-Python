import PIL
from PIL import Image, ImageDraw, ImageFont, ImageColor

# Create a list for colours to be added after user input
image_colours = []

# Create loop to ask and get colours from PIL.ImageColor.colormap._getitem__() based on user input, add colours into the
# list above
for x in range(4):
    while True:
        try:
            user_input = input("Input a colours for, background, text, triangle and circle in picture: ")
            colors = PIL.ImageColor.colormap.__getitem__(user_input)
            image_colours.append("".join(colors))
            break
        except KeyError:
            print("Colour input can't be found in list, please try again and use lower capital letters")

# Create a background for the image, draw the imag e
width, height = 500, 300
background_colour = image_colours[0]
image = Image.new("RGB", (width, height), f"{background_colour}")
draw = ImageDraw.Draw(image)

# Ask the user for some text
user_text = input("Input some text here: ")

# Load the Arial font from your file directory
font_path = r"C:\Users\Archoste\Downloads\arial.ttf"
try:
    font = ImageFont.truetype(font_path, size=16)
except IOError:
    print("Error: Unable to load the font file.")
    font = ImageFont.load_default()

# Create a position for users input text, define the colour of the text based on user input, draw text into the picture
text_position = (75, 250)
text_colour = image_colours[1]
draw.text(text_position, user_text, fill=text_colour, font=font)

# Create points for the triangle, define the colour of triangle based on user input and draw the triangle into the
# picture
triangle_points = [(250, 110), (290, 190), (210, 190), (250, 110)]
triangle_color = image_colours[2]
draw.polygon(triangle_points, fill=triangle_color)

# Create circle radius, center, define colour of circle based on user input, draw the circle into the picture
circle_radius = 16
circle_center = (250, 150)
circle_color = image_colours[3]
draw.ellipse((235, 135, 265, 165), fill=circle_color)

# Save the image
image.save("output_picture.png")

# Show the image to the user
image.show()
