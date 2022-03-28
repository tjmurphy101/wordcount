

def open_file(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    return lines

def main():
    file_lines = open_file("warpeace")
    word_count(file_lines)

def word_count(all_limes):
    word-counter = {}
    for line in all_lines:
        words_in_line = line.split(' ')
        for word in words_in_line:



