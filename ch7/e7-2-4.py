#e7-2-4 簡單的學校管理系統
class Member:
    def setlnfo(self,xm,xb,lb):
        self.name= xm 
        self.gender = xb 
        self.type = lb
    def show(self):
        print(self.name,self.gender,self.type)
class Teacher(Member): #定義教師類別
    def __init__(self,xm,xb,lb):
        Member.setlnfo(self,xm,xb,lb)
        self.lecture=[]
    def setLecture(self): # 
        Lectures = input("請輸入" + self.name+"所教課程(空格分隔,按 Enter 鍵結束)" )
        for t in Lectures.split():
            self.lecture.append(t)
    def show(self): 
        Member.show(self)
        print("所教課程有: ",self.lecture)
class Student(Member) : #定義學生類別
    def __init__(self ,xm,xb,lb):
        Member.setlnfo(self ,xm,xb,lb)
        self.course = [] 
        self.score = []
    def setScore(self): #方法 setScore ()輸入學生所學課程和成績
        Courses = input("請輸入"+self.name+"所學課程(空格分隔,按 Enter 鍵結束)" )
        for t in Courses.split():
            self.course.append(t)
        Scores = input ( "請輸入所學課程對應的成績(空格分隔,按Enter 鍵結束)")
        for t in Scores.split():
            self.score.append(int(t))
    def show( self) : 
        Member.show(self)
        print("所學課程為:",self.course,"對應成績為",self.score)
t1 = Teacher("張三","男","教師")#建立物件並測試
t1.setLecture( )
t1.show()
s1 = Student("李四","女","學生" )
s1.setScore()
s1.show()
