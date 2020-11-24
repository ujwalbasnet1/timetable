from mi import TimeTableGenerator
from mi import Activity
from mi import ClassRoom
from mi import Group

# driver code


def run():

    classRooms = [
        ClassRoom(0),
        ClassRoom(1),
        ClassRoom(2),
        ClassRoom(3),
        ClassRoom(4),
    ]

    groups = [
        Group(
            1,
            [
                Activity(1, "G1A", 5, 7, [0, 1]),
                Activity(1, "G1B", 6, 7, [3, 5]),
                Activity(1, "G1C", 7, 9, [2, 6]),
            ],
        ),
        Group(
            2,
            [
                Activity(2, "G2A", 7, 9, [2]),
                Activity(2, "G2B", 5, 7, [3, 6]),
                Activity(2, "G2C", 6, 8, [4]),
                Activity(2, "G2D", 9, 10, [1]),
                Activity(2, "G2E", 11, 12, [5, 4]),
            ],
        ),
        Group(
            3,
            [
                Activity(3, "G3A", 6, 8, [0, 3]),
                Activity(3, "G3B", 8, 9, [5, 6]),
                Activity(3, "G3C", 10, 12, [2, 4]),
                Activity(3, "G3D", 11, 12, [1]),
            ],
        ),
        Group(
            4,
            [
                Activity(4, "G4A", 5, 6, [3]),
                Activity(4, "G4B", 6, 8, [1]),
                Activity(4, "G4C", 10, 12, [5]),
            ],
        ),
        Group(
            5,
            [
                Activity(5, "G5A", 8, 10, [6]),
                Activity(5, "G5B", 7, 8, [0]),
                Activity(5, "G5C", 9, 10, [2]),
            ],
        ),
        Group(
            6,
            [
                Activity(6, "G6A", 10, 12, [4]),
                Activity(6, "G6B", 7, 9, [5]),
                Activity(6, "G6C", 11, 12, [3]),
            ],
        ),
    ]

    t = TimeTableGenerator(classRooms, groups)

    table = []

    for i in range(0, 7):
        table.append([])

        for j, g in enumerate(classRooms):
            table[i].append([])

    for a in t.generate():
        day = a[0]
        classRoom = a[1].name
        table[day][classRoom] = a[2]

    weekDays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    for row, days in enumerate(table):
        print(weekDays[row])
        for col, classRoom in enumerate(days):
            for activity in table[row][col]:
                print("C" + str(col) + ", " + str(activity), end="\n")
        print("\n\n")

    # print(t.activitySelector())


if __name__ == '__main__':
    run()


# def test(index):
#     if index == 0:
#         return [index]
