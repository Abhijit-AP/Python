import random
import hangmanart as art
import hangmanwords as words

chosen_word = random.choice(words.word_list)
print(chosen_word)

guess_list = []
for cw in chosen_word:
    guess_list.append("-")

# print(guess_list)

# for cw in range(0,len(chosen_word)):
#    if chosen_word[cw] == guess:
#        print("Right")
#    else:
#        print("Wrong")

# Or You can also do this for forloop
#for cw in chosen_word:
#    if cw == guess:
#        print("Right")
#    else:
#        print("Wrong")

print(art.logo)

lives = 6
guessed = ""
while lives != 0:
    guess = input("Guess a letter : ").lower()

    if guess in guessed:
        print(f"You have already guessed {guess}")

    for cw in range(0,len(chosen_word)):
        if chosen_word[cw] == guess:
            guess_list[cw] = guess

    if guess in chosen_word:
        print(guess_list)
        print(art.stages[lives])
        guessed += guess

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(guess_list)
        print(art.stages[lives])

        if lives == 0:
            print("Game over!")
            exit()

    if "-" not in guess_list:
        print("You Won!")
        exit()

