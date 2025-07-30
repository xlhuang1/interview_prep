# Find the Highest Altitude
# Leetcode 1732
# Given net altitude changes, find max altitude.
# 👉 Simple prefix sum.

def highest_altitude(alt_changes):
    current_altitude = 0
    max_alt = 0

    for x in alt_changes:
        current_altitude += x
        max_alt = max(current_altitude, max_alt)
    return max_alt