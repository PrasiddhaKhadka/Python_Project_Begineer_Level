import random

dict={
  "fruit": ["apple", "banana", "cherry", "orange", "grape", "kiwi"],
  "color": ["red", "green", "blue", "yellow", "purple", "black"],
  "animal": ["cat", "dog", "mouse", "elephant", "tiger", "panda"],
  "number": ["one", "two", "three", "four", "five", "six"],
  "footballer": ["Messi", "Ronaldo", "Neymar", "Mbappe", "Zidane", "Pele"]
}

value = random.choice(list(dict.values()))
finalValue = random.choice(list(value))
    
tries_remaining = 7

current_tries = 0    

def word_guessing_game():
    global current_tries
    print("Welcome to the Word Guessing Game!")
    print("You have total 7 tries")
    
    while current_tries < tries_remaining:
        current_tries += 1
        my_guess = input(f"Enter your word: {current_tries} Attempts ")
        
        if(my_guess == finalValue):
            print("You are correct")
            return
        elif(my_guess != finalValue):
           
            if(dict['animal'].__contains__(finalValue)):
            
                print("Hint: The word is from animal category \n")
            elif(dict['color'].__contains__(finalValue)):
                print("Hint: The word is from color category \n")
            elif(dict['fruit'].__contains__(finalValue)):
                print("Hint: The word is from fruit category \n") 
            elif(dict['number'].__contains__(finalValue)):
                print("Hint: The word is from number category \n")    
            elif(dict['footballer'].__contains__(finalValue)):
                print("Hint: The word is from footballer category \n")
            else:
                print("Word doesnot match our dataset \n")
                return
        else:
            print("Something went wrong")
    

word_guessing_game()