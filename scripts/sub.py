#!/usr/bin/env python3

import rospy

from yolact_ros_msgs.msg import Detections
from std_msgs.msg import String


class detection:

    def __init__(self):
        self.det_sub = rospy.Subscriber("/yolact_ros/detections",
                                        Detections, self.callback)
        self.det_pub = rospy.Publisher("/trafic_light_status", String, queue_size = 10)

    def callback(self, msg):
        
        if (len(msg.detections) > 0):
            for i in range (len(msg.detections)):
                if msg.detections[i].score>0.95:
                    status = "traffic light " + msg.detections[i].class_name
                else:
                    status = "no traffic light"
                self.det_pub.publish(status)
       


def main():
    # create a subscriber instance
    sub = detection()
    
    # initializing the subscriber node
    rospy.init_node('listener', anonymous=True)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
