#!/usr/bin/env python3

# Import Dependencies
import rospy 
from geometry_msgs.msg import Twist 
import time 

def move_turtle_square(): 
    rospy.init_node('turtlesim_square_node', anonymous=True)
    
    # Init publisher
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) 
    rospy.loginfo("Turtles are great at drawing squares!")

    move_forward = Twist()
    move_forward.linear.x = 1

    turn_left = Twist()
    turn_left.linear.y = 1

    move_backward = Twist()
    move_backward.linear.x = -1

    turn_right = Twist()
    turn_right.linear.y = -1

    while True:
        drawSquare(velocity_publisher, move_forward, turn_left, move_backward, turn_right)


def drawSquare(velocity_publisher, forward, left, backward, right):
    move(velocity_publisher, forward)

    move(velocity_publisher, left)

    move(velocity_publisher, backward)

    move(velocity_publisher, right)
    
def move(velocity_publisher, moveHere):
    velocity_publisher.publish(moveHere)
    time.sleep(1)
    velocity_publisher.publish(Twist())

if name == 'main': 

    try: 
        move_turtle_square() 
    except rospy.ROSInterruptException: 
        pass
