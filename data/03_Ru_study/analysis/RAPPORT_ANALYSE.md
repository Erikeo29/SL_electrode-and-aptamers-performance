# Rapport d'analyse - Etude R_u (resistance non-compensee)

Date: 2026-02-07 18:17
Nombre de runs: 54

## Design experimental

- RF: [np.float64(1.0), np.float64(2.0), np.float64(5.0)]
- Ni_pct: [np.int64(0), np.int64(5), np.int64(10)]
- R_u: [np.int64(0), np.int64(50), np.int64(100), np.int64(200), np.int64(500), np.int64(1000)] Ohm
- frequency=25 Hz, Cu=0, contamination=0 (fixes)

## Statistiques

| Metrique | Min | Mediane | Max |
|----------|-----|---------|-----|
| I_peak_nA | 1541.733 | 2935.906 | 4103.704 |
| SNR | 126.900 | 501.450 | 2883.000 |
| FWHM_mV | 56.000 | 56.000 | 64.000 |
| IR_drop_mV | 0.000 | 0.370 | 4.800 |
| E_peak_V | -0.244 | -0.240 | -0.240 |

## Impact R_u (electrode propre RF=1, Ni=0)

| R_u (Ohm) | SNR | I_peak (nA) | E_peak (mV) | FWHM (mV) | IR_drop (mV) |
|-----------|-----|-------------|-------------|-----------|-------------|
| 0 | 2206.2 | 1770.03 | -240.0 | 56.0 | 0.00 |
| 50 | 1917.5 | 1767.73 | -240.0 | 56.0 | 0.07 |
| 100 | 1915.2 | 1763.68 | -240.0 | 56.0 | 0.14 |
| 200 | 2225.2 | 1759.32 | -240.0 | 56.0 | 0.28 |
| 500 | 1790.9 | 1744.36 | -240.0 | 56.0 | 0.69 |
| 1000 | 1878.4 | 1715.59 | -240.0 | 56.0 | 1.38 |
