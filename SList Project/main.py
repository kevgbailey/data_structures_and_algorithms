from slist import SList
from course import Course

def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.grade * course.credit_hr
        credits += course.credit_hr
    if credits == 0:
        return 0
    return sumGrades / credits

def is_sorted(lyst):
    for i in range(0, len(lyst)  - 1):
        if lyst[i] > lyst[i + 1]:
            return False
    return True
    
def main():
    pass
  
if __name__ == "__main__":
    main()

test_slist = SList()
# test_slist.insert(4)
# test_slist.insert(1)
# test_slist.insert(3)
# test_slist.insert(2)
# test_slist.insert(1)
# test_slist.insert(3)
# test_slist.insert(12)
# test_slist.insert(1)
# test_slist.insert(7)
# test_slist.insert(8)
# test_slist.insert(12)
# test_slist.insert(3)
# print(test_slist)
# test_slist.remove_all(12)
# test_slist.remove(3)
# print(test_slist)
# print(test_slist.__len__())

# for value in test_slist:
#     print(value)

# print(test_slist)
# print("getitem test:")
# print(test_slist.__getitem__(10))
test_slist.insert(Course(1400, "Intro to Programming", 3, 4.0))
test_slist.insert(Course(2420, "Data Structures and Algorithms", 4, 3.8))
test_slist.insert(Course(1410, "Object Oriented Programming", 3, 3.7))
test_slist.insert(Course(4200, "Super Hard CS Course", 5, 2.8))
test_slist.insert(Course(5200, "Super Senior Capstone", 6, 4.0))
test_slist.insert(Course(3207, "React Web Development", 3, 3.7))


print(is_sorted(test_slist))
