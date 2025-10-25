#!/usr/bin/env python3
import rospy

def main():
    rospy.init_node('another_node')
    topic_name = rospy.get_param('~topic_name', 'default_topic')
    
    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        rospy.loginfo("Топик в another_one.launch: %s", topic_name)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass