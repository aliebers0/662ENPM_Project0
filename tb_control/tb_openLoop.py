#!/usr/bin/env python3
# using the following for referance:
# https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

# publisher for the velocity
class TbControl(Node):
    def __init__(self):
        super().__init__('tb_control_pub')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer_int = 0.2
        self.timer = self.create_timer(self.timer_int, self.vel_pub)
        self.i = 0
        self.a = 0.5
        self.vel_now = 0.0

    def vel_pub(self):
        msg = Twist()
        self.i += 1

        # SCENARIO 1
        # x = v*t + x0
        # 4s at constant velocity +0.25, ending coordinate should be (x0 + 1.0, 0)

        # if(self.i > 20):
        #    msg.linear.x = 0.0
        # else:
        #    msg.linear.x = 0.25
        # self.pub.publish(msg)
        # self.get_logger().info('Publishing: "%s"' % msg.linear.x)
        ####################################################################################

        # SCENARIO 2 
        # constant +acceleration -> constant velocity -> constant -acceleration
        # (0,0) to ()
    
        if(self.i < 10):
            # +acceleration for 2s
            self.vel_now += self.a*self.timer_int
        elif(self.i >= 20 and self.i < 30):
            # -acceleration for 2s
            self.vel_now -= self.a*self.timer_int
        elif(self.i >= 30):
            self.vel_now = 0.0
        msg.linear.x = self.vel_now
        ####################################################################################

        self.pub.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.linear.x)

def main(args=None):
    print('Hi from tb_control.')

    rclpy.init(args=args)

    tb_control = TbControl()
    rclpy.spin(tb_control)

    tb_control.destroy_node()
    rcply.shutdown()

if __name__ == '__main__':
    main()
