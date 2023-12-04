from Question_List import questions_and_answers
from Question import question
from Question_Master import QuestionMaster

question_bank = []

for Qnd in questions_and_answers:
    qn = Qnd["question"]
    ans = Qnd["answer"]
    question_bank.append(question(qn,ans))
question_master = QuestionMaster(q_list=question_bank)
question_master.start_quiz()

