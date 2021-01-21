import tkinter
from tkinter import*
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo,showerror
import sqlite3
import random
import time
import datetime
# import game_execute
# import t
import TypingGame

#로그인화면 배경변수
bg_color = "DeepSkyBlue2"
fg_color = "#383a39"
#단어 초기설정
words=[]

try:
    word_f=open('./resource/word1.txt','r')
except IOError:
    print("파일이 없으므로 게임진행 안됨")
else:
    for c in word_f:
        words.append(c.strip())
    word_f.close()
global start_tt, rankid

#맞힌개수 출력
def rankidpass(rankid):
    toss = rankid
    return toss
def count_print(score):
    return score
def get_randomuser():
    name =""
    db = sqlite3.connect('c:/gitOSSteam3/resource/database.db', isolation_level=None)
    db2 = sqlite3.connect('c:/gitOSSteam3/resource/records.db')
    cursor = db.cursor()
    cursor2 = db2.cursor()

    cursor.execute('SELECT * FROM users')
    cursor2.execute('SELECT * FROM login')
    lst = cursor.fetchall()
    lst2 = cursor2.fetchall()
    
    # rankidpass()
    # print(lst)
    anyone = random.choice(lst)
    id = anyone[0]
    print(lst2)
    print(rankid)
    print(type(name))
    for rid in lst2:
        if rankid in rid:
            name = rankid
            break
    db.close()
    return id, name
def get_nowTime():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d')
#메이크 튜플
def make_tuple(end,score,start_tt):
    lst = []
    id, name = get_randomuser()
    lst.append(id)
    lst.append(name)
    lst.append(count_print(score))
    lst.append(end-start_tt)
    lst.append(get_nowTime())
    tp1 = tuple(lst)
    return tp1
#현재시간받아오기

def input_data(user):
    print(user)
    db = sqlite3.connect('c:/gitOSSteam3/resource/records.db')
    cursor = db.cursor()

    # print(cursor)

    cursor.execute('INSERT INTO records(id, name, cor_cnt, record, regdate) VALUES(?,?,?,?,?)', user)
    db.commit()
    db.close()
#맞힌개수 gui 옆 왼쪽 구석에 time_see가 호출되서 게임진행도중에 보여야되는데 충돌때문에 미구현.
def time_see():
    global tm
    tm = tm+1
    t.config(text='소요시간 : '+str(tm),  font =("휴먼매직체", 20) ,fg='red')
    t.place(x=2,y=350)
    root.after(1000,time_see)
#결과화면 출력
def result(end,score):
    global start_tt
    # print("dfdf")
    # print(score)
    print(end)
    print(start_tt)
    # print(type(get_nowTime()))
    user = make_tuple(end,score,start_tt)
    input_data(user)

    res = Tk()
    res.config(bg='black')
    res.title("결과화면")
    res.geometry("600x400")
    re = Label(res, text='맞힌개수 : '+str(count_print(score)),fg='blue',font=('휴먼매직체',40),bg = 'black')
    re.place(x=150,y=300)
    see = Label(res, text='걸린시간 : '+format(end-start_tt,'.3f'),fg='red',font=('휴먼매직체',40),bg='black')
    see.place(x=100,y=245)
    lbl = Label(res, text = "Ranking")
    lbl.pack()

    treeview = ttk.Treeview(res, columns=['one', 'two', 'three', 'four', 'five'], displaycolumn = ["one", 'two', 'three', 'four', 'five'])
    treeview.pack()

    treeview.column("#0", width = 50,)
    treeview.heading("#0", text = "Rank")

    treeview.column("#1", width = 50, anchor = "center")
    treeview.heading("#1", text = "아이디 넘버")

    treeview.column("#2", width = 70, anchor = "center")
    treeview.heading("#2", text = "아이디", anchor = "center")

    treeview.column("#3", width = 100, anchor = "center")
    treeview.heading("#3", text = "맞춘 개수", anchor = "center")

    treeview.column("#4", width = 100, anchor = "center")
    treeview.heading("#4", text = "클리어 시간", anchor = "center")

    treeview.column("#5", width = 150, anchor = "center")
    treeview.heading("#5", text = "날짜", anchor = "center")

    db = sqlite3.connect('c:/gitOSSteam3/resource/records.db')
    cursor = db.cursor()

    cursor.execute('select * from records')
    records = cursor.fetchall()
    db.close()
    records.sort(key = lambda x:(-x[2], float(x[3])))
    for i in range(len(records)):
        treeview.insert('', 'end', text = i + 1, values = records[i], iid=str(i) + "번")
    res.mainloop()
#클래스1 = game진행 클래스.
start_tt=time.time()
class game():
    global root,e
    def __init__(self):
        global a, score, tm, t
        root = Tk()
        root.geometry("600x400")
        root.title("타이핑게임 실행화면")
        # exlabel = Label(root, text="{} 님이 Login 중입니다.".format(userid)).grid(row=1,column=0, padx=(50, 0), pady=(20, 10))
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
        # count.pack()
        #바뀌는 시간 출력해줄 라벨
        t = Label(root)
        print("루프전줄까지실행")
        #게임시작함수.
        def start():
            global end_tt
            try:
                    #게임횟수 10번
                if a < 10 :
                    if tm==-1:
                        # time_see()
                        pass
                    random.shuffle(words)
                    random_word = random.choice(words)
                    print(random_word)
                    q.config(text=str(random_word))
                    typing.place(x=70,y=200)
                    count.place(x=400, y=350)
                    def n(event):
                        global a,score
                        if typing.get()==random_word.lower():
                            typing.delete(0,END)
                            score = score + 1
                            count.config(text='맞힌개수 : '+str(score))
                            count_print(score)
                            print(score)
                            start()
                            a=a+1
                        else:
                            typing.delete(0,END)
                            start()
                            a=a+1
                    root.bind("<Return>",n)
                else:
                    global ent_tt
                    end_tt = time.time()
                    root.destroy()
                    result(end_tt,score)
            except:
                pass
        start()
        root.mainloop()
