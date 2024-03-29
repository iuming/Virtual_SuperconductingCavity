import epics
import numpy as np

while True:
    f_m1 = epics.caget("F_K1")
    f_m2 = epics.caget("F_K2")
    f_m3 = epics.caget("F_K3")
    
    Q_m1 = epics.caget("Q_K1")
    Q_m2 = epics.caget("Q_K2")
    Q_m3 = epics.caget("Q_K3")
    
    K_m1 = epics.caget("K_LFD1")
    K_m2 = epics.caget("K_LFD2")
    K_m3 = epics.caget("K_LFD3")
    
    dOmega1_dt = epics.caget("dOmega1_dt")
    dOmega2_dt = epics.caget("dOmega2_dt")
    dOmega3_dt = epics.caget("dOmega3_dt")
    
    V_I = epics.caget("V_I")
    V_Q = epics.caget("V_Q")
    V = np.sqrt(V_I**2 + V_Q**2)
    
    df_1 = epics.caget("DEL_F_LFD_1")
    df_2 = epics.caget("DEL_F_LFD_2")
    df_3 = epics.caget("DEL_F_LFD_3")
        
    f_m = np.array([f_m1, f_m2, f_m3])
    Q_m = np.array([Q_m1, Q_m2, Q_m3])
    K_m = np.array([K_m1, K_m2, K_m3])
    dOmega_dt = np.array([dOmega1_dt, dOmega2_dt, dOmega3_dt])
    omega_last = np.array([2*np.pi*df_1, 2*np.pi*df_2, 2*np.pi*df_3])
    Ts = epics.caget("Ts")

    d2omega_dt2 = np.zeros(3)
    omega_new = np.zeros(3)	

    for i in range(3):
        dt = Ts
        d2omega_dt2[i] = -2 * np.pi * f_m[i]**2 * omega_last[i] - 2 * np.pi * f_m[i] / Q_m[i] * dOmega_dt[i] - (2 * np.pi * f_m[i])**2 * K_m[i] * V**2
        dOmega_dt[i] += d2omega_dt2[i] * dt
        omega_new[i] = omega_last[i] + dOmega_dt[i] * dt
        print(omega_new)
        epics.caput("dOmega" + str(i+1) + "_dt", dOmega_dt[i])
        epics.caput("DEL_F_LFD_" + str(i+1), omega_new[i] / (2 * np.pi))

epics.caput 
