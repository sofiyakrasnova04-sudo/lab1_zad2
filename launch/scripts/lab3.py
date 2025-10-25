#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('params_study')
    
    # Получаем имя топика из параметра
    topic_name = rospy.get_param('~topic_name', 'default_topic')
    
    # Создаем publisher с заданным именем топика
    pub = rospy.Publisher(topic_name, String, queue_size=10)
    
    rate = rospy.Rate(1)  # 1 Hz
    counter = 0
    
    rospy.loginfo(f"Publishing to topic: {topic_name}")
    
    while not rospy.is_shutdown():
        # Публикуем сообщение
        msg = String()
        msg.data = f"Hello on topic {topic_name}! Count: {counter}"
        pub.publish(msg)
        
        rospy.loginfo(f"Published: {msg.data}")
        counter += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass