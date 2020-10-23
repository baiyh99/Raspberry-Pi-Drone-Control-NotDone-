import os 
import time 
os.system ("sudo pigpiod")
time.sleep(1)
import pigpio

m1=3 #front left
m2=4 #front right
m3=5 #back left
m4=6 #back right

pi = pigpio.pi();
pi.set_servo_pulsewidth(m1, 0) 
pi.set_servo_pulsewidth(m2, 0)
pi.set_servo_pulsewidth(m3, 0)
pi.set_servo_pulsewidth(m4, 0) 


max_value = 2000 #change this if your ESC's max value is different or leave it be
min_value = 700  #change this if your ESC's min value is different or leave it be


def setPulseWidth(pw):
    pi.set_servo_pulsewidth(m1, pw) 
    pi.set_servo_pulsewidth(m2, pw)
    pi.set_servo_pulsewidth(m3, pw)
    pi.set_servo_pulsewidth(m4, pw)

def getPulseWidth():
    a = pi.get_servo_pulsewidth(m1, pw) 
    b = pi.get_servo_pulsewidth(m2, pw)
    c = pi.get_servo_pulsewidth(m3, pw)
    d = pi.get_servo_pulsewidth(m4, pw)
    pwlist = [a,b,c,d]
    return pwlist

def getMinPW():
    a = pi.get_servo_pulsewidth(m1, pw) 
    b = pi.get_servo_pulsewidth(m2, pw)
    c = pi.get_servo_pulsewidth(m3, pw)
    d = pi.get_servo_pulsewidth(m4, pw)
    return min(a,b,c,d)
    
               
def control(): 
    print "I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'"
    time.sleep(1)
    takeoff_status = 0
    while True:
        pi.set_servo_pulsewidth(ESC, 0)
        inp = raw_input()
        if inp == "takeoff":
            if takeoff_status == 1:
                print "the drone is already took off"
            else:
                takeoff()
                takeoff_status = 1

                 if inp == "L":    
                    goL()
                elif inp == "R":
                    goR()
                elif inp == "U":
                    goU()
                elif inp == "D":
                    goD()
                elif inp == "F":
                    goF()
                elif inp == "B":
                    goB()
                elif inp == "land":
                    land()
                    takeoff_status = 0
                elif inp == "manual":
                    manual_drive()
                    break
                        elif inp == "arm":
                                arm()
                                break	
                else:
                    print "Wrong inputs"

        else:
            print "The drone is not taking off yet."
            
def arm(): 
    print "Connect the battery and press Enter"
    inp = raw_input()    
    if inp == '':
        setPulseWidth(0)
        time.sleep(1)
        setPulseWidth(max_value)
        time.sleep(1)
        setPulseWidth(min_value)
        time.sleep(1)
        control()

#6 direction control
def takeoff():
    setPulseWidth(1500)
    
def hover():
    setPulseWidth(getMinPW())
    
def goU():
    setPulseWidth(1600)

def goD():
    setPulseWidth(1200)

def goF():
    pi.set_servo_pulsewidth(m3, 1600)
    pi.set_servo_pulsewidth(m4, 1600)
    print(getPulseWidth())

def goB():
    pi.set_servo_pulsewidth(m1, 1600)
    pi.set_servo_pulsewidth(m2, 1600)
    print(getPulseWidth())
    
def goL():
    pi.set_servo_pulsewidth(m2, 1600)
    pi.set_servo_pulsewidth(m4, 1600)
    print(getPulseWidth())
    
def goL():
    pi.set_servo_pulsewidth(m1, 1600)
    pi.set_servo_pulsewidth(m3, 1600) 
    print(getPulseWidth())

def land():
    stop()
#-----------------------------------
def calibrate():
    pi.set_servo_pulsewidth(m1, 0) 
    pi.set_servo_pulsewidth(m2, 0)
    pi.set_servo_pulsewidth(m3, 0)
    pi.set_servo_pulsewidth(m4, 0)
    print("Disconnect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = raw_input()
        if inp == '':            
            setPulseWidth(0)
            print "Wierd eh! Special tone"
            time.sleep(7)
            print "Wait for it ...."
            time.sleep (5)
            print "Im working on it, DONT WORRY JUST WAIT....."
            setPulseWidth(0)
            time.sleep(2)
            print "Arming ESC now..."
            setPulseWidth(min_value)
            time.sleep(1)
            print "See.... uhhhhh"
            control() # You can change this to any other function you want
#-----------------------------------
def stop():
    setPulseWidth(0)
    pi.stop()

#--------------------------------------------------
inp = raw_input()
if inp == "manual":
    manual_drive()
elif inp == "calibrate":
    calibrate()
elif inp == "arm":
    arm()
elif inp == "control":
    control()
elif inp == "stop":
    stop()
else :
    print "Wrong Input"
