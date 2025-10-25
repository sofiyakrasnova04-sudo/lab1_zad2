#!/usr/bin/env python3
import rospy

def main():
    rospy.init_node('params_study')
    
    # Установка параметров как в задании
    rospy.set_param('~ros_priv_param', 'Hi, I am private =)')
    rospy.set_param('ros_loc_param', 'Hi, I am local =)') 
    rospy.set_param('/ros_glob_param', 'Hi, I am global =)')
    
    rospy.loginfo("✅ All parameters set successfully!")
    
    # Демонстрация работы с параметрами
    rate = rospy.Rate(1)
    counter = 0
    
    while not rospy.is_shutdown() and counter < 3:
        # Показываем текущие значения
        priv_val = rospy.get_param('~ros_priv_param')
        loc_val = rospy.get_param('ros_loc_param')
        glob_val = rospy.get_param('/ros_glob_param')
        
        rospy.loginfo(f"Private: {priv_val}, Local: {loc_val}, Global: {glob_val}")
        
        counter += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass