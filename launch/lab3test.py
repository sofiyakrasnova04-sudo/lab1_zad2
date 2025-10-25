#!/usr/bin/env python3
import rospy

rospy.init_node('lab3')

# Получение параметров со значениями по умолчанию
distro = rospy.get_param('/rosdistro')
my_set_param = rospy.get_param('my_set', 'default_value')  # значение по умолчанию
my_private_param = rospy.get_param('~private_param', 'default_private_value')  # значение по умолчанию

# Установка параметров с явными полными путями
rospy.set_param('/sample_ns/params_study/ros_priv_param', 'Hi, I am private =)')
rospy.set_param('/sample_ns/ros_loc_param', 'Hi, I am local =)')
rospy.set_param('/ros_glob_param', 'Hi, I am global =)')

rospy.loginfo("Parameters set successfully!")
rospy.loginfo(f"ROS distro: {distro}")
rospy.loginfo(f"My set param: {my_set_param}")
rospy.loginfo(f"My private param: {my_private_param}")

# Выведем созданные параметры для проверки
rospy.sleep(1)  # Даем время параметрам установиться

print("\nCreated parameters:")
for param_name in rospy.get_param_names():
    if 'sample_ns' in param_name or 'ros_glob' in param_name:
        value = rospy.get_param(param_name)
        print(f"  {param_name} = {value}")

# Оставим узел работать некоторое время
rospy.sleep(5)