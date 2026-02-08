The surface quality of a gold electrode is critical for aptamer biosensor performance. In an industrial fabrication process, the gold layer may exhibit defects: variable roughness, partially exposed nickel or copper sublayers, or residual contamination. This study quantifies the impact of each parameter on the biosensor's SWV signal, in order to establish quality thresholds and identify the dominant factors.

**Contents:**
1. Electrode parameters
2. Physical model
3. Experimental design
4. Effect hierarchy
5. Bibliographical references

---

## 1. Electrode parameters

### 1.1 Roughness factor (RF)

The roughness factor is the ratio of the real surface area to the geometric surface area of the electrode:

$$\text{RF} = \frac{A_{real}}{A_{geometric}}$$

| Level | RF | Description |
|-------|----|-------------|
| 1 | 1.0 | Perfectly flat surface |
| 2 | 1.5 | Moderate roughness (typical) |
| 3 | 2.0 | Rough surface |
| 4 | 3.0 | Very rough |
| 5 | 5.0 | Extremely rough |

**Physical effects:**

- The real surface area increases proportionally with RF, which increases the capacitive current ($I_{baseline}$).
- The surface density of aptamers $\Gamma_{eff}$ increases with RF (more anchoring sites available).
- The peak current $I_{peak}$ increases with RF, but the ratio $I_{peak} / I_{baseline}$ may degrade if roughness promotes non-specific adsorption.
- An optimum is generally observed around $\text{RF} = 1.5$, where the gain in faradaic signal exceeds the increase in background noise.

### 1.2 Exposed nickel ($\text{Ni}_{exposed}$)

The percentage of surface area where the nickel underlayer is exposed through defects in the gold layer:

| Level | $\text{Ni}_{exposed}$ (%) | Description |
|-------|---------------------------|-------------|
| 1 | 0 | Intact gold layer |
| 2 | 3 | Minor defects |
| 3 | 5 | Moderate defects |
| 4 | 10 | Major defects |

**Physical effects:**

- Exposed nickel catalyses buffer decomposition and generates significant parasitic currents.
- The effective rate constant $k^0_{eff}$ is strongly reduced because Ni is unfavourable for MB electron transfer.
- The dominant effect is a **degradation of SNR by a factor of 10** when $\text{Ni}_{exposed}$ goes from 0 to 10 %.
- Exposed nickel is the most influential factor in this study on signal quality.

### 1.3 Exposed copper ($\text{Cu}_{exposed}$)

The percentage of surface area where the copper underlayer is exposed:

| Level | $\text{Cu}_{exposed}$ (%) | Description |
|-------|---------------------------|-------------|
| 1 | 0 | No exposure |
| 2 | 2 | Moderate exposure |
| 3 | 5 | Significant exposure |

**Physical effects:**

- At pH 7.4 (PBS buffer), copper is relatively stable and its effect is secondary compared to nickel.
- Cu contributes weakly to the background current and to a slight reduction of $k^0_{eff}$.
- The impact on SNR is measurable but remains a second-order factor.

### 1.4 Contamination (blocked sites)

The percentage of surface sites blocked by contaminants (organic residues, oxides):

| Level | Contamination (%) | Description |
|-------|-------------------|-------------|
| 1 | 0 | Clean surface |
| 2 | 15 | Moderate contamination |
| 3 | 30 | Heavy contamination |

**Physical effects:**

- Blocked sites cannot accommodate aptamers, reducing $\Gamma_{eff}$ proportionally:

$$\Gamma_{eff} = \Gamma_0 \times \left(1 - \frac{\text{contamination}}{100}\right)$$

- The peak current $I_{peak}$ decreases linearly with contamination.
- Contamination does not directly affect $k^0_{eff}$ or $E_{peak}$, but reduces SNR through signal reduction.

---

## 2. Physical model

### 2.1 Effective rate constant

The effective electron transfer rate constant depends on the exposed surface fractions:

$$k^0_{eff} = k^0_{Au} \cdot f_{Au} + k^0_{Ni} \cdot f_{Ni} + k^0_{Cu} \cdot f_{Cu}$$

where:
- $k^0_{Au} \gg k^0_{Ni},\; k^0_{Cu}$ (gold is the best conductor for MB electron transfer)
- $f_{Au} = 1 - f_{Ni} - f_{Cu} - f_{contamination}$ (free gold surface fraction)

In practice, since $k^0_{Ni}$ and $k^0_{Cu}$ are very small compared to $k^0_{Au}$, the reduction in $k^0_{eff}$ is primarily due to the decrease in available gold fraction.

### 2.2 Effective surface density

$$\Gamma_{eff} = \Gamma_0 \times \text{RF} \times \left(1 - \frac{\text{contamination}}{100}\right)$$

The roughness factor multiplies the available surface area while contamination reduces the fraction of accessible sites.

---

## 3. Experimental design

### 3.1 Objective

This study explores the influence of four electrode surface parameters on the voltammetric response of the aptamer biosensor. The goal is to quantify how gold surface quality affects each metric extracted from the SWV voltammogram.

### 3.2 Full factorial design

The design is a full factorial crossing all four parameters:

$$5 \;(\text{RF}) \times 4 \;(\text{Ni}) \times 3 \;(\text{Cu}) \times 3 \;(\text{contamination}) = 180 \text{ combinations}$$

### 3.3 Fixed parameters

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Frequency | 25 Hz | Standard reference frequency |
| $R_u$ | 0 $\Omega$ | Isolate electrode parameter effects |
| $\delta E_s$ | 4 mV | Standard SWV |
| $\delta E_p$ | 25 mV | Standard SWV |
| Temperature | 25 °C | Ambient conditions |
| pH | 7.4 | Physiological PBS buffer |

---

## 4. Effect hierarchy

### 4.1 Ranking by order of influence

| Rank | Factor | Main effect | Most affected metric |
|------|--------|-------------|----------------------|
| 1 | $\text{Ni}_{exposed}$ | Parasitic currents, reduction of $k^0_{eff}$ | SNR ($\div 10$ between 0 and 10 %) |
| 2 | RF | Increase in $I_{baseline}$ and $I_{peak}$ | $I_{baseline}$ ($\propto$ RF) |
| 3 | Contamination | Reduction of $\Gamma_{eff}$ | $I_{peak}$ ($-30$ % at 30 % contam.) |
| 4 | $\text{Cu}_{exposed}$ | Weak contribution to background current | SNR (secondary effect at pH 7.4) |

### 4.2 Expected results

1. **Exposed Ni**: dominant factor. SNR drops by a factor of $\sim 10$ between 0 and 10 % exposed Ni, primarily because parasitic currents increase the noise.
2. **RF**: increases $I_{baseline}$ proportionally. Optimum around $\text{RF} = 1.5$ for the signal-to-noise trade-off.
3. **Contamination**: reduces $I_{peak}$ linearly. At 30 %, the signal is reduced by nearly one-third.
4. **Exposed Cu**: secondary effect at pH 7.4. Measurable contribution but not dominant.

---

## 5. Bibliographical references

*For the complete list of references, see the Bibliographical References section in the Appendices menu.*
