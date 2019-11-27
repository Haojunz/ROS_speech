import rospy
from std_msgs.msg import String

state = 0
message = "global"
pub = rospy.Publisher('output', String, queue_size=10)

def callback(data):
    global state
    global message
    # global pub
    rospy.loginfo(rospy.get_caller_id() + "I heard: %s", data.data)

    message = data.data

    print('message: ')
    print(message)

    ###process
    if message == 'hotword_detection1' and state == 0:#Graby
        state = 1
        print('state1 entered')
    elif message == 'hotword_detection2' and state == 1:
        state = 2
        print('state2 entered')
    ###
    print('state: ')
    print(state)

    pub.publish(str(state))

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
    rospy.init_node('listener', anonymous = True)
    rospy.init_node('Talker', anonymous = True)
    message = rospy.Subscriber("hotword_detection",String, callback)

    pub.publish(str(state))

    rospy.spin()


if __name__ == '__main__':
    process()
