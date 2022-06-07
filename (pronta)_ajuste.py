# Autor - Gilson Carvalho Filho - Engenharia Civil UFAL - 22/09/2021
# Código para o cálculo de ajustes de curvas

# O que falta fazer (qual método é melhor?, diminuir os algarismos significativos)

import numpy as np
import math

n=int(input("Insira o número de pontos a serem ajustados: "))
xy=np.ones((n,2))
for i in range(n):
	xy[i][0]=float(input("Entre com o X{}: ".format(i)))
for j in range(n):
	xy[j][1]=float(input("Entre com o Y{}: ".format(j)))

#temporario
#n=5
#xy=np.array([[0,1],[0.25,1.284],[0.5,1.6484],[0.75,2.117],[1,2.7183]])

mx1=0
for i in range(n):
	mx1=(xy[i][0])+mx1
mx2=0
for i in range(n):
	mx2=((xy[i][0])**2)+mx2
mx3=0
for i in range(n):
	mx3=((xy[i][0])**3)+mx3
mx4=0
for i in range(n):
	mx4=((xy[i][0])**4)+mx4
mx5=0
for i in range(n):
	mx5=((xy[i][0])**5)+mx5
mx6=0
for i in range(n):
	mx6=((xy[i][0])**6)+mx6
my1=0
for i in range(n):
	my1=(xy[i][1])+my1
my1x1=0
for i in range(n):
	my1x1=((xy[i][0])*(xy[i][1]))+my1x1
my1x2=0
for i in range(n):
	my1x2=(((xy[i][0])**2)*(xy[i][1]))+my1x2
my1x3=0
for i in range(n):
	my1x3=(((xy[i][0])**3)*(xy[i][1]))+my1x3
mlny=0
for i in range(n):
	mlny=(np.log(xy[i][1]))+mlny
mlnyx1=0
for i in range(n):
	mlnyx1=((xy[i][0])*(np.log(xy[i][1])))+mlnyx1

ml=np.array([[n,mx1],[mx1,mx2]])
mp2=np.array([[n,mx1,mx2],[mx1,mx2,mx3],[mx2,mx3,mx4]])
mp3=np.array([[n,mx1,mx2,mx3],[mx1,mx2,mx3,mx4],[mx2,mx3,mx4,mx5],[mx3,mx4,mx5,mx6]])
myl=np.array([[my1],[my1x1]])
myp2=np.array([[my1],[my1x1],[my1x2]])
myp3=np.array([[my1],[my1x1],[my1x2],[my1x3]])
mye=np.array([[mlny],[mlnyx1]])

# Calculando as matrizes inversas

mlinv=np.linalg.inv(ml)
mp2inv=np.linalg.inv(mp2)
mp3inv=np.linalg.inv(mp3)

al=mlinv.dot(myl)
ap2=mp2inv.dot(myp2)
ap3=mp3inv.dot(myp3)
ae=mlinv.dot(mye)
aef=np.array([[(math.e)**(ae[0][0])],[ae[1][0]]])

print("A reta de ajuste é \33[36mP(x)={}+{}.x\33[m ".format("%.3f" %(al[0][0]),"%.3f" %(al[1][0])))
print("A função quadrática de ajuste é \33[36mP(x)={}+{}.x+{}.x²\33[m ".format("%.3f" %(ap2[0][0]),"%.3f" %(ap2[1][0]),"%.3f" %(ap2[2][0])))
print("A função cúbica de ajuste é \33[36mP(x)={}+{}.x+{}.x²+{}.x³\33[m ".format("%.3f" %(ap3[0][0]),"%.3f" %(ap3[1][0]),"%.3f" %(ap3[2][0]),"%.3f" %(ap3[3][0])))
print("A curva exponencial de ajuste é \33[36mP(x)={}.eˆ({}.x)\33[m ".format("%.3f" %(aef[0][0]),"%.3f" %(aef[1][0])))

