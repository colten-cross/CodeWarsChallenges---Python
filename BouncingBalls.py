# A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.

# He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

# His mother looks out of a window 1.5 meters from the ground.

# How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?#

# Note:
# The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

# Example:
# h = 3, bounce = 0.66, window = 1.5, result is 3

def bouncing_ball(h, bounce, window):
    Sightcount = 1
    current = h * bounce
    while current > window:
        current *= bounce
        Sightcount += 2
    return Sightcount 
    
