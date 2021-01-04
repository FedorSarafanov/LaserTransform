from numpy import sqrt, array, sin, cos, exp, pi, tan
# в СГС #
lamda = 1064e-7 # см
chi = 10**-3 # (cm ** 2)/с

tau_0 = 0.0016523 # с

roCp = 10**7 # Эрг / (см**3 * К)
dedT = 1e-3 # 1/К
L = 5e-1 # см
d = 1e-1 # см
teta = 5/330 # Рад
n=1.5
eps_0 = sqrt(n)

k = 2 * pi / lamda 

k_x = k*sin(teta / 2)
k_z = k*cos(teta / 2) 
# print('k',k,k_z)

L = L*(k**2 / k_z / eps_0)
print(L)

# Время релаксации решетки 
tau_relax = tau_0 / (1 + 4 * chi *k_x ** 2 * tau_0) # с
print(tau_relax)

# Массив  мощностей 
P_ref = array([160, 182, 233, 267, 293, 323])*1e-3 * 10**7  #эрг/c

# Площадь пучка #
S_b = pi * (d / 2) ** 2

# I_0 #
I_0 =  P_ref / S_b 

sigma_0 = 3.5
print('sigma0',sigma_0)

# Характеристика эффективности ПДВ #
G = sigma_0 * tau_relax * I_0 * dedT / (4 * eps_0 * roCp)
# print(G*L)
# Коэффициент отражения ОВФ-зеркала #
re = tan (G*L) # Коэффициент отражения
# r = re**2 # Квадрат коэффициента отражения	
print(G*L, pi/2)
print(re)
# print(r)



p_sig = array([79, 110, 130, 147, 162, 176])
p_obr = array([18, 23, 27, 31, 31, 33])

rr = sqrt(p_obr / p_sig)

from matplotlib import pyplot as plt 
plt.plot(rr)
plt.plot(re*2)
plt.show()