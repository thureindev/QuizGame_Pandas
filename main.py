import turtle
import pandas
from ui_manager import UIManager

""" Prepare Screen """
screen = turtle.Screen()
screen.title("Guess the states in USA")
usa_map = "blank_states_img.gif"
screen.addshape(usa_map)
turtle.shape(usa_map)

# manager to write on screen # without conflicting with screen object
ui_manager = UIManager()

""" GET correct answers to check against user's answer """
#   # get dataframe including answers and coordinates to pin on screen
answer_data = pandas.read_csv("50_states.csv")
# print(answer_data)

#   # get all rows of first column as answer keys # and cast resulting obj to list
correct_answers = answer_data[answer_data.columns[0]].tolist()
# print(correct_answers)
# following code does the exact same thing using iloc property. I'll just leave it here
# correct_answers = answer_data.iloc[:, 0].tolist()

#   #   # lower all str in list to optimize answer check
def to_lower(c):
    return c.lower()
correct_answers = list(map(to_lower, correct_answers))
# print(correct_answers)

# In order to identify the answers that user have already scored
scored_answers = []

MAX_SCORE = len(correct_answers)
player_scored = 0


def game():
    """ ++++++ GAMEPLAY LOGIC START ++++++ """

    # just a stupid re-declaration for global var
    global player_scored

    # update ui scoreboard
    ui_manager.display_score(player_scored, MAX_SCORE)

    # get answer from user input
    user_answer = turtle.textinput("50 States in USA", "Guess another state")
    #   # when turtle prompted <cancel> button is clicked, it returns <None>
    #   # therefore the while loop checks that condition
    while user_answer is not None:

        # lower() to optimize answer check
        user_answer = user_answer.strip().lower()

        # if user answered correctly
        if user_answer in correct_answers:

            # if user answered already scored answer
            if user_answer in scored_answers:
                print(f"You already got {user_answer} correct.")
                ui_manager.display_answer_status(text=f"You already got {user_answer.upper()} correct.", status="neutral")

            # valid answer # user scored new correct answer
            else:
                print(f"{user_answer} is correct!")

                # ++++++ visual update on image ++++++

                #   #   #   faster way using index of dataframe for quicker access
                # by getting index in list we can access row index in panda dataframe
                index = correct_answers.index(user_answer)

                # get answer in original format in dataframe
                ans = answer_data.iloc[index, 0]
                # get coordinate data
                ans_pos_x = answer_data.iloc[index, 1]
                ans_pos_y = answer_data.iloc[index, 2]

                #   #   #   alternative way using data.column[0] == match_value
                #   #   # row = answer_data[answer_data.columns[0] == user_answer]

                ui_manager.write_on_map(ans, ans_pos_x, ans_pos_y)
                ui_manager.display_answer_status(text=f"{ans}: You got it right!", status="correct")
                # ++++++        ++++++          ++++++

                # Score a point
                player_scored += 1
                ui_manager.display_score(player_scored, MAX_SCORE)

                # update scored answers to prevent score cheat
                scored_answers.append(user_answer)

                # check if all answers are correct
                if player_scored == MAX_SCORE:
                    print("You Won!!")
                    ui_manager.display_answer_status(text=f"Congratulations! You Won!", status="correct")

                    # disable answer prompt action
                    turtle.onscreenclick(dummy_mouse_click)
                    # break while loop to prevent re-prompt for answer
                    break

        # answer is incorrect
        else:
            print(f"{user_answer}: incorrect answer")
            ui_manager.display_answer_status(text=f"{user_answer}: incorrect answer", status="incorrect")

        #   #   # re-prompt user answer to carry on the loop
        user_answer = turtle.textinput("50 States in USA", "Guess another state")


def dummy_mouse_click(x, y):
    print("I am dummy")


def get_coordinates(x, y):
    print(x, y)
    game()


if __name__ == '__main__':
    game()
    turtle.onscreenclick(get_coordinates)
    turtle.mainloop()
