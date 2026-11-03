import sys, subprocess, numpy as np
sys.path.insert(0, '/home/user/lenia-q16-ref/tools')
from lenia_f64 import Lenia, read_state
S = '/home/user/lenia-q16-private-tests/bench/bigRT/ORB_R39_s0.lq16'
P = 'R=39 T=10 mu=1500 sigma=160 beta=1/1'
q = read_state(S); n = q.shape[0]; e = np.exp(2j * np.pi * np.arange(n) / n)
def cen(A):
    return np.array([np.angle((A.sum(1) * e).sum()), np.angle((A.sum(0) * e).sum())]) * n / (2 * np.pi)
def heading(cs):
    d = np.diff(np.array(cs), axis=0); d = (d + n / 2) % n - n / 2
    return np.degrees(np.arctan2(d[:, 0], d[:, 1]))
mode = sys.argv[1]
cs = []
if mode == 'int':
    subprocess.run(['/home/user/lenia-q16-ref/target/release/lq16', 'run', '--params', P, '--state', S, '--steps', '20000',
                    '--algo', 'ntt', '--dump', '/home/user/work/heading/int.u16', '--every', '100'], check=True, capture_output=True)
    F = np.memmap('/home/user/work/heading/int.u16', dtype='<u2', mode='r').reshape(-1, n, n)
    cs = [cen(f / 65535.0) for f in F]
else:
    L = Lenia(n, 39, 10, 0.15, 0.016, [(1, 1)]); A = q / 65535.0
    for k in range(200):
        for _ in range(100):
            A = L.step(A)
        cs.append(cen(A))
h = heading(cs)
np.save(f'/home/user/work/heading/{mode}.npy', h)
print(mode, ' '.join(f'{x:.1f}' for x in h[::10]))
