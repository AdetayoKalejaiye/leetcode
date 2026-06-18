class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        dec = minutes / 60.0
        hour += dec
        minutes /= 5
        #37 minute = 7.4

        hour *= 30
        minutes *= 30
        angle = abs(hour - minutes)
        return min(angle, 360 - angle)
