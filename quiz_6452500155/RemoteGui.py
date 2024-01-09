#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

# Parameter for Defult Scale
#
#
point1 = "forward"
point2 = "backward"
point3 = "turnleft"
point4 = "turnright"

frame = Tk()
frame.title("REMOTE")
frame.geometry("200x300")

# Initial ROS node and determine Publish or Subscribe action
rospy.init_node("Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)
pub1 = rospy.Publisher("std_msgs/String",String, queue_size=10)

def fw():
    print("forward")
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z= 0.0
    pub.publish(cmd)
    cmd1 = String(point1)
    pub1.publish(cmd1)
   #publish
        
def bw():
    print("backward")
    cmd = Twist()
    cmd.linear.x = -LinearVel.get()
    cmd.angular.z= 0.0
    pub.publish(cmd)
    cmd1 = String(point2)
    pub1.publish(cmd1)
   #publish
       
def lt():
    print("turnleft")
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z= AngularVel.get()
    pub.publish(cmd)
    cmd1 = String(point3)
    pub1.publish(cmd1)
   #publish
   
def rt():
    print("turnright")
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z= -AngularVel.get()
    pub.publish(cmd)
    cmd1 = String(point4)
    pub1.publish(cmd1)
    #publish
    
LinearVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
LinearVel.set(1) # 1 is defult value for scale
LinearVel.pack()

AngularVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
AngularVel.set(1) # 1 is defult value for scale
AngularVel.pack()

B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=120)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=230)

B3 = Button(text = "LT", command=lt)
B3.place(x=20, y=180)

B4 = Button(text = "RT", command=rt)
B4.place(x=128, y=180)

frame.mainloop()    
    
    
    
