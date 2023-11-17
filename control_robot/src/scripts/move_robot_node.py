#!/usr/bin/env python3

import rospy
import sys
from std_msgs.msg import Float64
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def move_robot(joint_positions):
    rospy.init_node('move_robot_node', anonymous=True)

    # Define los nombres de las articulaciones
    joint_names = ["shoulder_1_joint", "shoulder_2_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]

    # Crea un mensaje de trayectoria
    trajectory_msg = JointTrajectory()
    trajectory_msg.joint_names = joint_names

    # Crea un punto de trayectoria
    trajectory_point = JointTrajectoryPoint()
    trajectory_point.positions = joint_positions
    trajectory_point.time_from_start = rospy.Duration(15.0)  # Ajusta según sea necesario

    # Agrega el punto a la trayectoria
    trajectory_msg.points.append(trajectory_point)

    # Publica la trayectoria en el tópico de comandos
    trajectory_pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)
    trajectory_pub.publish(trajectory_msg)

    rospy.loginfo(f"Publicando posición de la trayectoria:\n{trajectory_msg}")

    # Espera hasta que se complete la acción
    rospy.spin()

def get_user_input():
    try:
        # Solicita al usuario que ingrese las posiciones
        positions = [float(input(f"Ingrese la posición para la articulación {i + 1}: ")) for i in range(6)]
        return positions
    except ValueError:
        print("Error: Ingrese valores numéricos.")
        sys.exit(1)

if __name__ == '__main__':
    # Verifica si se proporcionaron argumentos
    if len(sys.argv) == 7:
        # Lee las posiciones deseadas desde los argumentos de la línea de comandos
        desired_positions = [float(pos) for pos in sys.argv[1:]]
    else:
        # Si no se proporcionan argumentos, obtén las posiciones del usuario
        desired_positions = get_user_input()

    # Mueve el robot a las posiciones especificadas
    move_robot(desired_positions)
