**Contents:**
1. Overview
2. Comparison table
3. Factor hierarchy
4. Recommendations

---

## 1. Overview

The three parametric studies systematically explore the factors influencing the SWV response of an aptamer biosensor with a methylene blue (MB) redox reporter on Au/Ni/Cu electrodes. Each study isolates a specific group of variables while fixing the others, then quantifies the impact on the metrics extracted from the voltammogram ($I_{peak}$, $E_{peak}$, FWHM, SNR, $IR_{drop}$, $K$).

Together, the results cover electrode surface quality, kinetic regime mapping, and electrical contact quality.

---

## 2. Comparison table

| Characteristic | Study 1 | Study 2 | Study 3 |
|:---------------|:--------|:--------|:--------|
| **Title** | Electrode parameters | Frequency effect | Ohmic drop coupling |
| **Variables** | RF, Ni%, Cu%, contamination | RF, Ni%, frequency | RF, Ni%, $R_u$ |
| **RF range** | 1 -- 5 | 1 -- 5 | 1 -- 5 |
| **Ni% range** | 0 -- 10% | 0 -- 10% | 0 -- 10% |
| **Cu% range** | 0 -- 5% | 0% (fixed) | 0% (fixed) |
| **Contamination** | 0 -- 30% | 0% (fixed) | 0% (fixed) |
| **Frequency** | 25 Hz (fixed) | 10 -- 500 Hz | 25 Hz (fixed) |
| **$R_u$** | 0 $\Omega$ (fixed) | 0 $\Omega$ (fixed) | 0 -- 1000 $\Omega$ |
| **Primary objective** | Surface quality | Kinetic regime | Contact quality |
| **Key metric** | SNR | $K = k^0_{eff}/f$ | $IR_{drop}$ |
| **Key equation** | $\Gamma_{eff} = \Gamma_0 \cdot \text{RF} \cdot (1 - \text{contam.}/100)$ | $K = k^0_{eff}/f$ | $\eta = E_{applied} - I R_u - E^0$ |
| **Iterative coupling** | No | No | Yes (fixed-point) |

---

## 3. Factor hierarchy

The three studies together establish a ranked hierarchy of the six factors affecting biosensor performance, ordered from the most influential to the least influential.

### 3.1 Exposed nickel -- dominant effect

| Aspect | Detail |
|--------|--------|
| **Rank** | 1 / 6 |
| **Mechanism** | Ni catalyzes parasitic reactions and reduces $k^0_{eff}$ |
| **Quantitative impact** | SNR drops by a factor of $\sim 10$ when Ni% goes from 0 to 10% |
| **Relevant studies** | Studies 1, 2, 3 |
| **Interaction with frequency** | Synergistic and negative: at high frequency, the Ni penalty is amplified because the system transitions to the irreversible regime earlier ($K \propto k^0_{eff}/f$) |

### 3.2 Roughness factor (RF) -- signal/noise trade-off

| Aspect | Detail |
|--------|--------|
| **Rank** | 2 / 6 |
| **Mechanism** | RF multiplies the real surface area, proportionally increasing both $\Gamma_{eff}$ and $I_{baseline}$ |
| **Quantitative impact** | $I_{baseline} \propto \text{RF}$; SNR has an optimum around RF $\approx 1.5$ |
| **Relevant studies** | Studies 1, 2, 3 |
| **Interaction with $R_u$** | High RF amplifies the ohmic drop (larger currents through $R_u$) |

### 3.3 Contamination -- linear signal reduction

| Aspect | Detail |
|--------|--------|
| **Rank** | 3 / 6 |
| **Mechanism** | Blocked sites cannot accommodate aptamers, reducing $\Gamma_{eff}$ proportionally |
| **Quantitative impact** | At 30% contamination, $I_{peak}$ is reduced by approximately one-third |
| **Relevant studies** | Study 1 |
| **Interactions** | No direct interaction with $k^0_{eff}$ or $E_{peak}$ |

### 3.4 Exposed copper -- secondary effect at pH 7.4

| Aspect | Detail |
|--------|--------|
| **Rank** | 4 / 6 |
| **Mechanism** | Weak contribution to background current and mild $k^0_{eff}$ reduction |
| **Quantitative impact** | Measurable but not dominant; effect significantly lower than Ni |
| **Relevant studies** | Study 1 |
| **Note** | Cu effect could be more pronounced at acidic pH or in the presence of complexing agents |

### 3.5 Frequency -- sensitivity lever

| Aspect | Detail |
|--------|--------|
| **Rank** | 5 / 6 (optimization lever, not a degradation factor) |
| **Mechanism** | $I_{peak}$ increases approximately linearly with $f$ in the quasi-reversible regime; $K = k^0_{eff}/f$ determines the kinetic regime |
| **Quantitative impact** | Signal increase by a factor of $\sim 20$ between 10 and 200 Hz (clean electrode); beyond $\sim 200$ Hz, the transition to irreversibility limits the gain |
| **Relevant studies** | Study 2 |
| **Associated shifts** | $E_{peak}$ shifts and FWHM broadens at high frequency |

### 3.6 Uncompensated resistance ($R_u$) -- moderate effect at 25 Hz

| Aspect | Detail |
|--------|--------|
| **Rank** | 6 / 6 |
| **Mechanism** | Linear ohmic drop $IR_{drop} = I_{peak} \times R_u$; RC filtering effect on fast current components |
| **Quantitative impact** | For nA-level currents at 25 Hz, $IR_{drop} < 0.1$ mV even at $R_u = 1000\;\Omega$; FWHM broadening is the main observable effect |
| **Relevant studies** | Study 3 |
| **Interaction with RF** | Amplified with rough electrodes (larger currents) |

### 3.7 Impact summary

| Rank | Factor | Impact on SNR | Character |
|-----:|--------|:--------------|:----------|
| 1 | Exposed Ni (Ni%) | Very strong | Degradation |
| 2 | Roughness factor (RF) | Strong, with optimum | Trade-off |
| 3 | Contamination | Moderate, linear | Degradation |
| 4 | Exposed Cu (Cu%) | Weak at pH 7.4 | Degradation |
| 5 | Frequency ($f$) | Strong | Optimization lever |
| 6 | $R_u$ | Weak at 25 Hz / nA | Degradation |

---

## 4. Recommendations

### 4.1 Electrode fabrication

| Parameter | Recommended range | Rationale |
|-----------|-------------------|-----------|
| Ni% | $< 3\%$ | Dominant degradation factor; above 3%, SNR drops sharply |
| RF | 1.2 -- 2.0 | Best signal-to-noise trade-off; higher RF increases baseline noise |
| Contamination | $< 10\%$ | Linear signal loss; rigorous cleaning protocol required |
| Cu% | $< 2\text{--}3\%$ | Tolerable under physiological conditions (pH 7.4) |

### 4.2 Measurement conditions

| Parameter | Recommended value | Rationale |
|-----------|-------------------|-----------|
| Frequency ($f$) | 25 -- 100 Hz | 25 Hz is a good general compromise; higher frequencies improve sensitivity but risk irreversibility, especially with exposed Ni |
| $R_u$ | $< 200\;\Omega$ | Optimal conditions; up to 500 $\Omega$ remains acceptable at 25 Hz with nA currents |

### 4.3 Key conclusion

Gold layer quality (absence of exposed Ni, controlled roughness, low contamination) is the predominant factor for biosensor performance. SWV frequency is a powerful optimization lever but is constrained by the kinetic regime ($K = k^0_{eff}/f$). Uncompensated resistance is a secondary factor under typical measurement conditions (25 Hz, nA-level currents).
