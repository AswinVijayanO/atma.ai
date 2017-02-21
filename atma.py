import sys, glob
import aiml
import os
import datetime
def appopen( str ):
 os.system(" cd /usr/share/applications && find -iname '*"+str+"*'>op.txt" )
 fil = open("/usr/share/applications/op.txt","r") 
 str = fil.read() 
 s=str.replace("./","")
 s=s.replace("\n","")
 print(str)
 fil2= open("/usr/share/applications/"+s,"r")
 for line in fil2:
    if "Exec=" in line: 
      st=line.split('=', 1)[1]
      st=st.split(' ', 1)[0]
      print(st)
 os.system("espeak -ven-us+f1  ' opening "+str+"'")
 os.system(st)     
 return st
sessionId = 12345
kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")
sessionData = kernel.getSessionData(sessionId)
kernel.setPredicate("name", "Aswin", sessionId)
kernel.setBotPredicate("name","Atma")
kernel.setBotPredicate("age","20")
kernel.setBotPredicate("home","this pc")
kernel.setBotPredicate("master","Aswin")
kernel.setBotPredicate("client_name","Aswin")
kernel.setBotPredicate("hometown", "calicut")
kernel.learn("botai/bot-startup.xml")
kernel.learn("botai/ai.aiml")
kernel.learn("botai/AI.aiml")
kernel.learn("botai/alice.aiml")
kernel.learn("botai/ALICE.aiml")
kernel.learn("botai/astrology.aiml")
kernel.learn("botai/Astrology.aiml")
kernel.learn("botai/atomic.aiml")
kernel.learn("botai/badanswer.aiml")
kernel.learn("botai/Badanswer.aiml")
kernel.learn("botai/basic_chat.aiml")
kernel.learn("botai/biography.aiml")
kernel.learn("botai/bot.aiml")
kernel.learn("botai/bot_profile.aiml")
kernel.learn("botai/client.aiml")
kernel.learn("botai/client_profile.aiml")
kernel.learn("botai/computers.aiml")
kernel.learn("botai/continuation.aiml")
kernel.learn("botai/date.aiml")
kernel.learn("botai/default.aiml")
kernel.learn("botai/drugs.aiml")
kernel.learn("botai/emotion.aiml")
kernel.learn("botai/Emotion.aiml")
kernel.learn("botai/food.aiml")
kernel.learn("botai/geography.aiml")
kernel.learn("botai/gossip.aiml")
kernel.learn("botai/history.aiml")
kernel.learn("botai/humor.aiml")
kernel.learn("botai/imponderables.aiml")
kernel.learn("botai/inquiry.aiml")
kernel.learn("botai/interjection.aiml")
kernel.learn("botai/iu.aiml")
kernel.learn("botai/knowledge.aiml")
kernel.learn("botai/literature.aiml")
kernel.learn("botai/loebner10.aiml")
kernel.learn("botai/money.aiml")
kernel.learn("botai/movies.aiml")
kernel.learn("botai/mp0.aiml")
kernel.learn("botai/mp1.aiml")
kernel.learn("botai/mp2.aiml")
kernel.learn("botai/mp3.aiml")
kernel.learn("botai/mp4.aiml")
kernel.learn("botai/mp5.aiml")
kernel.learn("botai/mp6.aiml")
kernel.learn("botai/music.aiml")
kernel.learn("botai/numbers.aiml")
kernel.learn("botai/personality.aiml")
kernel.learn("botai/phone.aiml")
kernel.learn("botai/pickup.aiml")
kernel.learn("botai/politics.aiml")
kernel.learn("botai/primeminister.aiml")
kernel.learn("botai/primitive-math.aiml")
kernel.learn("botai/psychology.aiml")
kernel.learn("botai/pyschology.aiml")
kernel.learn("botai/reduction0.safe.aiml")
kernel.learn("botai/reduction1.safe.aiml")
kernel.learn("botai/reduction2.safe.aiml")
kernel.learn("botai/reduction3.safe.aiml")
kernel.learn("botai/reduction4.safe.aiml")
kernel.learn("botai/reduction.names.aiml")
kernel.learn("botai/reductions-update.aiml")
kernel.learn("botai/religion.aiml")
kernel.learn("botai/salutations.aiml")
kernel.learn("botai/science.aiml")
kernel.learn("botai/sex.aiml")
kernel.learn("botai/sports.aiml")
kernel.learn("botai/stack.aiml")
kernel.learn("botai/stories.aiml")
kernel.learn("botai/that.aiml")
kernel.learn("botai/update1.aiml")
kernel.learn("botai/update_mccormick.aiml")
kernel.learn("botai/wallace.aiml")
kernel.learn("botai/xfind.aiml")
kernel.learn("botai/gen.aiml")
kernel.learn("botai/wordplay.aiml")
kernel.respond("LOAD AIML B")
print ("\nHi im atma")
now = datetime.datetime.now()
if now.hour>21:
 tim = "good night"
elif now.hour>=18:
 tim = "good evening"
elif now.hour>12:
 tim = "good afternoon"
else:
 tim = "good morning!"
print(tim)
os.system("espeak -ven-us+f2  'Hi im atma"+tim+"'")
while True:
 #print(kernel.respond(str(input("> "))))
 s=input("> ")
 st=s.split(' ', 1)[0]
 if s in  {"good bye","bye bye","good night","bye","good night","sleep"}:
  exit()
 elif s in {"save it","learn that","remember that"}:
  kernel.saveBrain("bot_brain.brn")
 elif st== "open":
  st=s.split(' ', 1)[1]
  appopen(st)
 else:
  st = kernel.respond(str(s),sessionId)
 print(st)
 st = st.replace("'", "")
 os.system("espeak -ven-us+f1  '"+st+"'")

    
     


