def main():
	number_of_words = 0
	with open("books/frankenstein.txt") as f:
		file_contents = f.read() 
		lines  =  file_contents.split()
		number_of_words += len(lines)
		lowered = file_contents.lower()
		letter_count =  {c: lowered.count(c) for c in set(lowered) if c.isalpha()}
	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{number_of_words} words found in the document", end='\n\n')
	for key in  sorted(letter_count.keys()):
		print("The " + "%s character was found %s times "  %  (key, letter_count[key]))
	print("--- End Report ---")


main()
