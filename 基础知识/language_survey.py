from survey import AnonymousSurvey

question = "what language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_questions()
print("enter 'q' to quit,\n")

while True:
    response=input("language: ")
    if response=='q':
        break;
    my_survey.store_response(response)

print("thank you !")
my_survey.show_results()
