number_of_halls = int(input())
capacity = int(input())
number_of_viewers = int(input())

is_able_to_hold_viewers = (number_of_halls * capacity) >= number_of_viewers
print(is_able_to_hold_viewers)
