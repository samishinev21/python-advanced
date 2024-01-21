text = input()
letters = {}

for letter in text:
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1

sorted_letters = sorted(letters.keys())

for letter in sorted_letters:
    print(f"{letter}: {letters[letter]} time/s")