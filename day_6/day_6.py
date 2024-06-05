# The following code will only work on the website: https://reeborg.ca

# # Hurdle 1 and 2
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# while not at_goal():
#     jump()

# # Hurdle 3
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         jump()

# # Hurdle 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     while not right_is_clear():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
#
# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         jump()

# # Maze
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while front_is_clear() and not at_goal():
#     move()
#     if wall_in_front() and right_is_clear():
#         turn_left()
#
# while not at_goal():
#     if front_is_clear() and wall_on_right():
#         move()
#     elif right_is_clear():
#         turn_right()
#         move()
#     else:
#         turn_left()
