import rclpy
from rclpy.node import Node
import sys

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class NinjaTurtle(Node):
    def __init__(self, linear_vel, angular_vel):
        super().__init__('ninja_turtle')

        self.linear_vel = linear_vel
        self.angular_vel = angular_vel

        self.vel_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.timer = self.create_timer(0.1, self.move_callback)
        
    def pose_callback(self, pose):
        self.get_logger().info(f"Pose received {pose}")
        
    def move_callback(self):
        vel_msg = Twist()
        vel_msg.linear.x = self.linear_vel
        vel_msg.angular.z = self.angular_vel
        self.vel_publisher.publish(vel_msg)
        

def main():
    rclpy.init()

    param_linear = 0.2  # m/s
    param_angular = 0.0 # rad/s
    
    if len(sys.argv) == 3:
        param_linear = sys.argv[1]
        param_angular = sys.argv[2]
        print(f"Requested linear and angular velocities: {param_linear}, {param_angular}")
    else:
        print("Not all parameters were set, working with default linear and angular velocities")
    
    ninja = NinjaTurtle(param_linear, param_angular)
    rclpy.spin(ninja)


if __name__ == '__main__':
    main()
