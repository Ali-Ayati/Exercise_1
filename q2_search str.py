def counter_world(txt: str, word: str) -> int:
    return txt.count(word)

txt = input("Enter a text: ")
word = input("Enter a word to search for: ")

print(counter_world(txt, word))
