#list of question
#Store the question 
#randomly pick question
#ask the question 
#see if they are correct 
#tell the user their score 
import random

questions = {
  "what is the keyword to define a function in python?": "def",
  "which data type is used to store True or False values?": "boolean",
  "which is the correct file extension for python files?": ".py",
  "which symbol is used to comment in python?": "#",
  "what is the output of 2 ** 3 in Python?": "8",
  "which keyword is used to create a loop in Python?": "for",
  "how do you take user input in Python?": "input()",
  "which function is used to find the length of a list?": "len()",
  "what is the correct syntax to check if 'x' is equal to 10?": "x == 10",
  "what is the result of 10 // 3 in Python?": "3",
  "which module is used to work with random numbers in Python?": "random",
  "how do you declare a list in Python?": "Using square brackets []",
  "how do you open a file in Python for reading?": "open('filename', 'r')",
  "what does the 'break' keyword do in a loop?": "Exits the loop",
  "which function is used to convert a string into an integer?": "int()"
}

def python_trivia_game():
  questions_list = list(questions.keys())
  total_questions = 5
  score = 0
  
  selected_questions = random.sample(questions_list,total_questions)
  print(selected_questions)
  
  for idx, question in enumerate(selected_questions):
    print(f"{idx + 1}. {question}")
    user_answer = input("Your answer: ").lower().strip()
    correct_answer = questions[question]
    
    if user_answer == correct_answer.lower():
      print("Correct \n")
      score += 1
    else:
      print(f"Wrong . The correct answer is : {correct_answer}.\n")
    
  
  print(f"Game Over! you final score is :{score}/{total_questions} ")
    
    


python_trivia_game()