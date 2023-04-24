class Player:
    backpack = []
    time_score = 0

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def __str__(self):
        return f"My name is {self.name}. Let's play!"

    def show_backpack(self):
        print(f"\nHere are your items in backpack: {Player.backpack}\n")


class Cat:
    sound = "Miauuuuu!!!"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Now I can tell you my name: I am {self.name} and I can meow: {self.sound}. Thank you for feeding me!!!"


class Room:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is {self.name}"


class LivingRoom(Room):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return super().__str__() + f"Here you can start the game."


class Bathroom(Room):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return (
            super().__str__()
            + f"I'm not sure if you can find here a safe, but you can clean up here..."
        )


class Basement(Room):
    safe = True

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return super().__str__() + f"Here you can find everything. Safe too!"


class Gym:
    calories_per_min = 0

    def __init__(self, name):
        self.name = name
        if self.name == "squats":
            self.calories_per_min = 7
        elif self.name == "push_ups":
            self.calories_per_min = 12

        # self.calories_per_min = calories_per_min

    def burnedCalories(calories_per_min, exercise_time):
        return float(calories_per_min * exercise_time)
