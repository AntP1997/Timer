
import sys
import os
import time
#ClearSystem ="clear"
ClearSystem = "cls"
def programEnd():
   
   return 0
os.system(ClearSystem)
def timer():
 
 
  timeSMH=input("Please enter seconds, minutes, hours  \n")
  
  timeN=int(input("Please enter the number you want for seconds minutes hours   \n"))
  
  S = -1
  M= -1
  H = -1
  if timeSMH == "seconds":
   
      if timeN < 60:
      
         S = timeN
         
         
      else:
        
          print("you have to enter a number less than 60\n")  
          print("Please enter a number less than 60\n")
          timer()
          
  elif timeSMH == "minutes":
   
        if timeN < 60:
          
           M = timeN
           print(M,"hellp")
        else:
          
          print("you have to enter a number less than 60\n")  
          print("Please enter a number less than 60\n")
          timer()
          
  elif timeSMH == "hours":
   
      if timeN < 60:
   
         H = timeN
         
      else:
   
       print("you have to enter a number less than 60\n")  
       print("Please enter a number less than 60\n")
       timer()     
      
  else:
  
     print("you did enter the right command \n")
  
     timer()
      

  count =True
  seconds = 0
  minutes = 0
  hours = 0
  while count:
    
    
    
    for x in range(0,60):
       os.system(ClearSystem) 
       print("hours = ", hours,"|minutes = ",minutes,"| seconds = ", seconds,"\n ")
       print("Timer will stop in ",timeN," ",timeSMH,"\n")       
       time.sleep(1)    
       seconds +=1 
       
       if seconds == 60:
          seconds =0
          minutes += 1
       elif minutes == 60:
           minutes = 0
           hours+= 1
       elif hours == 60:
           hours = 0               
       if seconds == S :
         
         os.system(ClearSystem)
         print("hours = ", hours,"|minutes = ",minutes,"| seconds = ", seconds,"\n") 
         time.sleep(1)
         print("time is up")
         print("Timer has reach \a",timeN," ",timeSMH)
         count = False
         break
         programEnd()
        
         
       if minutes == M:
          os.system(ClearSystem)
          print("hours = ", hours,"|minutes = ",minutes,"| seconds = ", seconds,"\n") 
          time.sleep(1)
          print("time is up")   
          print("Timer has reach \a",timeN," ",timeSMH)
          count= False
          break
          programEnd()

       elif hours == H:
         os.system(ClearSystem)
         print("hours = ", hours,"|minutes = ",minutes,"| seconds = ", seconds,"\n") 
         time.sleep(1)
         print("time is up")
         print("Timer has reach \a",timeN," ",timeSMH)
         count= False
         break 
         programEnd()
         
if __name__ == "__main__":
   
   timer()
   