from GetTimeTable import getSchoolTime
import schedule
import main
import datetime
import os

days = ['월', '화', '수', '목', '금', '토', '일']

a = datetime.datetime.today().weekday()
today = days[a]


class OpenClassroom:
    links = {
        '영어': 'https://classroom.google.com/c/NDc3NzgwMjM4MTA0',
        '지식': 'https://classroom.google.com/u/2/c/NTM4NjY3ODAyMzg2 https://meet.google.com/sjv-zcao-sxd',
        '국어': 'https://classroom.google.com/u/2/c/NDc4NDM0Nzg2NzI5',
        '국사': 'https://classroom.google.com/c/NDcwOTM4NTEzMjY0 https://meet.google.com/ryn-kska-jmx',
        '체육': 'https://classroom.google.com/c/NDc4MTcyNjE5MzA3',
        '통과': 'https://classroom.google.com/c/NDcwOTM0NTk4MTIx',
        '과실': 'https://classroom.google.com/c/NDcwOTM0NTk4MTIx',
        '통사': 'https://classroom.google.com/c/NDcwOTM5OTUxODE4',
        '수학': 'https://classroom.google.com/c/MjI4MTU2MTI2Njk3',
        '음악': 'https://classroom.google.com/c/NDcwOTM1NTI3MDMx'
    }

    def __init__(self, day: str, classtime: int):
        self.day = day
        self.classtime = classtime

    def bring_timetable(self):
        toegyewonhs = getSchoolTime('퇴계원고등학교', '1-5').loading_timetable()
        return toegyewonhs[self.day]

    def __call__(self):
        table = self.bring_timetable()
        thisclass = table[self.classtime - 1]
        print(thisclass)

        cmdline = 'start chrome --profile-directory="Profile 4"'
        os.system(cmdline + " " + self.links[thisclass])
        return self

def morning():
    print("아침조회")
    os.system('start chrome --profile-directory="Profile 4" https://classroom.google.com/c/NDk4Mzc0Mzc4NzY0')


schedule.every().day.at("08:59").do(morning)
schedule.every().day.at("09:09").do(OpenClassroom(today, 1))
schedule.every().day.at("10:09").do(OpenClassroom(today, 2))
schedule.every().day.at("11:09").do(OpenClassroom(today, 3))
schedule.every().day.at("12:09").do(OpenClassroom(today, 4))
schedule.every().day.at("13:59").do(OpenClassroom(today, 5))
schedule.every().day.at("14:59").do(OpenClassroom(today, 6))
schedule.every().day.at("15:59").do(OpenClassroom(today, 7))

while True:
    schedule.run_pending()
    time.sleep(1)
