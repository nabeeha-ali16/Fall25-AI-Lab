class SimpleReflexAgent:
    def __init__(self, fixed_temp):
        self.fixed_temp = fixed_temp
        self.previous_temp = None  

    def sensor(self, temp):
        self.current_temp = temp

    def performance(self):
        if self.current_temp < self.fixed_temp:
            return "Turn ON Heater"
        else:
            return "Turn OFF Heater"

    def actuator(self):
        action = self.performance()
        print(f"Previous: {self.previous_temp}, Current: {self.current_temp} = {action}")
        self.previous_temp = self.current_temp


class ModelBasedReflexAgent:
    def __init__(self, fixed_temp):
        self.fixed_temp = fixed_temp
        self.previous_action = None
        self.previous_temp = None  

    def sensor(self, temp):
        self.current_temp = temp

    def performance(self):
        if self.current_temp < self.fixed_temp:
            action = "Turn ON Heater"
        else:
            action = "Turn OFF Heater"

        if action == self.previous_action:
            return None
        self.previous_action = action
        return action

    def actuator(self):
        action = self.performance()
        if action:
            print(f"Previous: {self.previous_temp}, Current: {self.current_temp} = {action}")
        else:
            print(f"Previous: {self.previous_temp}, Current: {self.current_temp} = No change")
        self.previous_temp = self.current_temp  

rooms = {
    "Living Room": 20,
    "Drawing Room": 22,
    "Kitchen": 34,
}

print("\nSimple Reflex Agent")
simple = SimpleReflexAgent(22)
for room, temp in rooms.items():
    print(room, end=" : ")
    simple.sensor(temp)
    simple.actuator()

print("\nModel-Based Reflex Agent")
model = ModelBasedReflexAgent(22)
for room, temp in rooms.items():
    print(room, end=" : ")
    model.sensor(temp)
    model.actuator()

print("\nPrevious Temperature")
for t in [20, 23, 20, 23]:
    model.sensor(t)
    model.actuator()