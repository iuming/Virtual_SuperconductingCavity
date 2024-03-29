import epics
import numpy as np

while True:

	i0 = epics.caget("Ig_I")
	RL = epics.caget("R")
	f_half = epics.caget("FHBW")
	delta_w = epics.caget("DEL_F_TOTAL")
	t = epics.caget("CurrentTime")
	t /= 1e6

	def v(t, w_half, delta_w, i0, RL):
		numerator = i0 * w_half * RL * (np.exp((-w_half + 1j * delta_w) * t) - 1)
		denominator = -w_half + 1j * delta_w
		return numerator / denominator


	v_t = v(t, 2*np.pi*f_half, delta_w, i0, RL)

	I = v_t.real
	Q = v_t.imag

	epics.caput("V_I", I)
	epics.caput("V_Q", Q)
