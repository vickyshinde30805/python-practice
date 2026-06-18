class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        hour = hour % 12

        hour_angle = (30 * hour) + (0.5 * minutes)
        minutes_angle = 6 * minutes

        ans = abs(minutes_angle - hour_angle)

        return min(ans, 360 - ans)


# Create object
obj = Solution()

# Test cases
print(obj.angleClock(12, 0))    # 0.0
print(obj.angleClock(3, 15))    # 7.5
print(obj.angleClock(6, 0))     # 180.0
print(obj.angleClock(11, 0))    # 30.0