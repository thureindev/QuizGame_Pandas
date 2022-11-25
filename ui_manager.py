import turtle

FONT = ('Sans-Serif', 8, 'bold')
FONT_COLOR = '#2277FF'

SCORE_FONT_COLOR = '#BBBBBB'

STATUS_FONT = ('Sans-Serif', 16, 'bold')
INFO_STATUS_COLOR = "#33BBCC"
CORRECT_STATUS_COLOR = '#22CCFF'
INCORRECT_STATUS_COLOR = '#FF3333'


class UIManager():
    def __init__(self):
        self.in_game_text = turtle.Turtle()
        self.in_game_text.hideturtle()
        self.in_game_text.penup()
        self.in_game_text.color(FONT_COLOR)

        self.status_text = turtle.Turtle()
        self.status_text.hideturtle()
        self.status_text.penup()
        self.status_text.setpos(0, 250)

        self.score_text = turtle.Turtle()
        self.score_text.hideturtle()
        self.score_text.penup()
        self.score_text.color(SCORE_FONT_COLOR)
        self.score_text.setpos(-325, 250)

    def write_on_map(self, text="answer", x=0, y=0):

        # fastest speed to eliminate time in turtle-travel-animation
        self.in_game_text.speed("fastest")
        # goto position on map image
        self.in_game_text.setpos(x, y)

        # move=True to show animation # slowest speed to make animation seen
        self.in_game_text.speed("slowest")
        self.in_game_text.showturtle()
        self.in_game_text.write(text, move=True, align='center', font=FONT)
        self.in_game_text.hideturtle()

    def display_score(self, scored=0, max_score=0):
        # clear to prevent text overlap
        self.score_text.clear()
        self.score_text.write(f"{scored}/{max_score}", move=False, align='left', font=STATUS_FONT)

    def display_answer_status(self, text="game status", status="correct"):
        # clear to prevent text overlap
        self.status_text.clear()

        # for default
        font_color = INFO_STATUS_COLOR
        # for correct and incorrect
        if status == "correct":
            font_color = CORRECT_STATUS_COLOR
        elif status == "incorrect":
            font_color = INCORRECT_STATUS_COLOR

        # set color
        self.status_text.color(font_color)

        self.status_text.write(text, move=False, align='center', font=STATUS_FONT)
