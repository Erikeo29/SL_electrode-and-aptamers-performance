# Rapport d'analyse - Etude frequence SWV

Date: 2026-02-07 18:17
Nombre de runs: 72

## Design experimental

- RF: [np.float64(1.0), np.float64(1.5), np.float64(2.0), np.float64(3.0)]
- Ni_pct: [np.int64(0), np.int64(2), np.int64(5)]
- frequency: [np.int64(10), np.int64(25), np.int64(50), np.int64(100), np.int64(200), np.int64(500)] Hz
- Cu=0, contamination=0, R_u=0 (fixes)

## Statistiques

| Metrique | Min | Mediane | Max |
|----------|-----|---------|-----|
| I_peak_nA | 751.781 | 3384.835 | 6282.203 |
| SNR | 237.700 | 1187.000 | 4040.500 |
| FWHM_mV | 56.000 | 60.000 | 64.000 |
| K_dimensionless | 0.050 | 0.525 | 5.000 |

## K optimal (Ni=0)

- Meilleur SNR = 4040.5 a f=500 Hz, RF=1.5
- K optimal = 0.09
