import math

def get_switch_amount(switch_level):
	sum = math.pow(2, switch_level - 1)
	while (0 < switch_level - 1):
		sum += math.pow(2, switch_level - 1)
		switch_level -= 1
	return int(sum)
