# Literature-locus benchmarks (D-065) — PRIVATE

| name | params | chain (200 TU) | int / f64 mass | int / f64 speed (cells/TU) | 2R | 4T | note |
|---|---|---|---|---|---|---|---|
| ORB | R=13 T=10 mu=1500 sigma=160 beta=1/1 (Chan 2019 Fig. 6–7) | sha256:924f55a6abd1983840cc539d13397303a1c68a2ae55b3ffe022895ae3ec3b33e | 73.686 / 73.739 | 6.2647 / 6.2658 | survives | survives | Orbium; Platonic, agrees with Davis (2024) |
| P4spf | R=13 T=10 mu=3000 sigma=402 beta=1/1 (Chan 2019 Table 6 midpoint; R, T assumed) | sha256:2a318f613efeb46f7e94206d36e63e263d411fc621d27546f984411a00f4e7a0 | 112.261 / 112.302 | 0.0022 / 0.0024 | survives | survives | stationary blob; NOT confirmed to be Paraptera (the paper's species translocate) |

The other four Paraptera loci (P4as 0.0492, P4cp 0.0448, P4sp 0.0409, P4spr 0.0396) gave no stable
structure from ~210 random/gaussian/ring starts each at R=13, T=10. Per D-065 they are replaced by
self-found structures (code repo bench/v0/).
