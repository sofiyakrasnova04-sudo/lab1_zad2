#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def overflow_callback(data):
    """
    Callback функция для обработки сообщений о переполнении
    """
    rospy.loginfo("🚨 OVERFLOW DETECTED: %s", data.data)
    
    # Можно добавить дополнительную логику, например:
    # - Сохранение в файл
    # - Отправка уведомления
    # - Запуск другого процесса

def overflow_listener():
    """
    Узел для прослушивания сообщений о переполнении счетчика
    """
    # Инициализация узла
    rospy.init_node('overflow_listener', anonymous=True)
    
    # Подписка на топик переполнения
    rospy.Subscriber('overflow_topic', String, overflow_callback)
    
    rospy.loginfo("Overflow listener started. Waiting for overflow messages...")
    
    # Бесконечный цикл ожидания сообщений
    rospy.spin()

if __name__ == '__main__':
    try:
        overflow_listener()
    except rospy.ROSInterruptException:
        rospy.logerr("ROS interrupt exception")
    except KeyboardInterrupt:
        rospy.loginfo("Overflow listener stopped by user")