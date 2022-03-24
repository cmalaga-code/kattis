def search(word):
    word_list = list(word)
    start_index = word_list.index("a")
    return word[start_index:]

string_data = input()
solution = search(string_data)
print(solution)