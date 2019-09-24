class Exams:
    def __init__(self, subject, exam_date):
        self.subject = subject
        self.exam_date = exam_date
    def setSubject(self, subject):
        self.subject = subject
    def getSubject(self):
        return self.subject
    def setDate(self, exam_date):
        self.exam_date = exam_date
    def getDate(self):
        return self.exam_date

exam = Exams("Mathematics", "29 November 2019")
print(exam.getDate())
exam.setDate("14 Dec 2019")
print(exam.getDate())
