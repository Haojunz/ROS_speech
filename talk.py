import rospy
from std_msgs.msg import String

def talk():
    rospy.init_node('talker',anonymous = True)
    pub = rospy.Publisher('abc', String, queue_size=10)
    rate = rospy.Rate(5)
    ABC = "test"

    while not rospy.is_shutdown():
        pub.publish(ABC)
        rate.sleep()

if __name__ == '__main__':
    talk()
