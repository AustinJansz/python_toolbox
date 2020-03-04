 #!/usr/bin/python3
# Basic packages to get the scirpt up and running
import clipboard, random, string, sys

def main(argv):
	# Get some system randomness
	randomness = random.SystemRandom()
	# Set a random length between 10 and 15
	# Planned enhancement: allow this to be set manually in the function call                                           
	length = random.randint(10, 20)
	# Define the character space for the password
	# ASCII letters, digits, punctuation, and space
	char_space = string.ascii_letters + string.digits + string.punctuation + ' '
	# Generate the password
	password = str().join(randomness.choice(char_space) for _ in range(length))
	# Copy the password to the clipboard
	clipboard.copy(password)

	# Confirm with the user
	print("Your password has been copied to the clipboard!")
	# Check if the user would like to see the password
	print_pass = input("Would you like to see your password? [y|n]: ")
	if print_pass == "y" or print_pass == "yes":
		print(password)

if __name__ == "__main__":
   main(sys.argv[1:])