import random

words = ['hello', 'friend', 'world']


def get_word(words):
    random_index = random.randint(0, len(words) - 1)
    return words[random_index]


def guess_letter(word, current_word, letter):
    if len(letter) > 1 or ord(letter) < ord('a') or ord(letter) > ord('z'):
        raise ValueError(f'{letter} is not a letter')
    hit = False
    for i in range(len(word)):
        if word[i] == letter and current_word[i] == '*':
            hit = True
            current_word[i] = word[i]
    return hit


def main():
    word = list(get_word(words))
    current_word = list('*' * len(word))
    mistakes = 0
    win = False

    while mistakes < 5:
        letter = input('Guess a letter:\n')
        if guess_letter(word, current_word, letter):
            print('Hit!')
        else:
            mistakes += 1
            print(f'Missed, mistake {mistakes} out of 5.')
        print(f'\nThe word: {"".join(current_word)}\n')
        if current_word == word:
            win = True
            break

    if win:
        print('You won!')
    else:
        print('You lost!')


if __name__ == "__main__":
    main()
