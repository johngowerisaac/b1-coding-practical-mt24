class PIDController:
    def __init__(self, Kp: float, Kd: float, Ki: float):
        self.Kp = Kp
        self.Kd = Kd
        self.Ki = Ki
        self.previous_error = 0.0
        self.integral = 0.0

    def compute_control(self, reference: float, output: float) -> float:
        error = reference - output
        self.integral += error  # Accumulate error for integral term
        derivative = error - self.previous_error
        
        # Compute the control action (PID control)
        control_action = self.Kp * error + self.Kd * derivative + self.Ki * self.integral
        
        # Update previous error
        self.previous_error = error
        
        return control_action