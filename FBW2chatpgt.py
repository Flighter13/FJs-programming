class FighterJet:

    def __init__(self):
        self.throttle = 0
        self.elevator = 0
        self.ailerons = 0
        self.rudder = 0

    def set_throttle(self, throttle):
        self.throttle = throttle

    def set_elevator(self, elevator):
        self.elevator = elevator

    def set_ailerons(self, ailerons):
        self.ailerons = ailerons

    def set_rudder(self, rudder):
        self.rudder = rudder

    def get_flight_controls(self):
        return {
            'throttle': self.throttle,
            'elevator': self.elevator,
            'ailerons': self.ailerons,
            'rudder': self.rudder
        }

# Example usage
jet = FighterJet()
jet.set_throttle(80)
jet.set_elevator(-5)
jet.set_ailerons(10)
jet.set_rudder(2)

flight_controls = jet.get_flight_controls()
print(flight_controls)
