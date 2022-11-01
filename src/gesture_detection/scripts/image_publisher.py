#!/home/pumid/Desktop/athome/bin/python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2 as cv 
from cv_bridge import CvBridge
 
class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Image, '/camera/color/image_raw', 10)
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.cap = cv.VideoCapture(0)
        self.br = CvBridge()
        
    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            msg = self.br.cv2_to_imgmsg(frame)
            self.publisher_.publish(msg)
            
        self.get_logger().info('Publishing video frame')
  
def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()
  
if __name__ == '__main__':
    main()

