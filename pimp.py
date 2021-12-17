from multiprocessing import Pool
import random as rnd
import math
import matplotlib.pyplot as plt
from matplotlib import animation

def setplot(sx1,sx2,sy1,sy2):
	ax=plt.gca()
	ax.set_aspect(1)
	plt.xlim([sx1,sx2])
	plt.ylim([sy1,sy2])
	ax.set_facecolor('xkcd:black')

def pts(n):
	no=0
	ni=0
	xi=[]
	yi=[]
	xo=[]
	yo=[]
	for i in range(n):
		x=rnd.random()
		y=rnd.random()
		if(math.sqrt(x**2+y**2)<=1):
			ni+=1
			xi.append(x)
			yi.append(y)		
		else:
			no+=1
			xo.append(x)
			yo.append(y)
	return ni,xi,yi,no,xo,yo
 
if __name__ == '__main__':
	frps=30
	sec=60
	nr=0
	nb=0
	per='%'
	fig, a=plt.subplots()
	def run(frame):
		global nr,nb	
		N=10
		M=100
		itr=[]
		for i in range(N):
			itr.append(M)
		pool = Pool(processes=N)
		a=pool.map(pts, itr)
		for i in range(N):
			nr+=a[i][0]
			nb+=a[i][3]
			plt.plot(a[i][1],a[i][2],'ro',markersize=1)
			plt.plot(a[i][4],a[i][5],'bo',markersize=1)
		pi=4*nr/(nr+nb)
		plt.suptitle(r'$\pi \approx$ %f' % pi)
		pe=100*abs(pi-math.pi)/math.pi
		plt.title(per+'Error = %f' % pe)
		setplot(0,1,0,1)
	ani=animation.FuncAnimation(fig,run,frames=frps*sec)
	writervideo=animation.FFMpegWriter(fps=frps)
	ani.save('pi_est.mp4', writer=writervideo)
	plt.show()

