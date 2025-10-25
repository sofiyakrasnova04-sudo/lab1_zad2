#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import Float32MultiArray, Float32

class Request:
    def __init__(self):
        rospy.init_node('request_node')
        
        # Флаг для ожидания ответа
        self.response_received = False
        self.final_result = None
        
        # Публикуем запрос
        self.request_pub = rospy.Publisher('request_topic', Float32MultiArray, queue_size=10)
        
        # Подписываемся на финальный результат
        self.final_sub = rospy.Subscriber('final_result_topic', Float32, self.final_callback)
        
        # Ждем немного для установки соединений
        rospy.sleep(1)
        
    def final_callback(self, msg):
        # Получаем финальный результат
        self.final_result = msg.data
        self.response_received = True
        rospy.loginfo("Request: received final result: %.1f", self.final_result)
        
    def send_request(self, a, b, c):
        # Создаем сообщение с тремя числами
        request_msg = Float32MultiArray()
        request_msg.data = [float(a), float(b), float(c)]
        
        rospy.loginfo("Request: sending numbers: %.1f, %.1f, %.1f", a, b, c)
        
        # Публикуем запрос
        self.request_pub.publish(request_msg)
        
        # Ждем ответа (таймаут 5 секунд)
        timeout = rospy.Time.now() + rospy.Duration(5)
        while not self.response_received and rospy.Time.now() < timeout:
            rospy.sleep(0.1)
            
        if self.response_received:
            return self.final_result
        else:
            rospy.logwarn("Request: timeout waiting for response")
            return None

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: rosrun study_pkg request.py <a> <b> <c>")
        sys.exit(1)
        
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
        
        node = Request()
        result = node.send_request(a, b, c)
        
        if result is not None:
            print(f"Final result: {result}")
        else:
            print("Failed to get result")
            sys.exit(1)
            
    except ValueError:
        print("Error: All arguments must be numbers")
        sys.exit(1)
    except rospy.ROSInterruptException:
        pass