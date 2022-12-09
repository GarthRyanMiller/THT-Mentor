#An SMS Simulation
class SMSMessage(object):  
    
    
    hasBeenRead = False    #these three variables are initalized in _init_ its also not necessary
	messageText = text 
	fromNumber = number

	def __init__(self,hasBeenRead,messageText,fromNumber): 
		self.hasBeenRead = False
		self.messageText = text
		self.fromNumber = number
#here you are setting the type of variable when you create it such as in no_1, when you intialize the object you are setting the types such as no. You have no reference to hasBeenRead as you
#have to intialize it as such self.hasBeenRead = hasBeenRead. this is necessary so you can refer to this variable by using self.hasBeenRead.
    def MarkAsRead(self):
        if userChoice == read:
            self.hasBeenRead = True
            

    def add_sms():

    def get_count():

    def get_message():

    def get_unread_messages():

    def remove():

no_1 = SMSMessage(False, "Hello", "0798653452")
no_2 = SMSMessage(False, "WYD", "0845673864")
no_3 = SMSMessage(False, "How are you?", "0631873298")
# After you have created the object message no_1 you can refer to the methods in the class using the dot as such print(no_1.method_name())
# Alternatively you have the option to access the methods when creating the object as such SMSMessage(False, "hi", "123123").method_name()

SMSStore = []
userChoice = ""

while userChoice != "quit":
    userChoice = raw_input("What would you like to do - read/send/quit?")
    if userChoice == "read":
        #Place your logic here
    elif userChoice == "send":
        #Place your logic here
    elif userChoice == "quit":
        print ("Goodbye")
    else:
        print ("Oops - incorrect input")
