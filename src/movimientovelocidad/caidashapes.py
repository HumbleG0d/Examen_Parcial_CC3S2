INITIAL_FALL_SPEED = 100
SPEED_INCREMENT_INTERVAL = 1000
SPEED_INCREASE_FACTOR = 0.9

class FallManager:
    def __init__(self):
        self.fall_speed = INITIAL_FALL_SPEED
        self.fall_timer =0
        self.game_time= 0

    def update_fall_speed(self, time_passed):
        self.game_time +=time_passed
        if self.game_time >= SPEED_INCREMENT_INTERVAL:
            self.fall_speed *= SPEED_INCREASE_FACTOR
            self.game_time = 0

    def update_fall_timer(self, time_passed):
        self.fall_timer += time_passed
        if self.fall_timer > self.fall_speed:
            self.fall_timer= 0
            return True
        return False
