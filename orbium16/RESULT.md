# Orbium at the paper's parameters (sigma = 0.016) — PRIVATE

Source: Chan (2019), arXiv:1812.05433v3, Figures 6–7: Orbium mu = 0.15, sigma = 0.016;
the resolution experiments use R = 13 (time sweep) and T = 10 (space sweep); Orbium is
a rank-1 species (Figure 9), so beta = [1]. Supersedes the W1 run in ../orbium/ that used
sigma = 0.015 (an unverified secondary value).

Initial state: the sigma = 0.015 cultured glider (../orbium/culture_f64.py, seed 51) run
4000 steps in float64 at sigma = 0.016 (mass steady at 73.5–74.1), cropped 64x64,
placed in 256x256, quantised round-half-even.

| item | value |
|---|---|
| params (R=13 T=10 mu=1500 sigma=160 beta=1/1) | sha256:4e4af7f330a2390c92e9fbf85c3e5122cb9f209f636800ab988721e6050925e0 |
| L | 2000 steps |
| chain | sha256:924f55a6abd1983840cc539d13397303a1c68a2ae55b3ffe022895ae3ec3b33e |
| final | sha256:e56b1b9dc09ecd87c5966d391a72ce91c1892ebf7c46736646dfe1f201ebd622 |
| mass | 4829687 → 4831545 (+0.04%), survives |

Run with --algo ntt (equal to direct summation, see S1).
