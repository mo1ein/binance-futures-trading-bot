def round_down(x: float, precision: int) -> :
	return round(x - 5 * (10 ** (-precision - 1)), precision)
