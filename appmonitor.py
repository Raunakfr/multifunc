import psutil
def windowtracker():
    while True:
        ids = psutil.pids()
        for ida in ids:
            try:
                if(str(psutil.Process(ida)).split(",")[1][7:len(str(psutil.Process(ida)).split(",")[1])-1]) == "WinStore.App.exe":
                    killed = psutil.Process(ida)
                    killed.terminate()
            except:
                print("",end="")