import datetime
import androidhelper as android

def speak(str):
    droid=android.Android ()
    droid.ttsSpeak (str)
    print (str)
    
def greed (n):
    if n<12:
        speak (" Goood morning ")
    elif n<18:
        speak (" Good evening ")
    
    elif n <24:
        speak (" Good Night ")
    
    else:
        speak (" Greed function have some error")

date=datetime.datetime.now ()
time=date.strftime ('%T')


# Replacing ":" from time to make it intiger.
ti=time.replace (":"," ")
tim=ti.replace (" ","")
ntime=int (tim[0:2])

#Greeding the user
greed(ntime)

#ladder for specific performance
if ntime<=11:
    speak ("Didn't you attend your collage")
    speak ("Though you should do some codding stuff like self help .")

elif ntime <=12:
    speak (" Time to prepare for your presentation , make slides ")
    
elif ntime <=13:
    speak ("Had you made your slide")
    speak ("You can make your slid a bit more of time")
    
elif ntime<=14:
    speak ("Time to do your collage stuff \n learn mathmatics")
    
elif ntime <=16:
    speak ("Now it's about time to start your works \n go to grind some rice and stuffs")
    
elif ntime <=17:
    speak ("Get ready to go for runnning and remember nobody knows what you doing so don't care about their thoughts ")
    
elif ntime <=19:
    speak ("Learn your collage stuffs it worth it")
    speak ("If you are welling to going with your sister")
    
elif ntime <=21:
    speak ("Time to do some good stuffs like drawing ,coding, watch worthy videos, not other bullshits")

elif ntime>22:
    speak ("Its your bedtime. You need to get some rest")
    
else:
    speak ("WHAT THE FUCK ! happend ?")
       

   



    