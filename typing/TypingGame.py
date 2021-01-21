import tkinter
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo,showerror
import typing_main
import sqlite3
import tkinter.simpledialog
global strname

class typingGame():
    def __init__(self,user_id):
        self.user_id = user_id
    def user_info(strname):
        strname = strname
        print(strname)

class typGameGui:
    
    # global tpg
    # tpg = tkinter.Tk()
    # tpg.title("Typing Game!")
    # tpg.geometry("400x400")

    # # db에서 가져올 영문자 라벨
    # label1 = tkinter.Label(tpg,text="db에서받아올 str값").grid(row=0,column=0,padx=(50, 0), pady=(20, 10))
    # # 입력받을 영문자 값
    # tptxt = tkinter.simpledialog.askstring("Typing Game!","주어진 영문자를 입력하세요.")
    #입력한 값 대조
    # label1.configure(text=str(tptxt))
    # print(type(tptxt))
    # if tptxt == "1" or None:
    pass
    # else:
    #     print("확인용")
# if __name__ == "__main__":
#     tpg.mainloop()