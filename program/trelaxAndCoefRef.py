from numpy import sqrt, array, sin, pi, tan
# условия #
lamda = 1064 # нм
# D = 1 # мм
hi = 1e-3 # (см ** 2)/с
tau_0 = 0.7 # мс — длительность импульса
roCp = 1 # Дж / (см**3 * К)
dedT = 1e-3 # 1/К
L = 5 # мм
n = 1.5
d = 1 # мм

eps_0 = sqrt(n)

# в СИ #
lamda = 1064e-9 # м
hi = 10**-7 # (м ** 2)/с
tau_0 = 0.0016523 # с
roCp = 10**6 # Дж / (м**3 * К)
L = 5e-3 # м
d = 1e-3 # м
teta = 5/330 # Рад
k = 2 * pi / lamda # 1/м
# Проекция волнового вектора на ось X #
k_x = k*sin(teta / 2) # 1/м

# Время релаксации решетки 
tau_relax = tau_0 / (1 + 4 * hi *k_x ** 2 * tau_0) # с
print(tau_relax)

# Массив  мощностей 
P_ref = array([160, 182, 233, 267, 293, 323])*1e-3

# Площадь пучка #
S_b = pi * (d / 2) ** 2

# I_0 #
I_0 = 2* P_ref / S_b 

sigma_0 =59.5e6 # Сименс/м (проводимость меди)

# Характеристика эффективности ПДВ #
G = sigma_0 * tau_relax * I_0 * dedT / (4 * eps_0 * roCp)

# Коэффициент отражения ОВФ-зеркала #
re = tan (G*L) # Коэффициент отражения
r = re**2 # Квадрат коэффициента отражения	

print(re)
print(r)