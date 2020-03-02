# Basic packages to get the scirpt up and running
import pyqrcode, sys, getopt

def main(argv):
	# Initialize varibles
	data = ''
	output = ''
	
	# Attempt to get arguments from the command line
	try:
		opts, args = getopt.getopt(argv,"hd:o:",["data=","output="])
	# Error message in the event that the options could not be retrieved
	except getopt.GetoptError:
		print('python3 qr_generate.py --data <data> --output <output_file (sans ext)>')
		sys.exit(2)

	# Loop through the option entries
	for opt, arg in opts:
		# Help option to see how to operate the scrip
		if opt == '-h':
	 		print('python3 qr_generate.py --data <data> --output <output_file (sans ext)>')
	 		sys.exit()
	 	# Check to see if the current option is data
		elif opt in ("-d","--data"):
			data = arg
		# Check to see if the current option is output, add '.png' to file name
		elif opt in ("-o","--output"):
	 		output = arg + '.png'
	
	# Set the data of the qr code and generate a file
	# Current settings:
	# 100% black foreground
	# 100% transparent background
	data_qr = pyqrcode.create(data)
	data_qr.png(output, scale=6, module_color=(0xff, 0xff, 0xff, 0xff), background=(0x00,0x00,0x00,0x00))

if __name__ == "__main__":
   main(sys.argv[1:])