def history():
    with open('History.txt', 'r') as f:
        print(f.read())

def clear_history():
    with open('History.txt', 'w') as f:
        f.write('')

print('''This is a simple calculator that would calculate your input just for you,
Please note that: for exponential \"**\", we replaced it with \"^\" instead''')

def calculator(user_input):
    
    if user_input not in ["History", 'history', 'check history', "Clear history", "clear history", "clear", "Clear"]:
        
        user_input = user_input.replace(" ", "")

        temp = ''
        e = False

        for i in user_input:
            if i in ['^']:
                e = True
                user_input_temp = user_input.replace("^", "**")
                result = eval(user_input_temp)
            elif e == False:
                result = eval(user_input)

        for j in range(len(user_input)):
            if user_input[j] in ['(', ')']:
                temp += user_input[j]
            elif user_input[j] in ['+', '-', '^', '/', '*']:
                temp += " " + user_input[j] + " " 
            if user_input[j].isdigit():
                temp += user_input[j]
        #Wonder why I could've used replace instead for the above code? Well the thing is that
        #it keep doubling the amount of space I put -,- So I choose to go with this one

        user_input = temp

        print(user_input, "=", result)

        def save_history(user_input, result):
            with open('History.txt', 'a') as f:
                f.write(f'{user_input} = {result}\n')

        save_history(user_input, result)

    elif user_input in ["History", 'history', 'check history']:
        history()
        print("You can clear history by entering \"Clear\" ")
    
    elif user_input in ["Clear history", "clear history", "clear", "Clear"]:
        clear_history()
        print("History cleared")
    
    else:
        print("You did not enter the input correctly")
    
    user_input = input('Enter your equation or type History to check history: ')
    calculator(user_input)

user_input = input('Enter your equation or type History to check history: ')

calculator(user_input)
