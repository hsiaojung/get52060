
import os, signal 



def showme():
    

    try: 
            
        # iterating through each instance of the proess 
        for line in os.popen("ps ax | grep " + "chrom" + " | grep -v grep"):  
            fields = line.split() 
                
            # extracting Process ID from the output 
            pid = fields[0]  
                
            # terminating process  
            os.kill(int(pid), signal.SIGKILL)  
        print("Process Successfully terminated") 
            
    except: 
        print("Error Encountered while running script")  


def processkill(): 
      
    # Ask user for the name of process 
    name = input("Enter process Name: ") 
    try: 
          
        # iterating through each instance of the proess 
        for line in os.popen("ps ax | grep " + "chrom" + " | grep -v grep"):  
            fields = line.split() 
              
            # extracting Process ID from the output 
            pid = fields[0]  
              
            # terminating process  
            os.kill(int(pid), signal.SIGKILL)  
        print("Process Successfully terminated") 
          
    except: 
        print("Error Encountered while running script") 