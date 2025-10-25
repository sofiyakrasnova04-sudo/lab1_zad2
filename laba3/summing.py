#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

class Summing:
    def __init__(self):
        rospy.init_node('summing_node')
        
        # Переменная для хранения суммы
        self.total_sum = 0.0
        
        # Подписываемся на результаты от Polynominal
        self.poly_sub = rospy.Subscriber('polynominal_result_topic', Float32, self.poly_callback)
        
        # Публикуем финальный результат
        self.final_pub = rospy.Publisher('final_result_topic', Float32, queue_size=10)
        
        rospy.loginfo("Summing node started")
        
    def poly_callback(self, msg):
        # Получаем результат от Polynominal
        poly_result = msg.data
        
        # Суммируем (в данном случае просто передаем, так как у нас один запрос)
        # Но оставляем структуру для возможного расширения
        self.total_sum = poly_result
        
        rospy.loginfo("Summing: received result %.1f, total = %.1f", poly_result, self.total_sum)
        
        # Публикуем финальный результат
        final_msg = Float32()
        final_msg.data = self.total_sum
        self.final_pub.publish(final_msg)
        
    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = Summing()
    node.run()