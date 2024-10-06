#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

class pidCalulation:
    def __init__(self,Yaw , kp, ki, kd):
        self.desiredYaw = Yaw #desired yaw in degrees
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.time= rospy.get_time()
        self.lastError =0
        self.derivative=0
        self.integral=0

        rospy.Subscriber('/yawdata' , Float32 , self.pid_callback)


    def pid_callback(self,msg):
        currentYaw = msg.data

        error = self.desiredYaw - currentYaw

        current_time = rospy.get_time()

        dt = current_time - self.time

        self.derivative += error/dt
        integral =  


if __name__ == '__main__':
    rospy.init_node('pid_calc' , anonymous= True)

    pid = pidCalulation(90)

    rospy.spin()