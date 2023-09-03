#!/usr/bin/env python3
  
import rospy
# in this example we try to obtain linear
# and angular velocity related information.
# So we import Twist
from std_msgs.msg import StringStamped
  
  
class basic_subscriber:
  
    def __init__(self):
        # initialize the subscriber node now.
        # here we deal with messages of type Twist()
        self.image_sub = rospy.Subscriber("yolact_ros/detections", 
                                          Twist, self.callback)
        print("Initializing the instance!")
  
    def callback(self, Float):
        
        # now simply display what
        # you've received from the topic
        rospy.loginfo(rospy.get_caller_id() + "The velocities are %s",
                      Twist)
        print('Callback executed!')
  
  
def main():
    # create a subscriber instance
    sub = basic_subscriber()
      
    # follow it up with a no-brainer sequence check
    print('Currently in the main function...')
      
    # initializing the subscriber node
    rospy.init_node('listener', anonymous=True)
    rospy.spin()
  
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass