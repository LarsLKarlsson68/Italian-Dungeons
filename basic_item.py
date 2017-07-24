import questions
import random

class BasicItem:
    multiple_choice=False
    tries = 1
    questions=[]
    failed_questions = None

    def __init__(self):
        self.failed_questions = []
        
    def challenge(self,player,gui,tries=1):
        if not self.questions:
            return 1
#        print('Failed questions:', len(self.failed_questions))
        if random.randint(1,6) > len(self.failed_questions):
#            print('New question')
            outcome, question = questions.phrase_question(self.questions,gui,self.multiple_choice,tries)
        else:
#            print('Retrying failed question')
            question = self.failed_questions.pop(0)
            if question in player.failed_questions and len(player.failed_questions) >= 3:
                player.failed_questions.remove(question)
            outcome, question2 = question[0](*question[1]+(gui,))
#        print('outcome=', outcome, question)
        if not outcome and question:
#            print('Adding failed question')
            self.failed_questions.append(question)
            player.failed_questions.append(question)
        return outcome
