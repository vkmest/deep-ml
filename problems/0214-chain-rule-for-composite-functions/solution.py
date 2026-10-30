import numpy as np
import math

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	g, g_der = x, 1

	for f in reversed(functions):
		match f:
			case "square":
				g, g_der = g**2, 2*g * g_der
			case "sin":
				g, g_der = math.sin(g), math.cos(g) * g_der
			case "exp":
				g, g_der = math.exp(g), math.exp(g) * g_der
			case "log":
				g, g_der = math.log(g), 1/g * g_der
	
	return g_der