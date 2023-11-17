cmake_minimum_required(VERSION 3.0.2)
project(control_robot)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  trajectory_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy std_msgs  trajectory_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Añade la ejecución de Python
catkin_install_python(PROGRAMS
  src/scripts/move_robot_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

