# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
filehandle = open('questions.txt.',"w")

multiplechoice1 = input("Input multiple choice\n")
answer1 = input('input answer for question 1\n')
answer2 = input('input answer for question 2\n')
answer3 = input('input answer for question 3\n')
answer4 = input('input answer for question 4 \n')
num = input("Input the right answer \n")

filehandle.write(multiplechoice1 + "\n")
filehandle.write(answer1 + "\n")
filehandle.write(answer2 + "\n")
filehandle.write(answer3 + "\n")
filehandle.write(answer4 + "\n")
filehandle.write(num)

filehandle.close()