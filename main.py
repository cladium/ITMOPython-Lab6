import time
from enum import Enum

class LampState(Enum):
    ON = 0
    OFF = 1
    BURNT_OUT = 2

class Lamp:
    def __init__(self, radiation_power: float, energy_consumption: float, service_life_hours: int):
        # private fields
        self._radiation_power = radiation_power
        self._energy_consumption = energy_consumption
        self._service_life_hours = service_life_hours
        self._state = LampState.OFF
        self._hours_used = 0
        self._turn_on_time = None

    # calculate how many days until the lamp burns out, assuming 8 hours of use per day
    def days_until_burnout(self):
        if self._state == LampState.BURNT_OUT:
            return 0
        remaining_hours = self._service_life_hours - self._hours_used
        if remaining_hours <= 0:
            return 0
        return remaining_hours / 8

    # calculate the ratio of radiation power to energy consumption
    def power_to_energy_ratio(self):
        return self._radiation_power / self._energy_consumption

    # turn the lamp on
    def turn_on(self):
        if self._hours_used >= self._service_life_hours:
            self._state = LampState.BURNT_OUT
            print("Lamp is burnt out and cannot be turned on.")
        elif self._state == LampState.ON:
            print("Lamp is already on.")
        else:
            self._state = LampState.ON
            self._turn_on_time = time.time()
            print("Lamp is turned on.")

    # turn the lamp off
    def turn_off(self):
        if self._state == LampState.OFF:
            print("Lamp is already off.")
        elif self._state != LampState.BURNT_OUT:
            self._state = LampState.OFF
            duration_on = time.time() - self._turn_on_time
            self._hours_used += duration_on / 3600.0
            self._turn_on_time = None
            print(f"Lamp is turned off. It was on for {duration_on:.2f} seconds (or {(duration_on / 3600.0):.4f} hours).")

    # simulate lamp usage for a certain number of hours
    def use_lamp(self, hours: float):
        if self._state == LampState.BURNT_OUT:
            print("The lamp is burnt out and cannot be used.")
            return
        self._hours_used += hours
        if self._hours_used >= self._service_life_hours:
            self._state = LampState.BURNT_OUT

    def get_state(self):
        return self._state

    # string representation of the lamp's current state
    def __str__(self):
        return f"Lamp(radiation_power={self._radiation_power}, energy_consumption={self._energy_consumption}, service_life_hours={self._service_life_hours}, state={self._state})"


class DaylightLamp(Lamp):
    def __init__(self, radiation_power: float, energy_consumption: float, service_life_hours: int, mercury_content: float):
        super().__init__(radiation_power, energy_consumption, service_life_hours)
        self._mercury_content = mercury_content  # unique field for DaylightLamp
    
    def get_mercury_content(self):
        return self._mercury_content

    def __str__(self):
        return f"DaylightLamp with mercury content {self._mercury_content} mg, {super().__str__()}"


class Spotlight(Lamp):
    def __init__(self, radiation_power: float, energy_consumption: float, service_life_hours: int, beam_angle: int):
        super().__init__(radiation_power, energy_consumption, service_life_hours)
        self._beam_angle = beam_angle  # Unique field for Spotlight

    def get_beam_angle(self):
        return self._beam_angle

    def __str__(self):
        return f"Spotlight with beam angle {self._beam_angle} degrees, {super().__str__()}"

# example usage
if __name__ == "__main__":
    lamp = Lamp(60, 100, 5000)
    print(lamp)
    lamp.turn_on()
    time.sleep(3)
    lamp.turn_off()
    lamp.use_lamp(1000)
    print(f"Days until burnout: {lamp.days_until_burnout():.6f}")
    print(f"Power to energy ratio: {lamp.power_to_energy_ratio()}")
       
    daylight = DaylightLamp(50, 80, 6000, 5.0)
    print(daylight)
    print(f"Mercury content: {daylight.get_mercury_content()} mg")