from mi import TimeTableGenerator
from mi import Activity
from mi import ClassRoom
from mi import Group

# driver code


def run():

    classRooms = [
        ClassRoom("C1"),
        ClassRoom("C2"),
        ClassRoom("C3"),
        ClassRoom("C4"),
        ClassRoom("C5"),
    ]

    groups = [
        Group(
            1,
            [
                Activity(1, "G1A", 5, 7, [0, 1]),
                Activity(1, "G1B", 6, 7, [1, 3, 5]),
                Activity(1, "G1C", 7, 9, [2, 5, 6]),
            ],
        ),
        Group(
            2,
            [
                Activity(2, "G2A", 7, 9, [1, 2, 4]),
                Activity(2, "G2B", 5, 7, [3, 5, 6]),
                Activity(2, "G2C", 6, 8, [2, 3, 4]),
                Activity(2, "G2D", 9, 10, [1, 4, 3, 4]),
                Activity(2, "G2E", 11, 12, [2, 3, 4]),
            ],
        ),
        Group(
            3,
            [
                Activity(3, "G3A", 6, 8, [0, 1, 2, 3]),
                Activity(3, "G3B", 8, 9, [3, 5, 6]),
                Activity(3, "G3C", 10, 12, [2, 4, 5]),
                Activity(3, "G3D", 11, 12, [1, 3, 4, 5]),
            ],
        ),
        # Group(
        #     4,
        #     [
        #         Activity(4, "G4A", 1),
        #         Activity(4, "G4B", 1),
        #         Activity(4, "G4C", 1),
        #     ],
        # ),
        # Group(
        #     5,
        #     [
        #         Activity(5, "G5A", 1),
        #         Activity(5, "G5B", 2),
        #         Activity(5, "G5C", 1),
        #     ],
        # ),
        # Group(
        #     6,
        #     [
        #         Activity(6, "G6A", 2),
        #         Activity(6, "G6B", 1),
        #         Activity(6, "G6C", 1),
        #     ],
        # ),
    ]

    t = TimeTableGenerator(classRooms, groups)

    for a in t.generate():
        print(a)

    # print(t.activitySelector())


if __name__ == '__main__':
    run()


# def test(index):
#     if index == 0:
#         return [index]
