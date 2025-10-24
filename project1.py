#list of questions
#store the answers
#randomly pick questions
#ask the questions
#check if those correct
#keep track of the score
#tell the user their score

import random

questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}

# random_question = random.choice(list(questions.items()))

# def ask_user_random_question():
#   total_count = 0
#   user_answer =  input(f"{random_question[0]}")
#   total_count +=1
#   return user_answer
  


# def check_ans_is_correct(user_answer):
#   correct_answers_count=0
#   if user_answer == random_question[1]:
#         correct_answers_count += 1
#         print("Total Questions Count", correct_answers_count)
#         print("Correct Answers Count", correct_answers_count)
#         print(random_question[1], "is correct answer" )
#   else:
#      print("Wrong Answer")

# user_guess = ask_user_random_question()
# check_ans_is_correct(user_guess)


def trivia_game():
  questions_list= list(questions.keys())
  total_questions= 5
  score= 0

  selected_questions= random.sample(questions_list, total_questions)
  # print(selected_questions)

  for index, question in enumerate(selected_questions):
    print(f"{index + 1}. {question}")

    user_answer= input("Your answer: ").lower().strip()
    correct_answer = questions[question]

    if user_answer == correct_answer.lower():
      print("Correct!\n")
      score += 1
    else:
      print(f"Wrong. The Correct answer is {correct_answer}.\n")

  print(f"Game over! Your final score is {score}/{total_questions}")


trivia_game()