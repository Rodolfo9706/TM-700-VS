#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

class MoveRobotNode:
    def __init__(self):
        rospy.init_node('move_robot_node', anonymous=True)
        self.pose_publisher = rospy.Publisher('/desired_pose', PoseStamped, queue_size=10)

    def get_user_input(self):
        print("Esperando coordenadas de destino...")
        x = float(input("Ingrese la coordenada x de destino: "))
        y = float(input("Ingrese la coordenada y de destino: "))
        z = float(input("Ingrese la coordenada z de destino: "))
        return x, y, z

    def move_to_coordinates(self, x, y, z):
        print(f"Enviando robot a las coordenadas: x={x}, y={y}, z={z}")
        pose_msg = PoseStamped()
        pose_msg.header.stamp = rospy.Time.now()
        pose_msg.pose.position.x = x
        pose_msg.pose.position.y = y
        pose_msg.pose.position.z = z

        # Publicar la posición deseada
        self.pose_publisher.publish(pose_msg)

    def run(self):
        while not rospy.is_shutdown():
            x, y, z = self.get_user_input()
            self.move_to_coordinates(x, y, z)

if __name__ == '__main__':
    try:
        node = MoveRobotNode()
        node.run()
    except rospy.ROSInterruptException:
        pass
