words = open("C:\\Projects\\python-advanced\\10-lab-file-handling\\words.txt")
text = open("C:\\Projects\\python-advanced\\10-lab-file-handling\\input.txt")

words_count = {}

for line in words:
    line_words = line.split(" ")
    
    for word in line_words:
        words_count[word.lower()] = 0

for line in text:
    line_words = line.split(" ")
    
    for word in line_words:
        lower_word = word.lower()
        if lower_word in words_count:
            words_count[lower_word] += 1

output = open("C:\\Projects\\python-advanced\\10-lab-file-handling\\output.txt", "x")

for (word, count) in words_count.items():
    output.write(f"{word} - {count}\n")

output.close()