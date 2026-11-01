# Literature-locus benchmarks (D-065) — PRIVATE

| name | params | chain (200 TU) | int / f64 mass | int / f64 speed (cells/TU) | 2R | 4T | note |
|---|---|---|---|---|---|---|---|
| ORB | R=13 T=10 mu=1500 sigma=160 beta=1/1 (Chan 2019 Fig. 6–7) | sha256:924f55a6abd1983840cc539d13397303a1c68a2ae55b3ffe022895ae3ec3b33e | 73.686 / 73.739 | 6.2647 / 6.2658 | survives | survives | Orbium; Platonic, agrees with Davis (2024) |
| P4spf | R=13 T=10 mu=3000 sigma=402 beta=1/1 (Chan 2019 Table 6 midpoint; R, T assumed) | sha256:2a318f613efeb46f7e94206d36e63e263d411fc621d27546f984411a00f4e7a0 | 112.261 / 112.302 | 0.0022 / 0.0024 | survives | survives | stationary blob; NOT confirmed to be Paraptera (the paper's species translocate) |

The other four Paraptera loci (P4as 0.0492, P4cp 0.0448, P4sp 0.0409, P4spr 0.0396) gave no stable
structure from ~210 random/gaussian/ring starts each at R=13, T=10. Per D-065 they are replaced by
self-found structures (code repo bench/v0/).

## Large R and large T (2026-11-01)

| test | params | N | steps | chain | start / int / f64 mass | max abs cell diff |
|---|---|---|---|---|---|---|
| ORB at R = 39 (3x upsample, relaxed 50 TU in float64) | R=39 T=10 mu=1500 sigma=160 beta=1/1 | 512 | 1000 | sha256:13b14846b8e433a0677e18a31166c9a67da17416e80f7097f1f9b02ffb1dac9e | 663.73 / 663.20 / 663.60 | 1.0 (same shape, positions drift apart) |
| ORB at T = 40 | R=13 T=40 mu=1500 sigma=160 beta=1/1 | 256 | 4000 | sha256:4e9d3c9f5e1675a63e3a8b7ef4496bf5d5e4078507e1fa6b26827c2558e1a825 | 73.70 / 72.44 / 72.50 | 0.05 |
