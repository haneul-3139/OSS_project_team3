from tkinter import*
import random
import time
import sys
#사운드 출력 필요 모듈
import sqlite3


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


#게임실행
class game():
    def start():
        global end_tt
        
        try:
            #게임횟수 바꿔주려면 2값을 바꿔주면 됨
            if a < 5 :
                
                random.shuffle(words)
                random_word = random.choice(words)

                q.config(text=str(random_word))
                typing.place(x=70,y=200)
                count.place(x=400, y=350)
            
            
                def n(event):
                    global a
                    global score
                    if e.get()==random_word.lower():
                        # winsound.PlaySound('./sound/good.wav',winsound.SND_FILENAME)
                        typing.delete(0,END)
                        score = score + 1
                        count.config(text='맞힌개수 : '+str(score))
                        game.start()
                        a=a+1

                    else:
                        # winsound.PlaySound('./sound/bad.wav',winsound.SND_FILENAME)
                        typing.delete(0,END)
                        game.start()
                        a=a+1
            
                root.bind("<Return>",n)
            else:
                root.destroy()
        except:
            pass
    start()


root.mainloop()
