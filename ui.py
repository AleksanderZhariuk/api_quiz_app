from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1, sticky='e')

        self.question_canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.question_canvas.create_text(150, 125, text="Some Question text", fill=THEME_COLOR,
                                                              font=('Arial', 20, 'italic'), width=280)
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.get_next_question()

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.click_true_button)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.click_false_button)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.configure(bg='White')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def click_true_button(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def click_false_button(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.configure(bg='Green')
        else:
            self.question_canvas.configure(bg='Red')
        self.window.after(1000, self.get_next_question)
