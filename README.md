# Simple_calculator
REQUIREMENT(S): must run with a code compiler.
DESCRIPTION:
A simple calculator capable of doing basic math, you can use parenthesis '(' and ')', exponential '^', multiplication '*', division '/', addition '+' and abstraction '-'.
But it can't calculate your heart <3 JK -,- 
You also wont have to worry about precedence because this code use Python built-in function, the 'eval()' which basically does all the calculation of the input ><. 
I also implemented a loop to loop through your input and rewrite it in a neater way XD, so that you can easily read and access your history >_>.
Example: 
Terminal:
This is a simple calculator that would calculate your input just for you,
Please note that: for exponential "**", we replaced it with "^" instead  
Enter your equation or type History to check history: (2^3 +2  ) -10
(2 ^ 3 + 2) - 10 = 0
Enter your equation or type History to check history: history
(2 ^ 3 + 2) - 10 = 0

You can clear history by entering "Clear" 
Enter your equation or type History to check history: 

SIDE NOTES:
- I haven't added exception so ZeroDivisionError: division by zero, SyntaxError: '(' was never closed and other error will not work. Sorry, for not adding exception :PP
- You won't need to rerun the code because I used recursion ;), it will only be stopped if your pc died, or you close the terminal, or you caused the error mentioned above :PP
- The data is stored in 'History.txt' file, why not Postgresql or MongoDB? because text file is the easiest out of them all :P, it's not like I'm required to use them :T
