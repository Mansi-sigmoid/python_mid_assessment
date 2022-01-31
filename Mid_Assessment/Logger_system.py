logger_system = {}
output = []

class Logger:

    def shouldPrintMessage(self, timestamp, message):
        if message in logger_system.keys():
            if logger_system[message]+10<=timestamp:
                output.append("True")
                logger_system[message]=timestamp
            else:
                output.append("False")
        else:
            logger_system[message]=timestamp
            output.append("True")

logger = Logger()
prompt="How many messages are there? "
testcases=int(input(prompt))

while testcases>0:
    time=int(input("Time: "))
    msg=input("Message: ")
    logger.shouldPrintMessage(time,msg)
    testcases=testcases-1;

for o in output:
    print(o)
