def longest_word(count):
    with open(count, 'r') as infile:
        words = infile.read().split()
        max_len = len(max(words, key=len))
        return [word for word in words if len(word) == max_len] 
print(longest_word('count.txt')) 
