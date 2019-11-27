import rospy
from std_msgs.msg import String

state = 0

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard: %s", data.data)

# def listen():
#     rospy.init_node('listener', anonymous = True)
#     message = rospy.Subscriber("hotword_detection",String, callback)
#     ####
#     #process
#     ####
#     print(message)
#     rospy.spin()
#
# def talk():
#     rospy.init_node('talker',anonymous = True)
#     pub = rospy.Publisher('abc', String, queue_size=10)
#     rate = rospy.Rate(10)
#
#     while not rospy.is_shutdown():
#         pub.publish(ABC)
#         rate.sleep()

def process():
    global state
    rospy.init_node('listener', anonymous = True)
    message = rospy.Subscriber("hotword_detection",String, callback)
    pub = rospy.Publisher('Talker', String, queue_size=10)

    print(message)

    ###process
    if message == "hotword_detection1":#Graby
        state = 1
        print(state)
    elif message == "hotword_detection2" and state == 1:
        state = 2
        print(state)
    ###
    print(state)

    pub.publish(state)#_modified)

    rospy.spin()


if __name__ == '__main__':
    process()
