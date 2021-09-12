# ***************************** Palindrom Number *********************************

def play_quit():
    play_game = input("\n\nEnter any key to continue or \"Q\" to quit...!")
    if play_game.capitalize() == "Q":
        print(
            "Thanks for your valuable time that you spend with us....! We expect, you will be back soon...! Take care and stay home...!")
        exit()
    else:
        print("Enjoy the programme...!\n")

# Checking the number is palindrome or not
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# If n is not palindrom it will increase the n by 1
def next_palindrome(n):
    while not is_palindrome(n):
        n += 1
    return n

if __name__ == '__main__':
    while True:
    
        try:
            raw_input = int(input("Enter the turns of number:\n"))
            list = []
            for item in range(raw_input):
                palin = int(input("Enter the element:"))
                list.append(palin)
    
        except Exception as e:
            print("Invalid input occurs...! Please try again...! The Error is:",e)
            exit()
    
        for item in range(len(list)):
            print(f"The next palindrome of {list[item]} is {next_palindrome(list[item])}")
    
        play_quit()
        continue
