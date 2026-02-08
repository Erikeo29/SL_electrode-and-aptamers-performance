### Results analysis — study 3: uncompensated resistance

The plots below show the influence of $R_u$ (0 to 1000 $\Omega$) on SWV metrics, for different RF and exposed Ni combinations. Key observations:

- **$IR_{drop}$ vs $R_u$**: linear relationship for each combination, with slope proportional to $I_{peak}$. Rough electrodes (RF = 3) exhibit an ohmic drop approximately 3 times greater than flat electrodes (RF = 1).

- **$E_{peak}$ vs $R_u$**: shift towards more negative potentials, but very small in absolute value (< 0.1 mV even at $R_u = 1000\;\Omega$) because currents are in the nanoampere range.

- **FWHM vs $R_u$**: this is the main effect of uncompensated resistance. Progressive peak broadening reduces resolution and may affect the precision of Gaussian fitting. The effect is more pronounced for high-RF electrodes.

- **Practical conclusion**: at 25 Hz with nA currents, uncompensated resistance is a secondary factor. Recommended thresholds are $R_u < 200\;\Omega$ (optimal) and $R_u < 500\;\Omega$ (acceptable).
