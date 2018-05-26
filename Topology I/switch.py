import math

def get_switch_amount(switch_level):
	if switch_level = 1:
		return 1
	else:
		return math.pow(2, switch_level - 1) + 2 * get_switch_amount(switch_level - 1)
