class Details:
    def __init__(self,subject,start_date,end_date, fine):
        self.subject=subject
        self.start_date=start_date
        self.end_date=end_date

        self.fine=fine
    def __str__(self):
        return "{0},{1},{2},{3}".format(self.subject,self.start_date,self.end_date,self.fine)

class Library:
    def __init__(self,course,data):
        self.course=course
        self.data=data
    def __str__(self):
        return "{0},{1}".format(self.course,self.data)
l=Library("BCA",Details("computer fundamentals","10/1/2023","20/1/2023","Rs5/day"))
print(l)

"""
encapsulation

"""
