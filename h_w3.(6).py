# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


def int_func(word):
    latin_char = 'asdfghjklzxcvnetuir'
    return word.title() if not set(word).difference(latin_char) else False

words = input('Enter a string of space-separated words ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')


