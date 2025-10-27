from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("Enter 'q' anytime to quit.")
while True:
    answer = input("Language:")
    if answer == "q":
        break
    language_survey.store_response(answer.strip())

print("Survey results:")
language_survey.show_results()