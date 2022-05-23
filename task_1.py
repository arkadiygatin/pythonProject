from time import sleep


class TrafficLight:
    __color =  "Черный"

    def running(selfself):
        while True:
            print("RED")
            sleep(7)
            print("Yellow")
            sleep(2)
            print("GREEN")
            sleep(10)
            print("Yellow")
            sleep(2)
trafficlight = TrafficLight()
trafficlight.running()

