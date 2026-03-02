import datetime
import threading
import psutil
timereal = datetime.datetime.now().time()
timefake = str(timereal).split(":")
if 5<=int(timefake[0])<12:
    print("Good Morning User!")
elif 12<=int(timefake[0])<=17:
    print("Good afternoon User!")
elif 17<=int(timefake[0])<22:
    print("Good evening user!")
else:
    print("Hey User! It's kinda late, but alright if you want to study!!")
blockedapps=["VALORANT-Win64-Shipping.exe", "Notepad.exe"]
def windowtracker():
    chiggi  = True
    while True:
        ids = psutil.pids()
        for ida in ids:
            try:
                if(str(psutil.Process(ida)).split(",")[1][7:len(str(psutil.Process(ida)).split(",")[1])-1]) in blockedapps:
                    killed = psutil.Process(ida)
                    killed.terminate()
            except:
                print("",end="")
e=open("syllabus.txt", "r+")
f=e.read()
g=f.replace("\n", "   ")
m=g.split("|||")
nga = True
a=["P&S", "C++", "DS", "Value Education", "Chemistry", "Entrepreneurship", "Engg Graphs", "Logical Designing"]
c=1
for i in a:
    print(str(c)+".", i)
    c=c+1
if nga == True:
    b=int(input("Which subject do you want to study as of right now ?: "))
    if b==1:
        kk=0
        k=[]
        kk=[]
        unitname=[]
        uwisetopics=[]
        unitindexes=[]
        unitcounti = 0
        n=m[b-1].split(",")
        print(n[b-1], "Syllabus:")
        for j in range (1 ,len(n)):
            if n[j][1]!="U":
                if n[j][2]!="n":
                    if n[j][3]!="i":
                        if n[j][4]!="t":
                            k.append(n[j])
            else:
                unitname.append(n[j+1])
                kk.append(n[j])
                unitcounti+=1
                continue
        for j in range (1 ,len(n)):
            if n[j][1]=="U":
                if n[j][2]=="n":
                    if n[j][3]=="i":
                        if n[j][4]=="t":
                            unitindexes.append(j)
        for gg in range(0, len(unitindexes)):
            if gg+1 < len(unitindexes):
                uwisetopics.append(n[unitindexes[gg]:unitindexes[gg+1]+1])
            else:
                uwisetopics.append(n[unitindexes[gg]:len(n)])
        print("There are ",unitcounti," units in this subject. Which one would you like to study? ")
        for ll in range (0, len(kk)):
            print(ll+1,". ",kk[ll],": ",unitname[ll])
        print("Please enter your input(1-"+str(len(kk))+"): ",end="")
        bb=int(input())
        for iii in range (1,len(kk)):
            if bb==iii:
                print("The topics for", unitname[bb-1], "are:")
                for tt in range(1, len(uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1])+1):
                    print(str(tt)+". ",uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1][tt-1])
                print("Which topic do you want to study right now?\nPlease enter your input(1-"+str(len(uwisetopics[bb-1])-3)+"): ",end="")
                topname=int(input())
                if uwisetopics[bb-1][(topname+1)] in uwisetopics[bb-1][2:len(uwisetopics[bb-1])]:
                    print("You are studying"+uwisetopics[bb-1][(topname+1)]+" right now: ")        
                    print("Starting the timer!")
                    print("Starting the app monitor!")
                    print("You started studying at: ",end="")
                    if int(timefake[0])>=12:

                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" PM")
                    else:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" AM")
                    tracker = threading.Thread(target=windowtracker)
                    tracker.start()
                    print("Please press enter(return) as soon as you want to end your current study session, along with the timer!\n", end="")
                    aaa = input("Waiting for user input: ")
                    if aaa:
                        chiggi = False
                    realtime1=datetime.datetime.now().time()
                    timefake1=str(realtime1).split(":")
                    print("You ended your study session at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" PM")
                    else:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" AM")
                    print("Timer ended!")        
                    print("You studied for a total of: "+ str(abs(int(timefake1[0])-int(timefake[0])))+" hours "+str(abs(int(timefake1[1])-int(timefake[1])))+" minutes and "+str(abs(int(timefake1[2].split(".")[0])-int(timefake[2].split(".")[0])))+" seconds")
    elif b==2:
        kk=0
        k=[]
        kk=[]
        unitname=[]
        uwisetopics=[]
        unitindexes=[]
        unitcounti = 0
        n=m[b-1].split(",")
        print(n[0], "Syllabus:")
        for j in range (1 ,len(n)):
            if n[j][1]!="U":
                if n[j][2]!="n":
                    if n[j][3]!="i":
                        if n[j][4]!="t":
                            k.append(n[j])
            else:
                unitname.append(n[j+1])
                kk.append(n[j])
                unitcounti+=1
                continue
        for j in range (1 ,len(n)):
            if n[j][1]=="U":
                if n[j][2]=="n":
                    if n[j][3]=="i":
                        if n[j][4]=="t":
                            unitindexes.append(j)
        for gg in range(0, len(unitindexes)):
            if gg+1 < len(unitindexes):
                uwisetopics.append(n[unitindexes[gg]:unitindexes[gg+1]+1])
            else:
                uwisetopics.append(n[unitindexes[gg]:len(n)])
        print("There are ",unitcounti," units in this subject. Which one would you like to study? ")
        for ll in range (0, len(kk)):
            print(ll+1,". ",kk[ll],": ",unitname[ll])
        print("Please enter your input(1-"+str(len(kk))+"): ",end="")
        bb=int(input())
        for iii in range (1,len(kk)):
            if bb==iii:
                print("The topics for", unitname[bb-1], "are:")
                for tt in range(1, len(uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1])+1):
                    print(str(tt)+". ",uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1][tt-1])
                print("Which topic do you want to study right now?\nPlease enter your input(1-"+str(len(uwisetopics[bb-1])-3)+"): ",end="")
                topname=int(input())
                if uwisetopics[bb-1][(topname+1)] in uwisetopics[bb-1][2:len(uwisetopics[bb-1])]:
                    print("You are studying "+uwisetopics[bb-1][(topname+1)]+" right now: ")        
                    print("Starting the timer!")
                    print("You started studying at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" PM")
                    else:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" AM")
                    tracker = threading.Thread(target=windowtracker)
                    tracker.start()
                    print("Please press enter(return) as soon as you want to end your current study session, along with the timer!\n", end="")
                    aaa = input("Waiting for user input: ")
                    if aaa:
                        chiggi = False
                    timerstate = input()
                    realtime1=datetime.datetime.now().time()
                    timefake1=str(realtime1).split(":")
                    print("You ended your study session at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" PM")
                    else:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" AM")
                    print("Timer ended!")        
                    print("You studied for a total of: "+ str(abs(int(timefake1[0])-int(timefake[0])))+" hours "+str(abs(int(timefake1[1])-int(timefake[1])))+" minutes and "+str(abs(int(timefake1[2].split(".")[0])-int(timefake[2].split(".")[0])))+" seconds")
    elif b==3:
        kk=0
        k=[]
        kk=[]
        unitname=[]
        uwisetopics=[]
        unitindexes=[]
        unitcounti = 0
        n=m[b-1].split(",")
        print(n[0], "Syllabus:")
        for j in range (1 ,len(n)):
            if n[j][1]!="U":
                if n[j][2]!="n":
                    if n[j][3]!="i":
                        if n[j][4]!="t":
                            k.append(n[j])
            else:
                unitname.append(n[j+1])
                kk.append(n[j])
                unitcounti+=1
                continue
        for j in range (1 ,len(n)):
            if n[j][1]=="U":
                if n[j][2]=="n":
                    if n[j][3]=="i":
                        if n[j][4]=="t":
                            unitindexes.append(j)
        for gg in range(0, len(unitindexes)):
            if gg+1 < len(unitindexes):
                uwisetopics.append(n[unitindexes[gg]:unitindexes[gg+1]+1])
            else:
                uwisetopics.append(n[unitindexes[gg]:len(n)])
        print("There are ",unitcounti," units in this subject. Which one would you like to study? ")
        for ll in range (0, len(kk)):
            print(ll+1,". ",kk[ll],": ",unitname[ll])
        print("Please enter your input(1-"+str(len(kk))+"): ",end="")
        bb=int(input())
        for iii in range (1,len(kk)):
            if bb==iii:
                print("The topics for", unitname[bb-1], "are:")
                for tt in range(1, len(uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1])+1):
                    print(str(tt)+". ",uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1][tt-1])
                print("Which topic do you want to study right now?\nPlease enter your input(1-"+str(len(uwisetopics[bb-1])-3)+"): ",end="")
                topname=int(input())
                if uwisetopics[bb-1][(topname+1)] in uwisetopics[bb-1][2:len(uwisetopics[bb-1])]:
                    print("You are studying "+uwisetopics[bb-1][(topname+1)]+" right now: ")        
                    print("Starting the timer!")
                    print("You started studying at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" PM")
                    else:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" AM")
                    tracker = threading.Thread(target=windowtracker)
                    tracker.start()
                    print("Please press enter(return) as soon as you want to end your current study session, along with the timer!\n", end="")
                    aaa = input("Waiting for user input: ")
                    if aaa:
                        chiggi = False
                    timerstate = input()
                    realtime1=datetime.datetime.now().time()
                    timefake1=str(realtime1).split(":")
                    print("You ended your study session at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" PM")
                    else:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" AM")
                    print("Timer ended!")        
                    print("You studied for a total of: "+ str(abs(int(timefake1[0])-int(timefake[0])))+" hours "+str(abs(int(timefake1[1])-int(timefake[1])))+" minutes and "+str(abs(int(timefake1[2].split(".")[0])-int(timefake[2].split(".")[0])))+" seconds")
    elif b==4:
        kk=0
        k=[]
        kk=[]
        unitname=[]
        uwisetopics=[]
        unitindexes=[]
        unitcounti = 0
        n=m[b-1].split(",")
        print(n[0], "Syllabus:")
        for j in range (1 ,len(n)):
            if n[j][1]!="U":
                if n[j][2]!="n":
                    if n[j][3]!="i":
                        if n[j][4]!="t":
                            k.append(n[j])
            else:
                unitname.append(n[j+1])
                kk.append(n[j])
                unitcounti+=1
                continue
        for j in range (1 ,len(n)):
            if n[j][1]=="U":
                if n[j][2]=="n":
                    if n[j][3]=="i":
                        if n[j][4]=="t":
                            unitindexes.append(j)
        for gg in range(0, len(unitindexes)):
            if gg+1 < len(unitindexes):
                uwisetopics.append(n[unitindexes[gg]:unitindexes[gg+1]+1])
            else:
                uwisetopics.append(n[unitindexes[gg]:len(n)])
        print("There are ",unitcounti," units in this subject. Which one would you like to study? ")
        for ll in range (0, len(kk)):
            print(ll+1,". ",kk[ll],": ",unitname[ll])
        print("Please enter your input(1-"+str(len(kk))+"): ",end="")
        bb=int(input())
        for iii in range (1,len(kk)):
            if bb==iii:
                print("The topics for", unitname[bb-1], "are:")
                for tt in range(1, len(uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1])+1):
                    print(str(tt)+". ",uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1][tt-1])
                print("Which topic do you want to study right now?\nPlease enter your input(1-"+str(len(uwisetopics[bb-1])-3)+"): ",end="")
                topname=int(input())
                if uwisetopics[bb-1][(topname+1)] in uwisetopics[bb-1][2:len(uwisetopics[bb-1])]:
                    print("You are studying "+uwisetopics[bb-1][(topname+1)]+" right now: ")        
                    print("Starting the timer!")
                    print("You started studying at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" PM")
                    else:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" AM")
                    tracker = threading.Thread(target=windowtracker)
                    tracker.start()
                    print("Please press enter(return) as soon as you want to end your current study session, along with the timer!\n", end="")
                    aaa = input("Waiting for user input: ")
                    if aaa:
                        chiggi = False
                    timerstate = input()
                    realtime1=datetime.datetime.now().time()
                    timefake1=str(realtime1).split(":")
                    print("You ended your study session at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" PM")
                    else:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" AM")
                    print("Timer ended!")        
                    print("You studied for a total of: "+ str(abs(int(timefake1[0])-int(timefake[0])))+" hours "+str(abs(int(timefake1[1])-int(timefake[1])))+" minutes and "+str(abs(int(timefake1[2].split(".")[0])-int(timefake[2].split(".")[0])))+" seconds")
    elif b==5:
        kk=0
        k=[]
        kk=[]
        unitname=[]
        uwisetopics=[]
        unitindexes=[]
        unitcounti = 0
        n=m[b-1].split(",")
        print(n[0], "Syllabus:")
        for j in range (1 ,len(n)):
            if n[j][1]!="U":
                if n[j][2]!="n":
                    if n[j][3]!="i":
                        if n[j][4]!="t":
                            k.append(n[j])
            else:
                unitname.append(n[j+1])
                kk.append(n[j])
                unitcounti+=1
                continue
        for j in range (1 ,len(n)):
            if n[j][1]=="U":
                if n[j][2]=="n":
                    if n[j][3]=="i":
                        if n[j][4]=="t":
                            unitindexes.append(j)
        for gg in range(0, len(unitindexes)):
            if gg+1 < len(unitindexes):
                uwisetopics.append(n[unitindexes[gg]:unitindexes[gg+1]+1])
            else:
                uwisetopics.append(n[unitindexes[gg]:len(n)])
        print("There are ",unitcounti," units in this subject. Which one would you like to study? ")
        for ll in range (0, len(kk)):
            print(ll+1,". ",kk[ll],": ",unitname[ll])
        print("Please enter your input(1-"+str(len(kk))+"): ",end="")
        bb=int(input())
        for iii in range (1,len(kk)):
            if bb==iii:
                print("The topics for", unitname[bb-1], "are:")
                for tt in range(1, len(uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1])+1):
                    print(str(tt)+". ",uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1][tt-1])
                print("Which topic do you want to study right now?\nPlease enter your input(1-"+str(len(uwisetopics[bb-1])-3)+"): ",end="")
                topname=int(input())
                if uwisetopics[bb-1][(topname+1)] in uwisetopics[bb-1][2:len(uwisetopics[bb-1])]:
                    print("You are studying "+uwisetopics[bb-1][(topname+1)]+" right now: ")        
                    print("Starting the timer!")
                    print("You started studying at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" PM")
                    else:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" AM")
                    tracker = threading.Thread(target=windowtracker)
                    tracker.start()
                    print("Please press enter(return) as soon as you want to end your current study session, along with the timer!\n", end="")
                    aaa = input("Waiting for user input: ")
                    if aaa:
                        chiggi = False
                    timerstate = input()
                    realtime1=datetime.datetime.now().time()
                    timefake1=str(realtime1).split(":")
                    print("You ended your study session at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" PM")
                    else:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" AM")
                    print("Timer ended!")        
                    print("You studied for a total of: "+ str(abs(int(timefake1[0])-int(timefake[0])))+" hours "+str(abs(int(timefake1[1])-int(timefake[1])))+" minutes and "+str(abs(int(timefake1[2].split(".")[0])-int(timefake[2].split(".")[0])))+" seconds")
    elif b==6:
        kk=0
        k=[]
        kk=[]
        unitname=[]
        uwisetopics=[]
        unitindexes=[]
        unitcounti = 0
        n=m[b-1].split(",")
        print(n[0], "Syllabus:")
        for j in range (1 ,len(n)):
            if n[j][1]!="U":
                if n[j][2]!="n":
                    if n[j][3]!="i":
                        if n[j][4]!="t":
                            k.append(n[j])
            else:
                unitname.append(n[j+1])
                kk.append(n[j])
                unitcounti+=1
                continue
        for j in range (1 ,len(n)):
            if n[j][1]=="U":
                if n[j][2]=="n":
                    if n[j][3]=="i":
                        if n[j][4]=="t":
                            unitindexes.append(j)
        for gg in range(0, len(unitindexes)):
            if gg+1 < len(unitindexes):
                uwisetopics.append(n[unitindexes[gg]:unitindexes[gg+1]+1])
            else:
                uwisetopics.append(n[unitindexes[gg]:len(n)])
        print("There are ",unitcounti," units in this subject. Which one would you like to study? ")
        for ll in range (0, len(kk)):
            print(ll+1,". ",kk[ll],": ",unitname[ll])
        print("Please enter your input(1-"+str(len(kk))+"): ",end="")
        bb=int(input())
        for iii in range (1,len(kk)):
            if bb==iii:
                print("The topics for", unitname[bb-1], "are:")
                for tt in range(1, len(uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1])+1):
                    print(str(tt)+". ",uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1][tt-1])
                print("Which topic do you want to study right now?\nPlease enter your input(1-"+str(len(uwisetopics[bb-1])-3)+"): ",end="")
                topname=int(input())
                if uwisetopics[bb-1][(topname+1)] in uwisetopics[bb-1][2:len(uwisetopics[bb-1])]:
                    print("You are studying "+uwisetopics[bb-1][(topname+1)]+" right now: ")        
                    print("Starting the timer!")
                    print("You started studying at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" PM")
                    else:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" AM")
                    tracker = threading.Thread(target=windowtracker)
                    tracker.start()
                    print("Please press enter(return) as soon as you want to end your current study session, along with the timer!\n", end="")
                    aaa = input("Waiting for user input: ")
                    if aaa:
                        chiggi = False
                    timerstate = input()
                    realtime1=datetime.datetime.now().time()
                    timefake1=str(realtime1).split(":")
                    print("You ended your study session at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" PM")
                    else:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" AM")
                    print("Timer ended!")        
                    print("You studied for a total of: "+ str(abs(int(timefake1[0])-int(timefake[0])))+" hours "+str(abs(int(timefake1[1])-int(timefake[1])))+" minutes and "+str(abs(int(timefake1[2].split(".")[0])-int(timefake[2].split(".")[0])))+" seconds")
    elif b==7:
        kk=0
        k=[]
        kk=[]
        unitname=[]
        uwisetopics=[]
        unitindexes=[]
        unitcounti = 0
        n=m[b-1].split(",")
        print(n[0], "Syllabus:")
        for j in range (1 ,len(n)):
            if n[j][1]!="U":
                if n[j][2]!="n":
                    if n[j][3]!="i":
                        if n[j][4]!="t":
                            k.append(n[j])
            else:
                unitname.append(n[j+1])
                kk.append(n[j])
                unitcounti+=1
                continue
        for j in range (1 ,len(n)):
            if n[j][1]=="U":
                if n[j][2]=="n":
                    if n[j][3]=="i":
                        if n[j][4]=="t":
                            unitindexes.append(j)
        for gg in range(0, len(unitindexes)):
            if gg+1 < len(unitindexes):
                uwisetopics.append(n[unitindexes[gg]:unitindexes[gg+1]+1])
            else:
                uwisetopics.append(n[unitindexes[gg]:len(n)])
        print("There are ",unitcounti," units in this subject. Which one would you like to study? ")
        for ll in range (0, len(kk)):
            print(ll+1,". ",kk[ll],": ",unitname[ll])
        print("Please enter your input(1-"+str(len(kk))+"): ",end="")
        bb=int(input())
        for iii in range (1,len(kk)):
            if bb==iii:
                print("The topics for", unitname[bb-1], "are:")
                for tt in range(1, len(uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1])+1):
                    print(str(tt)+". ",uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1][tt-1])
                print("Which topic do you want to study right now?\nPlease enter your input(1-"+str(len(uwisetopics[bb-1])-3)+"): ",end="")
                topname=int(input())
                if uwisetopics[bb-1][(topname+1)] in uwisetopics[bb-1][2:len(uwisetopics[bb-1])]:
                    print("You are studying "+uwisetopics[bb-1][(topname+1)]+" right now: ")        
                    print("Starting the timer!")
                    print("You started studying at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" PM")
                    else:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" AM")
                    tracker = threading.Thread(target=windowtracker)
                    tracker.start()
                    print("Please press enter(return) as soon as you want to end your current study session, along with the timer!\n", end="")
                    aaa = input("Waiting for user input: ")
                    if aaa:
                        chiggi = False
                    timerstate = input()
                    realtime1=datetime.datetime.now().time()
                    timefake1=str(realtime1).split(":")
                    print("You ended your study session at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" PM")
                    else:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" AM")
                    print("Timer ended!")        
                    print("You studied for a total of: "+ str(abs(int(timefake1[0])-int(timefake[0])))+" hours "+str(abs(int(timefake1[1])-int(timefake[1])))+" minutes and "+str(abs(int(timefake1[2].split(".")[0])-int(timefake[2].split(".")[0])))+" seconds")
    elif b==8:
        kk=0
        k=[]
        kk=[]
        unitname=[]
        uwisetopics=[]
        unitindexes=[]
        unitcounti = 0
        n=m[b-1].split(",")
        print(n[0], "Syllabus:")
        for j in range (1 ,len(n)):
            if n[j][1]!="U":
                if n[j][2]!="n":
                    if n[j][3]!="i":
                        if n[j][4]!="t":
                            k.append(n[j])
            else:
                unitname.append(n[j+1])
                kk.append(n[j])
                unitcounti+=1
                continue
        for j in range (1 ,len(n)):
            if n[j][1]=="U":
                if n[j][2]=="n":
                    if n[j][3]=="i":
                        if n[j][4]=="t":
                            unitindexes.append(j)
        for gg in range(0, len(unitindexes)):
            if gg+1 < len(unitindexes):
                uwisetopics.append(n[unitindexes[gg]:unitindexes[gg+1]+1])
            else:
                uwisetopics.append(n[unitindexes[gg]:len(n)])
        print("There are ",unitcounti," units in this subject. Which one would you like to study? ")
        for ll in range (0, len(kk)):
            print(ll+1,". ",kk[ll],": ",unitname[ll])
        print("Please enter your input(1-"+str(len(kk))+"): ",end="")
        bb=int(input())
        for iii in range (1,len(kk)):
            if bb==iii:
                print("The topics for", unitname[bb-1], "are:")
                for tt in range(1, len(uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1])+1):
                    print(str(tt)+". ",uwisetopics[bb-1][2:len(uwisetopics[bb-1])-1][tt-1])
                print("Which topic do you want to study right now?\nPlease enter your input(1-"+str(len(uwisetopics[bb-1])-3)+"): ",end="")
                topname=int(input())
                if uwisetopics[bb-1][(topname+1)] in uwisetopics[bb-1][2:len(uwisetopics[bb-1])]:
                    print("You are studying "+uwisetopics[bb-1][(topname+1)]+" right now: ")        
                    print("Starting the timer!")
                    print("Starting app monitor!")
                    print("Starting browser tab monitor!")
                    print("You started studying at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" PM")
                    else:
                        print(timefake[0]+":"+timefake[1]+":"+timefake[2].split(".")[0]+" AM")
                    tracker = threading.Thread(target=windowtracker)
                    tracker.start()
                    print("Please press enter(return) as soon as you want to end your current study session, along with the timer!\n", end="")
                    aaa = input("Waiting for user input: ")
                    if aaa:
                        chiggi = False
                    realtime1=datetime.datetime.now().time()
                    timefake1=str(realtime1).split(":")
                    print("You ended your study session at: ",end="")
                    if int(timefake[0])>=12:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" PM")
                    else:
                        print(timefake1[0]+":"+timefake1[1]+":"+timefake1[2].split(".")[0]+" AM")
                    print("Timer ended!")        
                    print("You studied for a total of: "+ str(abs(int(timefake1[0])-int(timefake[0])))+" hours "+str(abs(int(timefake1[1])-int(timefake[1])))+" minutes and "+str(abs(int(timefake1[2].split(".")[0])-int(timefake[2].split(".")[0])))+" seconds")
    else:
        print("Invalid input!")
        nga = False
else:
    print("Restart the program nga!")