class Course:
    ''' Course object '''
    def __init__(self, num = 0, course_name="", credit_hour=0.0, course_grade=0.0):
        if not isinstance(num, int) or num < 0:
            raise ValueError("Wrong type for Course Number")
        if not isinstance(course_name, str):
            raise ValueError("Wrong value for name")
        if not isinstance(credit_hour, float) or credit_hour < 0:
            raise ValueError("Credit hours must be a float")
        if not isinstance(course_grade, float) or course_grade < 0:
            raise ValueError("Grade must be a float")
        self.num = num
        self.course_name = course_name
        self.credit_hour = credit_hour
        self.course_grade = course_grade


    def __str__(self):
        courseString = "cs" + str(self.num) + ", " + self.course_name + " Grade: " + str(self.course_grade) + " Credit Hours: " + str(self.credit_hour)
        return courseString
    
    def number(self):
        return self.num
        
    def name(self):
        return self.course_name
        
    def credit_hr(self):
        return self.credit_hour
        
    def grade(self):
        return self.course_grade
        
    def __eq__(self, other):
        if self.num is other:
            return True
        else: 
            return False

        
    def __ne__(self, other):
        if self.num is not other:
            return True
        else: 
            return False

    def __lt__(self, other):
        if self.num < other:
            return True
        else: 
            return False
        
    def __gt__(self, other):
        if self.num > other:
            return True
        else: 
            return False
        
    def __le__(self, other):
        if self.num <= other:
            return True
        else: 
            return False
        
    def __ge__(self, other):
        if self.num >= other:
            return True
        else: 
            return False
    