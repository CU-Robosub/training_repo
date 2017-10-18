#!/usr/bin/env python
import termios, fcntl, sys, os
import random
import rospy
import tf
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry


class Velocity():
    #TODO Create Class
## Main Function
def main():
    rospy.init_node('Velocity')
    m = Velocity()
    rospy.spinonce()

if __name__ == "__main__":
    main()
