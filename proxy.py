import time

class Producer:
    """ Define the 'resource-intensive' object to instantiate"""
    def produce(self):
        print("producer is working hard!")

    def meet(self):
        print("producer has time to meet you now!")

class Proxy:
    """Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if a producer is available ..."""
        print("Artist checking if producer is availbale ...")

        if self.occupied == "No":
            # if the producer is available, create a producer object
            self.producer = Producer()
            time.sleep(2)
            # make the producer meet the guest
            self.producer.meet()
        else:
            # otherwise don't instantiate a producer
            time.sleep(2)
            print("producer is busy")

# instantiate a proxy
p = Proxy()

# make the proxy: artist produce until producer is available
p.produce()

# change the state to occupied
p.occupied = "Yes"

# make the producer produce
p.produce()
