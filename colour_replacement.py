#!/usr/bin/python3
# Basic packages to get the scirpt up and running
from PIL import Image

def main(argv):
	# Have the user enter the image path
	src_loc = input("Path of the image: ")
	img = Image.open(src_loc)

	# Get the image data as well as its dimensions
	img_data = list(img.getdata())
	img_width, img_height = img.size

	# Tuple aquisition with the colour they want to replace and the replacement colour
	source_colour = tuple(int(x.strip()) for x in input("Source colour [R,G,B,A]: ").split(','))
	ideal_colour = tuple(int(x.strip()) for x in input("Ideal colour [R,G,B,A]: ").split(','))

	# Iterate through the image and replace the pixels
	i = 0
	while i < len(img_data):
		if img_data[i] == source_colour:
			img_data[i] = ideal_colour
		i += 1

	# Generate the new image container with the original width height
	new_img = Image.new('RGBA', (img_width,img_height))
	# Set in the altered data
	new_img.putdata(img_data)
	# Check to see if the user wants to confirm the image change
	user_confirm = input("Would you like to confirm the image? [y|n]: ")
	if user_confirm == "y":
		new_img.show()
	# Ask for the save location
	save_loc = input("Path of the new image: ")
	if save_loc == "":
		save_loc = src_loc
	new_img.save(save_loc)

if __name__ == "__main__":
   main(sys.argv[1:])