"""Which quantisation turns the R=39 Orbium? float64 run with one integer ingredient swapped in.
K: integer kernel weights / 2^16   G: U floored to the u16 grid + integer growth LUT
S: state rounded to u16 every step  (letters combine, e.g. KGS)"""
import sys, numpy as np
sys.path.insert(0, '/home/user/lenia-q16-ref/tools')
from lenia_f64 import kernel_f64, growth, read_state
v = sys.argv[1]; TUS = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
S0 = '/home/user/lenia-q16-private-tests/bench/bigRT/ORB_R39_s0.lq16'
R, T, mu, sg = 39, 10, 0.15, 0.016
q = read_state(S0); n = q.shape[0]
if v.startswith('Q'):  # Qbb: continuous kernel rounded to a total of 2^bb (diagnosis only, no exact-sum fix-up)
    bits = int(v[1:]); K = np.round(kernel_f64(R, [(1, 1)]) * 2 ** bits) / 2 ** bits
elif 'K' in v:
    b = open('/home/user/work/heading/rec/kernel.lq16', 'rb').read()
    K = np.frombuffer(b[44:], '<u4').reshape(2 * R + 1, 2 * R + 1) / 65536.0
else:
    K = kernel_f64(R, [(1, 1)])
pad = np.zeros((n, n)); pad[:2 * R + 1, :2 * R + 1] = K; pad = np.roll(pad, (-R, -R), axis=(0, 1))
fK = np.fft.fft2(pad)
lut = np.frombuffer(open('/home/user/work/heading/rec/lut.lq16', 'rb').read()[40:], '<i4') / 65535.0
e = np.exp(2j * np.pi * np.arange(n) / n)
cen = lambda A: np.array([np.angle((A.sum(1) * e).sum()), np.angle((A.sum(0) * e).sum())]) * n / (2 * np.pi)
A = q / 65535.0; cs = [cen(A)]
for k in range(TUS):
    for _ in range(T):
        U = np.real(np.fft.ifft2(np.fft.fft2(A) * fK))
        if 'G' in v:
            idx = np.clip(np.floor(U * 65535 + 1e-9), 0, 65535).astype(int)
            A = np.clip(A + lut[idx], 0, 1)
        else:
            A = np.clip(A + growth(U, mu, sg) / T, 0, 1)
        if 'S' in v:
            A = np.round(A * 65535) / 65535
    if k % 10 == 9:
        cs.append(cen(A))
d = np.diff(np.array(cs), axis=0); d = (d + n / 2) % n - n / 2
h = np.degrees(np.arctan2(d[:, 0], d[:, 1]))
print(v or 'f64', 'heading every 100 TU:', ' '.join(f'{x:.1f}' for x in h[::10]), '| mass %.1f' % A.sum(), flush=True)
