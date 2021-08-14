import math
from typing import List


def minSpeedOnTime(dist, hour):
    def get_travel_time(this_speed: int, dist: List[int]) -> float:
        total_time = 0
        # iterate through each dist in this_dist
        for i in range(len(dist)):
            # get the time needed for this train to reach it's destination
            this_time = dist[i] / this_speed
            # if this isn't the last train we need to wait for the next train
            if i < len(dist) - 1:
                this_time = math.ceil(this_time)
            total_time += this_time
        return total_time

    if len(dist) - 1 > hour:
        return -1

    hour_diff = 1
    if hour % 1 != 0.0:
        hour_diff = hour % 1

    min_speed = 0
    max_speed = math.ceil(1 / (hour_diff / max(dist))) + 1
    this_speed = (min_speed + max_speed) // 2

    old_this_speed = -1
    last_passed_speed = -1

    while min_speed < max_speed:
        temp = this_speed
        this_speed = (min_speed + max_speed) // 2
        if this_speed == min_speed or this_speed == max_speed:
            break
        if old_this_speed == this_speed:
            break
        else:
            old_this_speed = temp

        travel_time = get_travel_time(this_speed, dist)
        # if this time is exactly at our time limit
        # we have no extra time left and return this speed
        if travel_time == hour:
            last_passed_speed = this_speed
            break
        # if we have met the time limit and have some time to spare
        # explore lower speeds
        if travel_time < hour:
            last_passed_speed = this_speed
            # make this speed the maximum of any speeds to try in the future
            max_speed = this_speed

        # if we have not met the time limit
        elif travel_time > hour:
            # make this speed the minimum of any speeds to try in the future
            # because this speed fails, any speeds lower than it will also fail
            min_speed = this_speed

    return last_passed_speed


if __name__ == "__main__":
    res = minSpeedOnTime([1, 3, 2], 6)
    assert res == 1
    res = minSpeedOnTime([1, 3, 2], 2.7)
    assert res == 3
    res = minSpeedOnTime([1, 3, 2], 1.9)
    assert res == -1
    assert minSpeedOnTime([1, 1, 100000], 2.01) == 10000000
    assert minSpeedOnTime([2, 1, 5, 4, 4, 3, 2, 9, 2, 10], 75.12)
    print("passed all test cases")

"""
GIVEN
    must take n trains in sequential order
    given integer array dist of length n
    dist[i] describes the distance(in kilometers) of the ith train ride
    each train only departs at an integer hour
    may need to wait in between each train ride
INPUT
    float hour
        amount of time left
OUTPUT
    positive integer
        minimum positive integer speed in kilometers per hour
        that all the trains must travel at for you to reach the office on time
        or -1 if it is impossible on time
EXAMPLE
    dist = [1, 3, 2], hour = 6
    at 1 kilometers per hour
        takes 1 + 3 + 2 = 6 hours
        since we reach work on time
        return this as it is minimum positive integer speed that all the trains must travel at for me to reach the office on time

    dist = [1,3,2], hour = 2.7
    at 1, take 6 hours too slow
        increase speed
    at 2 km / h
        start first at 0 1 takes 0.5 hours, must wait till 1 hour to catch next train
        start second at 1 3km takes 1.5 hours done by 2.5 hours
        start third at 3, 2 km takes 1 hour, reach by 4 which is not within the time,
        increase speed
    at 3 km / h
        start first at 0, 1 km takes 0.33_ hourse, must wait till 1 hour to catch next train
        start second train at 1 hour, 3 km takes 1 hour, reach at 2 hours
        start train 3 at 3 hours, 2 km / 3 takes 0.666 hours, takes
        2.66 hours
        within time
        return 3

    dist = [1,3,2], hour = 1.9
        the first two trains will take 1 hour at least
        even if we take 1 minute to get from train 1 to 2 and train 2 to 3, we have to wait 59 minutes for the next bus
        return -1
BRUTE FORCE
    if len(dist) - 1  > hour:
        return -1

    this_speed = 1
    while this_speed <= max(dist) * 2:
        if reaches_on_time(this_speed, dist, hour):
            return this_speed

BINARY SEARCH?
    between min possible speed and max of dist
"""
