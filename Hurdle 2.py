def turn_right():
    turn_left()
    turn_left()
    turn_left()

def course_run():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() != True:
    course_run()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