z=1
while(z==1):
	print("Deseja ver a resolução passa a passo de algum dos ajustes (s) ou (n)? ")
	w=str(input())
	while(w!="s" and w!="n"):
		print("Use apenas (s) ou (n) ")
		print("Deseja ver a resolução passa a passo de algum dos métodos (s) ou (n)? ")
		w=str(input())
	if(w=="n"):
		quit()
	if(w=="s"):
		print("Selecione qual ajuste você deseja encontrar: ")
		print("[1] Ajuste linear")
		print("[2] Ajuste quadrática")
		print("[3] Ajuste cúbico")
		print("[4] Ajuste exponencial")
		print("[5] Qual o melhor ajuste?")
		u=int(input())
		while(u!=1 and u!=2 and u!=3 and u!=4 and u!=5):
			print("Escolha apenas um número dentro do intervalo fechado 1 e 4: ")
			print("Selecione qual ajuste você deseja encontrar: ")
			print("[1] Ajuste linear")
			print("[2] Ajuste quadrática")
			print("[3] Ajuste cúbico")
			print("[4] Ajuste exponencial")
			print("[5] Qual o melhor ajuste?")
			u=int(input())
		if(u==1):
			mxlap=np.array([[n,mx1],[mx1,mx2]])
			malap=np.array([["ao"],["a1"]])
			mylap=np.array([[my1],[my1x1]])
			mxlapi=np.array([["n","Σxi"],["Σxi","Σxi2"]])
			malapi=np.array([["ao"],["a1"]])
			mylapi=np.array([["Σyi"],["Σyi.xi"]])
			print("------------------------------------------------------------------------------------")
			print("Equação matricial linear: ")
			print("X.A=Y")
			print("------------------------------------------------------------------------------------")
			print("X=")
			print(mxlapi)
			print("------------------------------------------------------------------------------------")
			print("A=")
			print(malapi)
			print("------------------------------------------------------------------------------------")
			print("Y=")
			print(mylapi)
			print("------------------------------------------------------------------------------------")
			print("Equação matricial linear resolvida: ")
			print("X.A=Y")
			print("------------------------------------------------------------------------------------")
			print("X=")
			print(mxlap)
			print("------------------------------------------------------------------------------------")
			print("A=")
			print(malap)
			print("------------------------------------------------------------------------------------")
			print("Y=")
			print(mylap)
			print("------------------------------------------------------------------------------------")
			print("a0 e a1 lineares: ")
			print("a0=")
			print(al[0][0])
			print("------------------------------------------------------------------------------------")
			print("a1=")
			print(al[1][0])
			print("------------------------------------------------------------------------------------")
		if(u==2):
			mxpap=np.array([[n,mx1,mx2],[mx1,mx2,mx3],[mx2,mx3,mx4]])
			mapap=np.array([["ao"],["a1"],["a2"]])
			mypap=np.array([[my1],[my1x1],[my1x2]])
			mxpapi=np.array([["n","Σxi","Σxi2"],["Σxi","Σxi2","Σxi3"],["Σxi2","Σxi3","Σxi4"]])
			mapapi=np.array([["ao"],["a1"],["a2"]])
			mypapi=np.array([["Σyi"],["Σyi.xi"],["Σyi.xi2"]])
			print("------------------------------------------------------------------------------------")
			print("Equação matricial parabólica: ")
			print("X.A=Y")
			print("------------------------------------------------------------------------------------")
			print("X=")
			print(mxpapi)
			print("------------------------------------------------------------------------------------")
			print("A=")
			print(mapapi)
			print("------------------------------------------------------------------------------------")
			print("Y=")
			print(mypapi)
			print("------------------------------------------------------------------------------------")
			print("Equação matricial parabólica resolvida: ")
			print("X.A=Y")
			print("------------------------------------------------------------------------------------")
			print("X=")
			print(mxpap)
			print("------------------------------------------------------------------------------------")
			print("A=")
			print(mapap)
			print("------------------------------------------------------------------------------------")
			print("Y=")
			print(mypap)
			print("------------------------------------------------------------------------------------")
			print("a0, a1 e a2 parabólica: ")
			print("a0=")
			print(ap2[0][0])
			print("------------------------------------------------------------------------------------")
			print("a1=")
			print(ap2[1][0])
			print("------------------------------------------------------------------------------------")
			print("a2=")
			print(ap2[2][0])
			print("------------------------------------------------------------------------------------")
		if(u==3):
			mxp3ap=np.array([[n,mx1,mx2,mx3],[mx1,mx2,mx3,mx4],[mx2,mx3,mx4,mx5],[mx3,mx4,mx5,mx6]])
			map3ap=np.array([["ao"],["a1"],["a2"],["a3"]])
			myp3ap=np.array([[my1],[my1x1],[my1x2],[my1x3]])
			mxp3api=np.array([["n","Σxi","Σxi2","Σxi3"],["Σxi","Σxi2","Σxi3","Σxi4"],["Σxi2","Σxi3","Σxi4","Σxi5"],["Σxi3","Σxi4","Σxi5","Σxi6"]])
			map3api=np.array([["ao"],["a1"],["a2"],["a3"]])
			myp3api=np.array([["Σyi"],["Σyi.xi"],["Σyi.xi2"],["Σyi.xi3"]])
			print("------------------------------------------------------------------------------------")
			print("Equação matricial cúbica: ")
			print("X.A=Y")
			print("------------------------------------------------------------------------------------")
			print("X=")
			print(mxp3api)
			print("------------------------------------------------------------------------------------")
			print("A=")
			print(map3api)
			print("------------------------------------------------------------------------------------")
			print("Y=")
			print(myp3api)
			print("------------------------------------------------------------------------------------")
			print("Equação matricial cúbica resolvida: ")
			print("X.A=Y")
			print("------------------------------------------------------------------------------------")
			print("X=")
			print(mxp3ap)
			print("------------------------------------------------------------------------------------")
			print("A=")
			print(map3ap)
			print("------------------------------------------------------------------------------------")
			print("Y=")
			print(myp3ap)
			print("------------------------------------------------------------------------------------")
			print("a0, a1, a2 e a3 cúbica: ")
			print("a0=")
			print(ap3[0][0])
			print("------------------------------------------------------------------------------------")
			print("a1=")
			print(ap3[1][0])
			print("------------------------------------------------------------------------------------")
			print("a2=")
			print(ap3[2][0])
			print("------------------------------------------------------------------------------------")
			print("a3=")
			print(ap3[3][0])
			print("------------------------------------------------------------------------------------")
		if(u==4):
			mxeap=np.array([[n,mx1],[mx1,mx2]])
			maeap=np.array([["ao"],["a1"]])
			myeap=np.array([[mlny],[mlnyx1]])
			mxeapi=np.array([["n","Σxi"],["Σxi","Σxi2"]])
			maeapi=np.array([["ao"],["a1"]])
			myeapi=np.array([["Σln(yi)"],["Σln(yi).xi"]])
			print("------------------------------------------------------------------------------------")
			print("Equação matricial exponencial: ")
			print("X.A=Y")
			print("------------------------------------------------------------------------------------")
			print("X=")
			print(mxeapi)
			print("------------------------------------------------------------------------------------")
			print("A=")
			print(maeapi)
			print("------------------------------------------------------------------------------------")
			print("Y=")
			print(myeapi)
			print("------------------------------------------------------------------------------------")
			print("Equação matricial exponencial resolvida: ")
			print("X.A=Y")
			print("------------------------------------------------------------------------------------")
			print("X=")
			print(mxeap)
			print("------------------------------------------------------------------------------------")
			print("A=")
			print(maeap)
			print("------------------------------------------------------------------------------------")
			print("Y=")
			print(myeap)
			print("------------------------------------------------------------------------------------")
			print("a0 e a1 exponencial: ")
			print("A equação é da forma P(x)=a.eˆ(b.x)")
			print("a0=")
			print(ae[0][0])
			print("------------------------------------------------------------------------------------")
			print("a1=")
			print(ae[1][0])
			print("------------------------------------------------------------------------------------")
			print("a=eˆ(a1)")
			print(aef[0][0])
			print("------------------------------------------------------------------------------------")
			print("b=a1")
			print(ae[1][0])
			print("------------------------------------------------------------------------------------")
		if(u==5):
			
			# Coeficiente de pearson para função linear:

			mresl=np.ones((n,2))
			for i in range(n):
				mresl[i][1]=(al[0][0])+((xy[i][0])*(al[1][0]))
				mresl[i][0]=xy[i][0]
			cima=0
			for i in range(n):
				cima=cima+(((xy[i][1])-(mresl[i][1]))**2)
			cima=cima*n
			baixo1=0
			for i in range(n):
				baixo1=baixo1+((xy[i][1])**2)
			baixo1=baixo1*n
			baixo2=my1**2
			cpl=(1-((cima)/(baixo1-baixo2)))**(1/2)

			# Coeficiente de pearson para função quadrática

			mresp2=np.ones((n,2))
			for i in range(n):
				mresp2[i][1]=(ap2[0][0])+((xy[i][0])*(ap2[1][0]))+((ap2[2][0])*((xy[i][0])**2))
				mresp2[i][0]=xy[i][0]
			cima=0
			for i in range(n):
				cima=cima+(((xy[i][1])-(mresp2[i][1]))**2)
			cima=cima*n
			baixo1=0
			for i in range(n):
				baixo1=baixo1+((xy[i][1])**2)
			baixo1=baixo1*n
			baixo2=my1**2
			cpp2=(1-((cima)/(baixo1-baixo2)))**(1/2)

			# Coeficiente de pearson para função cúbica

			mresp3=np.ones((n,2))
			for i in range(n):
				mresp3[i][1]=(ap3[0][0])+((xy[i][0])*(ap3[1][0]))+((ap3[2][0])*((xy[i][0])**2))+((ap3[3][0])*((xy[i][0])**3))
				mresp3[i][0]=xy[i][0]
			cima=0
			for i in range(n):
				cima=cima+(((xy[i][1])-(mresp3[i][1]))**2)
			cima=cima*n
			baixo1=0
			for i in range(n):
				baixo1=baixo1+((xy[i][1])**2)
			baixo1=baixo1*n
			baixo2=my1**2
			cpp3=(1-((cima)/(baixo1-baixo2)))**(1/2)

			# Coeficiente de pearson para função exponencial

			mrese=np.ones((n,2))
			for i in range(n):
				mrese[i][1]=(aef[0][0])*((math.e)**((ae[1][0])*(xy[i][0])))
				mrese[i][0]=xy[i][0]
			cima=0
			for i in range(n):
				cima=cima+(((xy[i][1])-(mrese[i][1]))**2)
			cima=cima*n
			baixo1=0
			for i in range(n):
				baixo1=baixo1+((xy[i][1])**2)
			baixo1=baixo1*n
			baixo2=my1**2
			cppe=(1-((cima)/(baixo1-baixo2)))**(1/2)

			listacp=np.array([[cpl],[cpp2],[cpp3],[cppe]])
			print("Linear = ",cpl)
			print("Quadrática = ",cpp2)
			print("Cúbica = ",cpp3)
			print("Exponencial = ",cppe)

			nome="nada"
			if(cpl==(listacp.max())):
				nome="Linear"
			if(cpp2==(listacp.max())):
				nome="Quadrática"
			if(cpp3==(listacp.max())):
				nome="Cúbica"
			if(cppe==(listacp.max())):
				nome="Exponencial"

			print("A melhor curva que se ajusta aos pontos é a \33[36m{}\33[m pois é a\n que teve o coeficiente de Pearson mais próximo de 1: ".format(nome))


