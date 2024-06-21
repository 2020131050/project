import random

def get_random_word(word_list):
    """설정한 단어 중 랜덤으로 하나를 선택하여 출제합니다."""
    word = random.choice(word_list)
    return word

def display_current_state(word, guessed_letters):
    """현재까지 맞힌 단어의 철자 상태를 표시합니다."""
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    print('단어: ' + display)

def get_guess():
    """추측되는 철자를 입력받습니다."""
    guess = input('추측할 문자를 입력하세요: ')
    guess = guess.lower()
    return guess

def play_영단어맞추기게임(word_list):
    word_to_guess = get_random_word(word_list)
    guessed_letters = []
    attempts = 6

    print('영단어맞추기 게임을 시작합니다.')
    print('단어는 ' + str(len(word_to_guess)) + ' 글자입니다.')
    print('남은 목숨: ' + str(attempts))

    while attempts > 0:
        display_current_state(word_to_guess, guessed_letters)
        guess = get_guess()

        if guess in guessed_letters:
            print('중복된 문자입니다. 목숨이 하나 줄어듭니다.')
            attempts = attempts - 1
        elif guess in word_to_guess:
            print('맞았습니다!')
            guessed_letters.append(guess)
        else:
            print('틀렸습니다.')
            attempts = attempts - 1
            guessed_letters.append(guess)
        print('남은 목숨: ' + str(attempts))

        all_guessed = True
        for letter in word_to_guess:
            if letter not in guessed_letters:
                all_guessed = False

        if all_guessed:
            print('정답입니다!! 단어는 ' + word_to_guess + '입니다.')
            break

    if attempts == 0:
        print('You Lose. 정답은 ' + word_to_guess + '입니다.')

if __name__ == "__main__":
    my_word_list = ['yonsei', 'seoul', 'busan', 'mathematics', 'dentisty', 'iphone', 'apple', 'watch', 'game', 'university', 'girl', 'boy', 'black']
    play_영단어맞추기게임(my_word_list)
