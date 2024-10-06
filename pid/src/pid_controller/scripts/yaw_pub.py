#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion
import math

class GetYaw :
    def __init__(self):

        self.yaw_publisher = rospy.Publisher('/yawdata' , Float32 , queue_size=10)
        rospy.Subscriber('/imu' , Imu , self.imu_callback)
        self.currentYaw = 0.0

    def imu_callback(self,msg): # msg-> x y z w
        quat = (msg.orientation.x , msg.orientation.y , msg.orientation.z , msg.orientation.w)
        eulerDegrees = euler_from_quaternion(quat) #euler now will be a tuple (roll, pitch, yaw) angles in radian
        self.currentYaw = eulerDegrees[2]

        self.yaw_publisher.publish( math.degrees(self.currentYaw) )

if __name__ == '__main__':
    rospy.init_node('yaw_pub' , anonymous= True)

    yaw = GetYaw()

    rospy.spin()





