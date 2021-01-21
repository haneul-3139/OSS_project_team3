import tkinter
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo,showerror
import sqlite3
import random
import time
# import game_execute
# import t
import TypingGame

#로그인화면 배경변수
bg_color = "DeepSkyBlue2"
fg_color = "#383a39"
# 단어 초기설정
words=[]

try:
    word_f=open('./resource/word1.txt','r')
except IOError:
    print("파일이 없으므로 게임진행 안됨")
else:
    for c in word_f:
        words.append(c.strip())
    word_f.close()

#클래스
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
    
    #추가적으로 밑에다가 구현해야함! 로그인하면 로그인창 꺼지고
    #새로운 gui가 오픈되어야함, 즉 새로운 프레임 오픈
    #그 안에다가 user_id 를 얻어와서 누구누구님 환영합니다. 써지게하고 밑에는 타이핑게임 구현 하려함.
    #간단하게 타이핑 게임 text에다가 word.txt를 불러와서 랜덤에하게 나온 글자를 
    #Text()에다가 뿌려줌 정확하게 타이핑하고 교수님이 미리 구현해놓은 비교구문으로 
    #text() 와 text를 비교하여 get으로 얻어와 정답 / 오답 구분
    #마지막엔 label에다가 텍스트를 작성. ex) 걸린시간 : 131313 , 정답수 : 10
    #그럼 db에는 시간, 정답수 등 저장될꺼임
    #그럼 그 데이터와 회원가입한 userid를 가지고 순위를 매김
    # 즉 그럼 타이핑게임이 종료되는시점에서 타이핑게임 GUI는 종료 새로운 순위 GUI가 오픈되도록
    #설정할 예정 첫 계획안이라 전부 안될수도있음. 일단 참고 부탁드릴게요.

    #login 이벤트
    def login(self):
        global userid, password
        db = sqlite3.connect('c:/gitOSSteam3/resource/records.db')
        c = db.cursor()
        userid = lbluserid.get()
        password = lblpassword.get()
        c.execute("SELECT * FROM login WHERE user_id = ? AND user_password = ?", (userid,password))
        if c.fetchall():
            showinfo(title = "Login", message = "{}님이 로그인 하셨습니다.".format(userid))
            TypingGame.typingGame.user_info(userid)
            # game()
            # game.start()
        else:
            showerror(title = "Login", message = "로그인 실패!! ID or Password 확인!")
        c.close()
#회원가입 버튼 이벤트
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
        sql2 = 'INSERT INTO login (user_id, user_password) VALUES(?,?)'
        # txt = c.execute("SELECT * FROM login WHERE user_id like '{}%'" % userid2)
        # print(txt)
        # if userid2 == c.execute("SELECT * FROM login WHERE user_id=%s" % userid2):
        #     print("중복")
        # print(userid2,password2)
        # c.commit()
        c.execute(sql2,(userid2,password2))
        for uid in c.execute("SELECT * FROM login WHERE user_id=?",(userid2,)):
            if uid == uid:
                showinfo(title="회원가입 성공", message="회원가입 성공!!!")
                sign.destroy()
            else:
                showerror(title="아이디중복오류",message="다른 아이디를 입력해주세요.")
        c.close()
#맞힌개수 출력
def count_print(score):
    return score
def main():
    typingApp()
if __name__ == "__main__":
    main()