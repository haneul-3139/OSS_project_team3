def prt1():
    print("test package!")
def prt2():
    print("test module!")

#단위 실행(독립적으로 파일 실행)
if __name__ == "__main__":
    print("this is ", dir())
    prt1()
    prt2()
else:
    print("외부에서 모듈 호출함")