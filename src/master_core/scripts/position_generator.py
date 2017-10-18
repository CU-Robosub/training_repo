#!/usr/bin/env python
import termios, fcntl, sys, os
import random
import rospy
import tf
from geometry_msgs.msg import PoseWithCovarianceStamped

class Position_Gen():
    def __init__(self):
        self.pub = rospy.Publisher('/positions', PoseWithCovarianceStamped, queue_size=1)
        self.pub_Data = PoseWithCovarianceStamped()
    def pub_random(self):
        time = rospy.get_rostime()
        self.pub_Data.header.stamp.secs = time.secs
        self.pub_Data.header.stamp.nsecs = time.nsecs


        self.pub_Data.pose.pose.position.x = random.randint(1,3);
        self.pub_Data.pose.pose.position.y = random.randint(1,3);
        self.pub_Data.pose.pose.position.z = random.randint(1,3);
        quaternion = tf.transformations.quaternion_from_euler(0, 0, random.uniform(-0.78539816339,0.78539816339))
        self.pub_Data.pose.pose.orientation.x = quaternion[0]
        self.pub_Data.pose.pose.orientation.y = quaternion[1]
        self.pub_Data.pose.pose.orientation.z = quaternion[2]
        self.pub_Data.pose.pose.orientation.w = quaternion[3]
        self.pub.publish(self.pub_Data)
## Main Function
def main():
    rospy.init_node('Position_Gen')
    m = Position_Gen()
    r = rospy.Rate(10)
    while(1):
        m.pub_random()
        r.sleep()
        # rospy.spinonce()

if __name__ == "__main__":
    main()
