#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray, Float32

class Polynominal:
    def __init__(self):
        rospy.init_node('polynominal_node')
        
        # Подписываемся на топик с запросами
        self.request_sub = rospy.Subscriber('request_topic', Float32MultiArray, self.request_callback)
        
        # Публикуем результаты вычислений
        self.result_pub = rospy.Publisher('polynominal_result_topic', Float32, queue_size=10)
        
        rospy.loginfo("Polynominal node started")
        
    def request_callback(self, msg):
        # Получаем три числа из сообщения
        numbers = msg.data
        if len(numbers) != 3:
            rospy.logwarn("Expected 3 numbers, got %d", len(numbers))
            return
            
        a, b, c = numbers
        
        # Вычисляем полином: a^3 + b^2 + c^1
        result = a**3 + b**2 + c
        
        rospy.loginfo("Polynominal: %.1f^3 + %.1f^2 + %.1f = %.1f", a, b, c, result)
        
        # Публикуем результат
        result_msg = Float32()
        result_msg.data = result
        self.result_pub.publish(result_msg)
        
    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = Polynominal()
    node.run()