#클래스2 = 첫 gui 로그인 페이지 
class typingApp:
    def __init__(self):
        #id쪽 ui
        global lbluserid, lblpassword, master
        master = tkinter.Tk()
        master.geometry("390x350")
        master.configure(background= bg_color)
        master.title("환영합니다. 타이핑게임")
        photo = ImageTk.PhotoImage(Image.open("./resource/typing.jpg"))
        tkinter.Label(master, image=photo).grid(rowspan = 3, columnspan = 5, row =0,column = 0)
        tkinter.Label(master).grid(rowspan = 3, columnspan = 5, row =0,column = 0)
        tkinter.Label(master,  text="Userid:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=8, padx=(50, 0), pady=(20, 10))

        lbluserid = tkinter.Entry(master)
        lbluserid.grid(row=8, column=1, padx=(10, 10), pady=(20, 10))

        #비밀번호쪽 ui
        tkinter.Label(master,  text="Password:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=9, padx=(50, 0), pady=(20, 10))
        lblpassword = tkinter.Entry(master)
        lblpassword.grid(row=9, column=1, padx=(10, 10),pady=(20, 10))

        #로그인버튼
        tkinter.Button(master, text="Login",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 15, command = self.login).grid(row = 10, padx=(50, 0), pady=(20, 10))
        #회원가입 버튼
        tkinter.Button(master, text="sign",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 15, command = self.sign).grid(row = 10, column=1,pady=(20, 10))
        master.mainloop()
    #login 이벤트
    def login(self):
        global userid, password, rankid
        db = sqlite3.connect('c:/gitOSSteam3/resource/records.db')
        c = db.cursor()
        userid = lbluserid.get()
        password = lblpassword.get()
        c.execute("SELECT * FROM login WHERE user_id = ? AND user_password = ?", (userid,password))
        if c.fetchall():
            showinfo(title = "Login", message = "로그인 성공!!")
            TypingGame.typingGame.user_info(userid)
            rankid = userid
            print(rankid)
            game()
        else:
            showerror(title = "Login", message = "로그인 실패!! ID or Password 확인!")
        c.close()
    #회원가입 창 gui, 즉 회원가입 버튼을 누를시 이벤트 발생.
    def sign(self):
        global sign,lbluserid2,lblpassword2
        sign = tkinter.Tk()
        sign.geometry("390x350")
        sign.configure(background= bg_color)
        sign.title("회원 가입")
        #회원가입 아이디
        tkinter.Label(sign,  text="User_id:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=8, padx=(50, 0), pady=(20, 10))
        lbluserid2 = tkinter.Entry(sign)
        lbluserid2.grid(row=8, column=1, padx=(10, 10), pady=(20, 10))
        #회원가입 비밀번호
        tkinter.Label(sign,  text="User_password:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=9, padx=(50, 0), pady=(20, 10))
        lblpassword2 = tkinter.Entry(sign)
        lblpassword2.grid(row=9, column=1, padx=(10, 10), pady=(20, 10))
        #회원가입 하기 버튼
        tkinter.Button(sign, text="회원 가입",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 15, command = self.signdone).grid(row = 10, padx=(50, 0), pady=(20, 10))
        tkinter.Button(sign, text="취소",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 15, command = self.close1).grid(row = 10,column=1, padx=(50, 0), pady=(20, 10))
        sign.mainloop()
    #회원가입 닫기 이벤트
    def close1(self):
        sign.destroy()
        print("닫기")
    #회원가입완료버튼 이벤트
    def signdone(self):
        db = sqlite3.connect('c:/gitOSSteam3/resource/records.db',isolation_level=None)
        c = db.cursor()
        userid2 = lbluserid2.get()
        password2 = lblpassword2.get()
        # sql = "INSERT INTO login (user_id,user_password)VALUES({0},{1})",format(userid2,password2)
        sql = 'INSERT INTO login (user_id, user_password) VALUES(?,?)'
        # txt = c.execute("SELECT * FROM login WHERE user_id like '{}%'" % userid2)
        # print(txt)
        # if userid2 == c.execute("SELECT * FROM login WHERE user_id=%s" % userid2):
        #     print("중복")
        c.execute(sql,(userid2,password2))
        # c.commit()
        for uid in c.execute("SELECT * FROM login WHERE user_id=?",(userid2,)):
            if uid == uid:
                showinfo(title="회원가입 성공", message="회원가입 성공!!!")
                sign.destroy()
            else:
                showerror(title="아이디중복오류",message="다른 아이디를 입력해주세요.")
        c.close()
# 첫 로그인페이지을 부르는 메인함수
def main():
    typingApp()
if __name__ == "__main__":
    main()