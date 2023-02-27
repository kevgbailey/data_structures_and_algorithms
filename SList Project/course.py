''' Course Class for Project 4 of CS 2420 '''

class Course:
    ''' Course object '''
    def __init__(self, number = 0, name="", credit_hr=0, grade=0.0):
         self.number = number
         self.name = name
         self.credit_hr = credit_hr
         self.grade = grade

    def __str__(self):
        courseString = "cs" + str(self.number) + " " + self.name + " Grade: " + str(self.grade) + " Credit Hours: " + str(self.credit_hr)
        return courseString
    
    def __eq__(self, other):
        if self.number is other.number:
            return True
        else: 
            return False

        
    def __ne__(self, other):
        if self.number is not other.number:
            return True
        else: 
            return False

    def __lt__(self, other):
        if self.number < other.number:
            return True
        else: 
            return False
        
    def __gt__(self, other):
        if self.number > other.number:
            return True
        else: 
            return False
        
    def __le__(self, other):
        if self.number <= other.number:
            return True
        else: 
            return False
        
    def __ge__(self, other):
        if self.number >= other.number:
            return True
        else: 
            return False
    
