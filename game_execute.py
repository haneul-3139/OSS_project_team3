import tkinter
import tkinter.ttk
import random
import time
import sys
import sqlite3
#사운드 출력 필요 모듈
import winsound
import sqlite3
import datetime
from tkinter import *


#단어
words=[]


try:
    word_f=open('./resource/word1.txt','r')
except IOError:
    print("파일이 없으므로 게임진행 안됨")
else:
    for c in word_f:
        words.append(c.strip())
    word_f.close()


root = Tk()
root.title("타이핑게임 실행화면")
root.geometry("600x400")
root.config(bg='white')


#게임 플레이 횟수
a=1

#맞힌개수 초기화
score = 0

#시간설정 초기화
tm = -1

e = StringVar()

#입력창
typing = Entry(root,textvariable=e, font=("휴먼매직체", 30), bg='black', fg='white')

#랜덤 단어 보여주기
q = Label(root,font=("휴먼매직체", 50), bg='white')
q.pack(side='top')

#맞힌개수
count = Label(root, text="맞힌개수 : 0", font =("휴먼매직체", 20), fg ='blue' )

#바뀌는 시간 출력해줄 라벨
t = Label(root)
    
#맞힌개수 출력
def count_print(score):
    return score


def get_nowTime():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d')


def make_tuple(end):
    global start_tt
    lst = []
    id, name = get_randomuser()

    lst.append(id)
    lst.append(name)
    lst.append(count_print(score))
    lst.append(end-start_tt)
    lst.append(get_nowTime())

    return tuple(lst)


#결과 출력
def result(end):
    global start_tt

    user = make_tuple(end)
    input_data(user)

    res = Tk()
    res.config(bg='black')
    res.title("결과화면")
    res.geometry("600x400")
    re = Label(res, text='맞힌개수 : '+str(count_print(score)),fg='blue',font=('휴먼매직체',40),bg = 'black')
    re.place(x=150,y=200)
    see = Label(res, text='걸린시간 : '+format(end-start_tt,'.3f'),fg='red',font=('휴먼매직체',40),bg='black')
    see.place(x=100,y=100)
    


start_tt = time.time()
# 타임 보이기
def time_see():
    global tm
    tm = tm+1
    t.config(text='소요시간 : '+str(tm),  font =("휴먼매직체", 20) ,fg='red')
    t.place(x=2,y=350)
    root.after(1000,time_see)


# 랜덤으로 유저 하나 가져와서 내 정보로 쓰는 것. 로그인이 안돼서 썼어요!
def get_randomuser():
    db = sqlite3.connect('./resource/database.db', isolation_level=None)
    cursor = db.cursor()

    cursor.execute('SELECT * FROM users')
    lst = cursor.fetchall()

    anyone = random.choice(lst)
    id = anyone[0]
    name = anyone[1]
    db.close()
    return id, name


def input_data(user):
    db = sqlite3.connect('./resource/records.db', isolation_level=None)
    cursor = db.cursor()

    print(cursor)

    cursor.execute('INSERT INTO records(id, name, cor_cnt, record, regdate) VALUES(?,?,?,?,?)', user)
    db.commit()
    db.close()


#게임실행
class game():
    def start():
        global end_tt
        
        try:
            #게임횟수 10번
            if a < 10 :
                if tm==-1:
                    time_see()
                random.shuffle(words)
                random_word = random.choice(words)

                q.config(text=str(random_word))
                typing.place(x=70,y=200)
                count.place(x=400, y=350)
            
            
                def n(event):
                    global a
                    global score
                    if e.get()==random_word.lower():
                        winsound.PlaySound('./resource/audio/good.wav',winsound.SND_FILENAME)
                        typing.delete(0,END)
                        score = score + 1
                        count.config(text='맞힌개수 : '+str(score))
                        count_print(score)
                        game.start()
                        a=a+1

                    else:
                        winsound.PlaySound('./resource/audio/bad.wav',winsound.SND_FILENAME)
                        typing.delete(0,END)
                        game.start()
                        a=a+1
            
                root.bind("<Return>",n)
            else:
                end_tt = time.time()
                root.destroy()
                result(end_tt)
        except:
            pass
    start()


root.mainloop()