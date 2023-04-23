import time

# def time_convert(sec):
#     mins = sec // 60
#     sec = sec % 60
#     hours = mins // 60
#     mins = mins % 60
#     print("Your time = {0}:{1}:{2}".format(int(hours), int(mins), sec))

# def my_tconv(msec):


# input("Press Enter to start")
# start_time = time.time()
# input("Press Enter to stop")
# end_time = time.time()
# time_total = end_time - start_time
# time_lapsed = round((end_time - start_time), 0)
# # time_convert(time_lapsed)
# print(time_lapsed)


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


chuj = Gym("kurwa", 12)
print(Gym.burnedCalories(chuj.calories_per_min, 4))
