# Timetable generator:
# A school has
# 5 classrooms,
# 6 groups of students,

# each group requires
# to attend lectures of at most 4 hours in a day.

# The duration of the lectures is
# either 1 hour or 2 hour. [done]

# Write a program to generate a weekly timetable for the school.
# Hint: use greedy algorithms.

# STEPS

# 1. sort by finish time ascending order

class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.hoursLeft = 7  # 5  - 12

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Group:

    def __init__(self, name, activites):
        self.name = name
        self.activites = activites

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Activity:
    def __init__(self, groupName, name, startTime, endTime, days):
        assert((endTime - startTime) <= 2)
        self.groupName = groupName
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        self.days = days
        self.activityTime = endTime - startTime

    def __str__(self):
        return "T" + str(self.startTime) + "-" + str(self.endTime) + ": " + str(self.name)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.endTime < other.endTime


class TimeTableGenerator:

    notAssignedActivites = [[]] * 7

    def __init__(self, classRooms, groups):
        self.classRooms = classRooms
        self.groups = groups

        for i in range(0, 6):
            self.notAssignedActivites[i] = []

        for g in self.groups:
            for a in g.activites:
                for d in a.days:
                    self.notAssignedActivites[d].append(a)

        # sort not assigned activities by finish time - ascending order
        for dayActivities in self.notAssignedActivites:
            dayActivities.sort()

    def generate(self):
        # fill each class one by one

        generated = []

        for dayIndex, dayActivities in enumerate(self.notAssignedActivites):
            for classRoom in self.classRooms:
                # select activity for classRoom
                a = (
                    dayIndex,
                    classRoom,
                    self.activitySelector(classRoom, dayActivities)
                )

                generated.append(a)

        return generated

    def activitySelector(self, classRoom, activities):
        n = len(activities)

        if n <= 0:
            return []

        removedActivites = [activities[0]]
        A = [activities[0]]

        k = 1

        for m in range(2, n):

            am = activities[m]
            ak = activities[k]

            if (am.startTime >= ak.endTime) and classRoom.hoursLeft >= am.activityTime and self.getGroupStudyHours(am.groupName, activities) <= 4:
                if(am not in removedActivites):
                    classRoom.hoursLeft -= am.activityTime
                    A.append(am)
                    removedActivites.append(am)
                    k = m

        for activity in removedActivites:
            activities.remove(activity)

        return A

    def getGroupStudyHours(self, groupName, activities):
        studyHours = 0
        for a in activities:
            if a.groupName == groupName:
                studyHours += a.activityTime

        return studyHours
