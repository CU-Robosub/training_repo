#!/usr/bin/env python
import termios, fcntl, sys, os
import random
import rospy
from std_msgs.msg import Float64

class Number_Gen():
    def __init__(self):
        self.pub = rospy.Publisher('/numbers', Float64, queue_size=1)
    def pub_random(self):
        self.pub.publish(random.randint(1,101))
## Main Function
def main():
    rospy.init_node('Number_Gen')
    m = Number_Gen()
    r = rospy.Rate(20)
    while(1):
        m.pub_random()
        r.sleep()
        # rospy.spinonce()

if __name__ == "__main__":
    main()
