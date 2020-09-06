import math

print("Örnek Parabol: f(x)=ax2+bx+c")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

atepe = a*2
btepe = b*-1
rtepenoktasi = btepe/atepe

kicinrtepe = rtepenoktasi**2
ktepenoktasi = kicinrtepe*a+b*rtepenoktasi+c

delta = b**2-4*a*c

if delta>0:
	print("\nGrafik x eksenini iki noktada keser.")
	print("Diskriminant =",delta)
	print("T(r,k):",rtepenoktasi,",",ktepenoktasi)
elif delta==0:
        print("\nGrafik x eksenine teğettir.")
        print("Diskriminant =",delta)
        print("T(r,k):",rtepenoktasi,",",ktepenoktasi)
elif delta<0:
        print("\nGrafik x eksenini kesmez.")
        print("Diskriminant =",delta)
        print("T(r,k):",rtepenoktasi,",",ktepenoktasi)

else:

	print("Yanlış giden bir şeyler var.")
