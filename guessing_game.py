import random


    def get_guess():
      while True:
        try:
          user_guess = int(input('Please enter your guess (1-10) >>> '))
        except ValueError:
          print('Input has to be an integer!')
          continue
        else:
          if user_guess not in range(1,11):
            print('Input has to be in range 1-10!')
            continue
        break

      return user_guess


def start_game(highscore=0):
    print('Welcome to the number guessing game!' + ((' The HIGHSCORE is %s!' % highscore) if highscore != 0 else ''))
    answer = random.randint(1,10)
    attempts = 0

    while True:
      guess = get_guess()
      attempts += 1

      if guess < answer:
        print('It\'s higher!')
      elif guess > answer:
        print('It\'s lower!')
      else:
        print('Correct! It took you %s %s!' % (attempts, 'attempts' if (attempts-1) else 'attempt'))
        if (highscore == 0 or attempts < highscore):
          highscore = attempts
          print('New HIGHSCORE!')
        break

    if input('Would you like to play again? Input "y" to play again. Any other input will end the game. >>> ').lower() == 'y':
      start_game(highscore=highscore)
    else:
      print('Thanks for playing!')


start_game()