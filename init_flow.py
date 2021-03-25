import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

Nx=20
Ny=40
Nt=20

dx=1/(Nx-1)
dy=1/(Ny-1)
dt=1

u_init = np.zeros((Nt,Ny,Nx))


u = u_init
print("初期状態 \n",u[1])
alpha=1


for n in range(Nt-1):
	for i in range(1,Nx-1):
		for j in range(1,Ny-1):
			u[n+1,j,i]=dt*( (dx*dy*dy + dx*dx*dy - 2*alpha*dy*dy - 2*alpha*dx*dx + 1/dt )*u[n,j,i] + (alpha*dy*dy - dx*dy*dy)*u[n,j,i+1] +  (alpha*dx*dx - dx*dx*dy)*u[n,j+1,i] + (alpha*dy*dy)*u[n,j,i-1] + (alpha*dx*dx)*u[n,j-1,i] + dx*dx*dy*dy )

data = u
sns.heatmap(data[Nt-1],vmin=np.amax(data[Nt-1])*0.9,vmax=np.amax(data[Nt-1]))
plt.savefig("img.png")


print("Courant Number",alpha*dx/dt)
print("Max Value",np.amax(data[Nt-1]))