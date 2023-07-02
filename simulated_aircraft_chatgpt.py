#ChatGPT Simulated Aircraft code
import time
import numpy as np

class Aircraft:
    def __init__(self, initial_altitude):
        self.altitude = initial_altitude
        self.velocity = 0
        self.acceleration = 0
    
    def update_state(self, throttle):
        # Simplified physics model to update altitude and velocity
        self.acceleration = throttle / 10
        self.velocity += self.acceleration
        self.altitude += self.velocity
    
    def get_state(self):
        return self.altitude, self.velocity

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0
        self.previous_error = 0
    
    def update(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.previous_error = error
        return output

def main():
    setpoint = 1000  # desired altitude in meters
    aircraft = Aircraft(initial_altitude=100)  # initial altitude in meters
    pid = PIDController(kp=1, ki=0.01, kd=0.1)  # PID gains
    dt = 0.1  # time step in seconds
    
    while True:
        altitude, _ = aircraft.get_state()
        error = setpoint - altitude
        throttle = pid.update(error, dt)
        aircraft.update_state(throttle)
        time.sleep(dt)

if __name__ == '__main__':
    main()
