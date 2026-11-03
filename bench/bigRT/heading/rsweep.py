"""Heading drift vs R with a 2^16 kernel (diagnosis only). Scales the R=13 benchmark state
by R/13 (bilinear) onto 512^2, relaxes 50 TU in float64 at R, then runs float64 and the
2^16-rounded kernel for 1000 TU each and prints the heading every 100 TU."""
import sys, numpy as np
sys.path.insert(0, '/home/user/lenia-q16-ref/tools')
from lenia_f64 import kernel_f64, growth, read_state
R, var = int(sys.argv[1]), sys.argv[2]
T, mu, sg, n = 10, 0.15, 0.016, 512
q = read_state('/home/user/lenia-q16-private-tests/bench/ORB.s0.lq16') / 65535.0
N0 = q.shape[0]; y, x = np.unravel_index(np.argmax(q), q.shape); q = np.roll(q, (N0 // 2 - y, N0 // 2 - x), (0, 1))
f = R / 13; yy, xx = np.mgrid[0:n, 0:n]; sy = (yy - n / 2) / f + N0 / 2; sx = (xx - n / 2) / f + N0 / 2
y0 = np.floor(sy).astype(int); x0 = np.floor(sx).astype(int); fy = sy - y0; fx = sx - x0
g = lambda a, b: q[np.clip(a, 0, N0 - 1), np.clip(b, 0, N0 - 1)] * ((a >= 0) & (a < N0) & (b >= 0) & (b < N0))
A = g(y0, x0) * (1 - fy) * (1 - fx) + g(y0 + 1, x0) * fy * (1 - fx) + g(y0, x0 + 1) * (1 - fy) * fx + g(y0 + 1, x0 + 1) * fy * fx
def fk(K):
    pad = np.zeros((n, n)); pad[:2 * R + 1, :2 * R + 1] = K; return np.fft.fft2(np.roll(pad, (-R, -R), (0, 1)))
Kf = kernel_f64(R, [(1, 1)]); fKf = fk(Kf); fK = fk(np.round(Kf * 65536) / 65536 if var == 'Q16' else Kf)
for _ in range(50 * T):
    A = np.clip(A + growth(np.real(np.fft.ifft2(np.fft.fft2(A) * fKf)), mu, sg) / T, 0, 1)
e = np.exp(2j * np.pi * np.arange(n) / n)
cen = lambda A: np.array([np.angle((A.sum(1) * e).sum()), np.angle((A.sum(0) * e).sum())]) * n / (2 * np.pi)
cs = [cen(A)]
for k in range(1000):
    for _ in range(T):
        A = np.clip(A + growth(np.real(np.fft.ifft2(np.fft.fft2(A) * fK)), mu, sg) / T, 0, 1)
    if k % 10 == 9:
        cs.append(cen(A))
d = np.diff(np.array(cs), axis=0); d = (d + n / 2) % n - n / 2
h = np.degrees(np.arctan2(d[:, 0], d[:, 1]))
print(f'R={R} {var}:', ' '.join(f'{v:.1f}' for v in h[::10]), '| mass %.1f' % A.sum(), flush=True)
