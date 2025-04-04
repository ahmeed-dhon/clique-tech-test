import logging
import random
import time

def print_log(entry):
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler("./service_log/log_file.log")
    formatter = logging.Formatter(
        "%(asctime)s : %(name)s  : %(funcName)s : %(levelname)s : %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.critical("Fatal error occured. Cannot continue. Log delay time " + str(second) + " second")

while True:
    mylist = [1,2,3,4,5,10,20,30,60,120,180,240,300,360]
    second = random.choice(mylist)
    # print(second)
    print_log(second)
    time.sleep(second)
