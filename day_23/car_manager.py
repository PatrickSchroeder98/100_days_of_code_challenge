import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "blue", "green", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates a car with random y position."""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            y = random.randint(-250, 250)
            car.goto(300, y)
            self.all_cars.append(car)

    def move_cars(self):
        """Method that moves all of the cars."""
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.speed += MOVE_INCREMENT
