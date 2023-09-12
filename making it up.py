import random


def read_paragraphs(file_path, encoding='utf-8'):
	with open(file_path, 'r', encoding=encoding, errors='replace') as file: #Using utf-8 encoding because my locale is Japanese
		paragraphs = file.read().split('\n\n')
	return paragraphs

def select_random_paragraphs(paragraphs, num_paragraphs):
	return random.sample(paragraphs, num_paragraphs)

def write_paragraphs_to_file(selected_paragraphs, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
                file.write('\n\n'.join(selected_paragraphs))

source_file = 'source.txt'
destination_file = 'destination.txt'

num_random_paragraphs = 10 #Amount of random paragraphs to copy

paragraphs = read_paragraphs(source_file)

selected_paragraphs = select_random_paragraphs(paragraphs, num_random_paragraphs)

write_paragraphs_to_file(selected_paragraphs, destination_file)

print(f"{num_random_paragraphs} paragraphs have been copied to the file.")
