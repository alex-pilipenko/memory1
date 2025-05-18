from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
from random import shuffle, randint

class Question():
    
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):

        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
question_list.append(Question('Какой национальности не существует?', 'Энцы', 'Чулымцы', 'Смурфы', 'Алеуты' ))
question_list.append(Question('Какова цвета нет на флаге России', 'зеленый', 'белый', 'красный', 'синий'))
app = QApplication([])

wind = QWidget()
wind.setWindowTitle('Memo Card')

label_vopros = QLabel('Самый сложный вопрос в мире!')

push_otwet = QPushButton('Ответить')

group1 = QGroupBox('Варианты ответов')

radio1 = QRadioButton('Энцы')
radio2 = QRadioButton('Чулымцы')
radio3 = QRadioButton('Смурфы')
radio4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(radio1)
RadioGroup.addButton(radio2)
RadioGroup.addButton(radio3)
RadioGroup.addButton(radio4)

QHB = QHBoxLayout()
QVB1 = QVBoxLayout()
QVB2 = QVBoxLayout()
QVB1.addWidget(radio1)
QVB1.addWidget(radio2)
QVB2.addWidget(radio3)
QVB2.addWidget(radio4)

QHB.addLayout(QVB1)
QHB.addLayout(QVB2)

group1.setLayout(QHB)

group2 = QGroupBox('Результат теста')

lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
group2.setLayout(layout_res)

layout_line1= QHBoxLayout()
layout_line2= QHBoxLayout()
layout_line3= QHBoxLayout()

layout_line1.addWidget(label_vopros, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(group1)
layout_line2.addWidget(group2)
group2.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(push_otwet, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
def show_result():
    group1.hide()
    group2.show()

    push_otwet.setText('Следущий вопрос')

def show_question():

    group1.show()
    group2.hide()
    push_otwet.setText('Ответить')
    RadioGroup.setExclusive(False)
    radio1.setChecked(False)
    radio2.setChecked(False)
    radio3.setChecked(False)
    radio4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [radio1, radio2, radio3, radio4]

def ask(q: Question):
    
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    label_vopros.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):

    lb_Result.setText(res)
    show_result()

def check_answer():

    if answers[0].isChecked():
        show_correct('Правильно!')
        wind.score += 1
        print('Статистика\n-Всего вопросов: ' , wind.total, '\n-Правильных ответов: ', wind.score)
        print('Рейтинг: ', (wind.score/wind.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (wind.score/wind.total*100), '%')

def next_question():

    wind.total += 1
    print('Статистика\n-Всего вопросов: ' , wind.total, '\n-Правильных ответов: ', wind.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_OK():

    if push_otwet.text() == 'Ответить':
        check_answer()
    else:
        next_question()



wind.setLayout(layout_card)
wind.setWindowTitle('Memory Card')


wind.cur_question = -1 
push_otwet.clicked.connect(click_OK)
wind.score = 0
wind.total = 0
next_question()
wind.resize(400, 300)
wind.show()

app.exec()

