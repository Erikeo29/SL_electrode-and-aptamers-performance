Glossaire des termes, acronymes et symboles utilisés dans la documentation du biocapteur à aptamère SWV.

**Sommaire :**
1. Acronymes et techniques
2. Symboles physiques
3. Métriques SWV
4. Paramètres de surface
5. Termes techniques

---

## 1. Acronymes et techniques

| Acronyme | Signification | Description |
|----------|---------------|-------------|
| **SWV** | Square Wave Voltammetry | Voltammétrie à onde carrée. Technique électroanalytique pulsée superposant un signal carré symétrique ($\pm\,\delta E_p$) à un escalier de potentiel ($\delta E_s$). Le courant net $I_{net} = I_{forward} - I_{reverse}$ élimine la composante capacitive. |
| **CV** | Cyclic Voltammetry | Voltammétrie cyclique. Balayage linéaire du potentiel entre deux bornes. Moins sensible que la SWV. |
| **EIS** | Electrochemical Impedance Spectroscopy | Spectroscopie d'impédance électrochimique. Technique complémentaire mesurant la réponse en fréquence pour extraire $R_u$, $C_{dl}$, $R_{ct}$. |
| **MB** | Methylene Blue | Bleu de méthylène. Rapporteur redox phénothiazinique : $\text{MB}_{ox} + 2e^- + 2H^+ \rightleftharpoons \text{MB}_{red}$, $E^0 = -0.24$ V vs Ag/AgCl (pH 7.4). |
| **CPE** | Constant Phase Element | Élément à phase constante. Modélise un comportement non idéal de la capacité : $Z_{CPE} = 1 / [Q_0(j\omega)^{n_{CPE}}]$ avec $0 < n_{CPE} \leq 1$. |
| **BV** | Butler-Volmer | Modèle cinétique reliant le courant faradique à la surtension. |
| **FEM** | Finite Element Method | Méthode des éléments finis. Approche numérique de résolution des EDP. |
| **SELEX** | Systematic Evolution of Ligands by Exponential Enrichment | Procédé de sélection *in vitro* des aptamères. |
| **PBS** | Phosphate-Buffered Saline | Tampon phosphate salin (pH 7.4). Milieu électrolytique de référence. |
| **WE** | Working Electrode | Électrode de travail (lieu de la réaction d'intérêt). |
| **RE** | Reference Electrode | Électrode de référence (potentiel stable, ex. Ag/AgCl). |
| **CE** | Counter Electrode | Électrode auxiliaire (ferme le circuit). |
| **SNR** | Signal-to-Noise Ratio | Rapport signal-sur-bruit. |
| **FWHM** | Full Width at Half Maximum | Largeur totale à mi-hauteur du pic SWV. |
| **RF** | Roughness Factor | Facteur de rugosité : $\text{RF} = A_{réelle} / A_{géométrique}$. |

---

## 2. Symboles physiques

### 2.1 Constantes fondamentales

| Symbole | Nom | Valeur | Unité |
|---------|-----|--------|-------|
| $F$ | Constante de Faraday | 96 485 | C/mol |
| $R$ | Constante des gaz parfaits | 8.314 | J/(mol·K) |
| $T$ | Température | 298.15 (25 °C) | K |
| $n$ | Nombre d'électrons transférés | 2 (pour MB) | — |

### 2.2 Paramètres de potentiel

| Symbole | Nom | Unité | Description |
|---------|-----|-------|-------------|
| $E$ | Potentiel d'électrode | V | Potentiel appliqué par le potentiostat |
| $E^0$ | Potentiel standard apparent | V | $-0.24$ V vs Ag/AgCl pour MB (pH 7.4) |
| $\eta$ | Surtension | V | $\eta = E - E^0$ (sans $R_u$) ou $\eta = E_{appliqué} - I R_u - E^0$ |
| $\delta E_s$ | Incrément de potentiel (escalier) | V | Typiquement 4 mV |
| $\delta E_p$ | Amplitude d'impulsion | V | Typiquement 25 mV |
| $E_{start}$ | Potentiel initial | V | $-0.05$ V |
| $E_{end}$ | Potentiel final | V | $-0.45$ V |

### 2.3 Paramètres cinétiques

| Symbole | Nom | Unité | Description |
|---------|-----|-------|-------------|
| $k^0_{eff}$ | Constante de vitesse effective | s⁻¹ | Moyenne pondérée sur la composition de surface |
| $k^0_{Au}$ | Constante de vitesse sur or | s⁻¹ | $\sim 10$–$100$ s⁻¹ pour MB adsorbé |
| $k^0_{Ni}$ | Constante de vitesse sur nickel | s⁻¹ | Très inférieure à $k^0_{Au}$ |
| $k^0_{Cu}$ | Constante de vitesse sur cuivre | s⁻¹ | Inférieure à $k^0_{Au}$ |
| $\alpha$ | Coefficient de transfert | — | Généralement 0.5 (symétrie de la barrière d'activation) |
| $K$ | Paramètre cinétique adimensionnel | — | $K = k^0_{eff} / f$ |

### 2.4 Paramètres de transport

| Symbole | Nom | Unité | Description |
|---------|-----|-------|-------------|
| $C$ | Concentration du MB | mol/m³ | Variable résolue par le solveur FEM |
| $C_{ox}$ | Concentration de la forme oxydée | mol/m³ | À la surface de l'électrode |
| $C_{red}$ | Concentration de la forme réduite | mol/m³ | À la surface de l'électrode |
| $D$ | Coefficient de diffusion dans le film | m²/s | $\sim 10^{-12}$ m²/s |
| $L$ | Épaisseur du film d'aptamères | m | Typiquement 2–5 nm |

### 2.5 Paramètres électriques

| Symbole | Nom | Unité | Description |
|---------|-----|-------|-------------|
| $R_u$ | Résistance non compensée | $\Omega$ | Solution + contacts + films de surface |
| $C_{dl}$ | Capacité de double couche | F/m² (ou µF/cm²) | Typiquement 10–40 µF/cm² pour Au en PBS |
| $I$ | Courant | A | Courant total traversant le circuit |
| $j$ | Flux molaire à la surface | mol/(m²·s) | Issu de la cinétique de Butler-Volmer |

---

## 3. Métriques SWV

| Symbole | Nom | Unité | Description |
|---------|-----|-------|-------------|
| $I_{peak}$ | Courant de pic | nA | Amplitude maximale du pic faradique après soustraction de la ligne de base |
| $E_{peak}$ | Potentiel de pic | V | Potentiel au maximum du courant net. $E_{peak} \approx E^0$ en régime réversible |
| FWHM | Largeur à mi-hauteur | mV | $\text{FWHM}_{idéal} = 90.6 / n$ mV (45.3 mV pour MB). Un élargissement indique une quasi-réversibilité ou une hétérogénéité |
| SNR | Rapport signal-sur-bruit | — | $\text{SNR} = I_{peak} / \sigma_{résidus}$. $> 10$ : quantitatif ; $> 50$ : excellent |
| $I_{baseline}$ | Courant de ligne de base | µA | Courant de fond mesuré loin du pic. $\propto \text{RF} \times C_{dl}$ |
| $IR_{drop}$ | Chute ohmique | mV | $IR_{drop} = I_{peak} \times R_u$. Décale et élargit le pic |
| $I_{net}$ | Courant net | A | $I_{net} = I_{forward} - I_{reverse}$ |
| $I_{forward}$ | Courant *forward* | A | Courant échantillonné à la fin de l'impulsion positive |
| $I_{reverse}$ | Courant *reverse* | A | Courant échantillonné à la fin de l'impulsion négative |

---

## 4. Paramètres de surface

| Symbole | Nom | Unité | Description |
|---------|-----|-------|-------------|
| RF | Facteur de rugosité | — | $A_{réelle} / A_{géométrique}$. RF $= 1$ : surface plane. Typique Au électrodéposé : 1.2–3.0 |
| $A_{géométrique}$ | Surface géométrique | m² (ou cm²) | Surface projetée de l'électrode |
| $A_{réelle}$ | Surface réelle | m² (ou cm²) | $A_{réelle} = A_{géométrique} \times \text{RF}$ |
| $\Gamma_0$ | Densité surfacique nominale | mol/cm² | Densité d'aptamères par unité de surface d'or propre ($10^{-11}$–$10^{-10}$) |
| $\Gamma_{eff}$ | Densité surfacique effective | mol/cm² | $\Gamma_{eff} = \Gamma_0 \times \text{RF} \times (1 - \text{contamination}/100)$ |
| $f_{Au}$ | Fraction d'or libre | — | $f_{Au} = 1 - \text{Ni}_{exp}/100 - \text{Cu}_{exp}/100 - \text{contamination}/100$ |
| $\text{Ni}_{exp}$ | Nickel exposé | % | Fraction de surface occupée par le nickel |
| $\text{Cu}_{exp}$ | Cuivre exposé | % | Fraction de surface occupée par le cuivre |
| Contamination | Contamination de surface | % | Fraction de surface bloquée (organique, résidus) |

---

## 5. Termes techniques

### 5.1 Électrochimie et biocapteurs

| Terme | Définition |
|-------|------------|
| **Aptamère** | Oligonucléotide (ADN ou ARN simple brin) sélectionné par SELEX pour sa capacité à se lier spécifiquement à une molécule cible. Ancré sur l'or via une liaison thiol (extrémité 3'), portant un rapporteur redox (MB) à l'extrémité 5'. |
| **Rapporteur redox** | Molécule électroactive conjuguée à l'aptamère (ici le bleu de méthylène) dont le signal varie avec la conformation de l'aptamère. |
| **Voltammogramme** | Courbe $I = f(E)$ obtenue lors du balayage de potentiel. |
| **Courant faradique** | Courant dû au transfert d'électrons lors de la réaction redox. Proportionnel à la concentration de l'espèce électroactive. |
| **Courant capacitif** | Courant de charge de la double couche électrique. Éliminé par la soustraction *forward* − *reverse* en SWV. |
| **Double couche** | Interface métal/solution avec séparation de charge, caractérisée par la capacité $C_{dl}$. |
| **Réversible** | Régime où le transfert d'électrons est rapide devant la fréquence ($K > 5$). Pic fin, $E_{peak} = E^0$. |
| **Quasi-réversible** | Régime intermédiaire ($0.1 < K < 5$). Pic élargi, $E_{peak}$ se déplace. |
| **Irréversible** | Régime limité par la cinétique ($K < 0.1$). Pic très large, courant fortement réduit. |
| **Chute ohmique** | Perte de potentiel $IR_{drop} = I \cdot R_u$ dans la résistance non compensée entre WE et RE. |

### 5.2 Méthodes numériques

| Terme | Définition |
|-------|------------|
| **Maillage** | Discrétisation spatiale du domaine de calcul (ici le film d'aptamères). |
| **Éléments P1** | Éléments finis de Lagrange de degré 1 (linéaires). |
| **Euler implicite** | Schéma temporel inconditionnellement stable (*backward Euler*). |
| **Firedrake** | Bibliothèque Python open-source de résolution d'EDP par éléments finis. |
| **Boucle itérative** | Algorithme de point fixe résolvant le couplage non linéaire $I$–$R_u$ à chaque pas de temps (étude 3). |
| **Ajustement gaussien** | Modélisation du pic SWV par une gaussienne superposée à un polynôme de degré 2 pour extraire les métriques. |
| **Formulation faible** | Forme intégrale des équations aux dérivées partielles, base de la méthode des éléments finis. |
