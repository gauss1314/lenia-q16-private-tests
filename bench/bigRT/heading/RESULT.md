# ORB at R = 39: integer heading turns onto the lattice axis (2026-11-03)

- Integer reference (NTT, 512^2): heading 142 deg -> 180 deg over ~600 TU, then locked on the -x axis.
  float64 at the same R: 141.5 -> 140.8 deg over 2000 TU. Noise seeds (+-1 LSB): within 0.3 deg.
- Hybrid float64 runs, one integer ingredient swapped in (hybrid.py, 1000 TU):
  K (spec integer kernel / 2^16) reproduces the turn (141.7 -> -179.9); G (U floor + integer LUT)
  and S (state rounded to u16 each step) do not (141.5 -> 141.2). KGS = K.
- Kernel total 2^bb, plain rounding: Q16 turns (141.6 -> 179.9); Q20 and Q24 do not (141.5 -> 141.2/141.1).
- Cause: kernel weight quantisation at total 2^16. At R = 39 there are ~4800 taps, mean weight ~14,
  so the rounding error per tap is a few percent and is anisotropic. Input to D-022 / D-028 (W3).
- R sweep (rsweep.py): see rsweep.txt.

## 2026-11-04: real integer reference with kernel total 2^20 (branch exp/kernel-2p20)

ORB R=39, 2000 TU: heading 141.5 -> 142.9 deg and stable (heading_k20.txt). float64 141.5 -> 140.8. Final difference about 2 deg (tolerance 5). With 2^16 it locked at 180.
