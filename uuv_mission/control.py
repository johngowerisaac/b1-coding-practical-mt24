class PDController:
    def __init__(self, Kp: float, Kd: float):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0.0

    def compute_control(self, reference: float, output:float) -> float:
        error = reference - output
        control_action = self.Kp * error + self.Kd * (error - self.previous_error)
        self.previous_error = error
        return control_action