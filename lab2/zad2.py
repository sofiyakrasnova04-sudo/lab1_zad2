#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def overflow_callback(data):
    """
    Callback функция для обработки сообщений о переполнении
    """
    node_name = rospy.get_name()
    rospy.loginfo("🚨 [%s] OVERFLOW DETECTED: %s", node_name, data.data)

def overflow_listener():
    """
    Узел для прослушивания сообщений о переполнении счетчика
    """
    # Инициализация узла
    rospy.init_node('overflow_listener', anonymous=True)
    
    # Получение информации о узле для логирования
    node_name = rospy.get_name()
    namespace = rospy.get_namespace()
    
    # Подписка на топик переполнения
    rospy.Subscriber('overflow_topic', String, overflow_callback)
    
    rospy.loginfo("Overflow listener %s started in namespace %s. Waiting for overflow messages...", 
                  node_name, namespace)
    
    # Бесконечный цикл ожидания сообщений
    rospy.spin()

if __name__ == '__main__':
    try:
        overflow_listener()
    except rospy.ROSInterruptException:
        rospy.logerr("ROS interrupt exception")
    except KeyboardInterrupt:
        rospy.loginfo("Overflow listener stopped by user")