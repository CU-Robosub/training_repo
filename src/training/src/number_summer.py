#!/usr/bin/env python
import termios, fcntl, sys, os
import random
import rospy
from std_msgs.msg import Float64

class Number_Sum():
    def __init__(self):
        self.sub = rospy.Subscriber('/numbers', Float64, self.sum, queue_size=1)
        self.pub = rospy.Publisher('/summed_numbers', Float64, queue_size=1)

    def sum(self,msg):
        #TODO Sum numbers and publish

## Main Function
def main():
    rospy.init_node('Number_Sum')
    m = Number_Sum()
    rospy.spinonce()

if __name__ == "__main__":
    main()
