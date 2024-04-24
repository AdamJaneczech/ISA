gradients = [-0.0065, 0, 0.0010, 0.0028, 0, -0.0028, -0.0020]
altitudes = [11000, 20000, 32000, 47000, 51000, 71000, 86000]
g_0, T_0, p_0, rho_0, R = 9.80665, 288.15, 101325, 1.225, 287.0

alt = float(input('Enter altitude: '))

def calcTemp(alt):
    T = T_0
    for i in range(0, len(altitudes)):
        if(alt > altitudes[i]):
            T += gradients[i]*(altitudes[i]-altitudes[i-1]) if i > 0 else gradients[i]*(altitudes[i])
        else:
            T += gradients[i]*(alt-altitudes[i-1]) if i > 0 else gradients[i]*alt
            break
    return T

print(calcTemp(alt))