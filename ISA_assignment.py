from math import e
gradients = [-0.0065, 0, 0.0010, 0.0028, 0, -0.0028, -0.0020]
altitudes = [11000, 20000, 32000, 47000, 51000, 71000, 86000]
g_0, T_0, p_0, rho_0, R = 9.80665, 288.15, 101325, 1.225, 287.0

altitude = float(input('Enter altitude: '))

def calcISA(alt):
    T, t_0 = T_0, T_0 #local variable
    p = p_0
    for i in range(0, len(altitudes)):
        if(alt > altitudes[i]):
            T += gradients[i]*(altitudes[i]-altitudes[i-1]) if i > 0 else gradients[i]*(altitudes[i])
            p *= pow(T/t_0,-g_0/(gradients[i] * R)) if gradients[i] != 0 else pow(e,((-g_0)/(R*T))*(altitudes[i]-altitudes[i-1])) #no need to check whether i is higher than 0 since the isothermal region is always at i > 0
            t_0 = T
        else:
            T += gradients[i]*(alt-altitudes[i-1]) if i > 0 else gradients[i]*alt
            p = p*pow(T/t_0,-g_0/(gradients[i] * R)) if gradients[i] != 0 else p*pow(e,((-g_0)/(R*T))*(alt-altitudes[i-1]))         
            break
    rho = p/(R*T)
    return T, p, rho

print(calcISA(altitude))