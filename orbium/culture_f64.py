import sys, numpy as np
sys.path.insert(0,'/home/user/lenia-q16-ref/tools')
from lenia_f64 import Lenia
N=128; R=13; T=10
L=Lenia(N,R,T,0.15,0.015,[(1,1)])
def cm(A):
    ang=2*np.pi*np.arange(N)/N
    return (np.angle((A.sum(1)*np.exp(1j*ang)).sum())%(2*np.pi)*N/(2*np.pi), np.angle((A.sum(0)*np.exp(1j*ang)).sum())%(2*np.pi)*N/(2*np.pi))
found=0
for seed in range(200):
    rng=np.random.default_rng(seed)
    amp=rng.uniform(0.3,1.0); s=int(rng.integers(16,40))
    A=np.zeros((N,N)); A[64-s//2:64-s//2+s,64-s//2:64-s//2+s]=rng.random((s,s))*amp
    ms=[];cs=[]
    for k in range(2000):
        A=L.step(A)
        if k>=1500 and k%50==0: ms.append(A.sum()); cs.append(cm(A))
    if min(ms)<1: continue
    var=(max(ms)-min(ms))/np.mean(ms)
    d=np.hypot(*(np.array(cs[-1])-np.array(cs[0])))
    nz=(A>0.01).sum()
    if var<0.03 and nz<800 and d>1:
        print(seed,f"amp={amp:.2f} s={s} mass={np.mean(ms):.1f} var={var:.3f} nz={nz} moved={d:.1f}")
        np.save(f'cand_{seed}.npy',A); found+=1
        if found>=3: break
print('done',found)
