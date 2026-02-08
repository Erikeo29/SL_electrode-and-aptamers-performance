Les biocapteurs électrochimiques à aptamères reposent sur la mesure d'un signal redox pour détecter des molécules cibles en temps réel. L'interrogation du capteur se fait par voltammétrie à onde carrée (SWV), une technique pulsée offrant une sensibilité et un rapport signal-sur-bruit nettement supérieurs à la voltammétrie cyclique classique (CV).

Cette page présente le principe de la SWV, le rapporteur redox utilisé (bleu de méthylène) et les métriques quantitatives extraites du voltammogramme. Ces métriques constituent la base d'analyse des trois études paramétriques de cette application.

**Sommaire :**
1. Principe de la voltammétrie à onde carrée
2. Pic de bleu de méthylène
3. Métriques extraites du voltammogramme
4. Tableau récapitulatif des métriques

---

## 1. Principe de la voltammétrie à onde carrée

### 1.1 Pourquoi la SWV plutôt que la CV ?

La voltammétrie cyclique (CV) est la technique électrochimique la plus courante, mais elle mélange courant faradique (signal utile) et courant capacitif (bruit de fond). La SWV résout ce problème en soustrayant deux mesures de courant prises à des instants symétriques, éliminant ainsi la composante capacitive. En pratique, la SWV permet d'atteindre des limites de détection 10 à 100 fois plus basses que la CV.

![Comparaison des formes d'onde et voltammogrammes : CV (haut) vs SWV (bas)](../../../assets/illustrations/swv_vs_cv_waveform.png)

### 1.2 Forme d'onde

La voltammétrie à onde carrée (Square Wave Voltammetry, SWV) superpose deux signaux sur le potentiel de travail :

1. **Escalier (*staircase*)** : incrément de potentiel $\delta E_s = 4$ mV à chaque cycle.
2. **Impulsions symétriques** : amplitude $\pm\,\delta E_p = 25$ mV autour de chaque marche.

À chaque marche de l'escalier, une impulsion positive (*forward*) puis une impulsion négative (*reverse*) sont appliquées. Le courant est échantillonné à la fin de chaque impulsion, lorsque le courant capacitif a décru exponentiellement.

### 1.3 Courant net

Le courant net est défini par :

$$I_{net} = I_{forward} - I_{reverse}$$

Cette soustraction élimine la composante capacitive (courant de charge de la double couche), identique en amplitude pour les deux impulsions. Seul le courant faradique, proportionnel à la concentration de l'espèce électroactive, est conservé. La SWV offre ainsi un rapport signal-sur-bruit nettement supérieur à celui de la CV.

### 1.4 Paramètres typiques

| Paramètre | Symbole | Valeur typique |
|-----------|---------|----------------|
| Incrément de potentiel | $\delta E_s$ | 4 mV |
| Amplitude d'impulsion | $\delta E_p$ | 25 mV |
| Fréquence | $f$ | 10 – 500 Hz |
| Potentiel initial | $E_{start}$ | −0.05 V |
| Potentiel final | $E_{end}$ | −0.45 V |

---

## 2. Pic de bleu de méthylène

### 2.1 Rapporteur redox

Le bleu de méthylène (MB) est un colorant cationique de la famille des **phénothiazines**, largement utilisé comme rapporteur redox dans les biocapteurs E-AB. Sa structure comporte :

- un **noyau tricyclique phénothiazinique** : deux cycles benzéniques fusionnés à un cycle central thiazine contenant un atome de soufre (S) et un atome d'azote (N) ;
- deux groupes **diméthylamino** —N(CH₃)₂ en positions 3 et 7, responsables de la couleur bleue ;
- un **groupe méthyle** —CH₃ sur l'azote central du cycle thiazine, conférant à la molécule sa charge positive permanente.

> Formule brute : C₁₆H₁₈N₃S⁺ (cation) · Cl⁻ (contre-ion) — masse molaire : 319,85 g/mol.

Le MB est conjugué de manière covalente à l'extrémité distale (5') de l'aptamère, lui-même ancré sur la surface d'or de l'électrode via une liaison thiol (extrémité 3').

### 2.2 Réaction redox

La réaction redox du bleu de méthylène implique deux électrons et deux protons :

$$\text{MB}_{ox} + 2e^- + 2H^+ \rightleftharpoons \text{MB}_{red}$$

Le pic de courant est centré autour du potentiel standard apparent :

$$E^0 = -0.24 \text{ V vs Ag/AgCl} \quad (\text{pH } 7.4, \text{ tampon PBS})$$

Le potentiel $E^0$ dépend du pH selon la relation de Nernst : déplacement d'environ $-59$ mV par unité de pH à 25 °C pour un processus impliquant autant de protons que d'électrons.

### 2.3 Mécanisme de détection

En l'absence de cible, l'aptamère adopte une conformation qui maintient le MB proche de la surface de l'électrode, permettant un transfert d'électrons efficace. Lorsque la cible se lie à l'aptamère, le changement conformationnel éloigne le MB de la surface, réduisant le courant de pic. La variation de courant est proportionnelle à la concentration de cible.

![Principe du biocapteur E-AB : sans cible (gauche) vs avec cible (droite)](../../../assets/illustrations/eab_biosensor_structure.png)

---

## 3. Métriques extraites du voltammogramme

### 3.1 $I_{peak}$ — courant de pic (nA)

L'amplitude maximale du pic faradique après soustraction de la ligne de base. Directement proportionnel à :

- La densité surfacique d'aptamères électroactifs $\Gamma_{eff}$ (mol/cm²)
- La fréquence SWV $f$ (Hz)
- Le nombre d'électrons échangés ($n = 2$ pour MB)

### 3.2 $E_{peak}$ — potentiel de pic (V)

Potentiel auquel le courant net atteint son maximum. Pour un système réversible, $E_{peak} \approx E^0$. Un déplacement par rapport à la valeur attendue ($-0.24$ V) peut indiquer :

- Une résistance non compensée (déplacement ohmique $IR$)
- Un changement d'environnement local (pH, force ionique)
- Des effets cinétiques à haute fréquence

### 3.3 FWHM — largeur à mi-hauteur (mV)

La largeur totale à mi-hauteur du pic SWV. Pour un système idéal nernstien avec $n$ électrons :

$$\text{FWHM}_{idéal} = \frac{90.6}{n} \text{ mV} \quad (25\,°\text{C})$$

Pour le bleu de méthylène ($n = 2$) : $\text{FWHM}_{idéal} = 45.3$ mV. Un élargissement au-delà de cette valeur indique une quasi-réversibilité cinétique, une hétérogénéité de surface ou une résistance non compensée.

### 3.4 SNR — rapport signal-sur-bruit

$$\text{SNR} = \frac{I_{peak}}{\sigma_{résidus}}$$

Un SNR $> 10$ est généralement requis pour une mesure quantitative fiable. Un SNR $> 50$ est considéré comme excellent.

### 3.5 $I_{baseline}$ — courant de ligne de base (µA)

Le courant de fond mesuré loin du pic faradique, reflétant la contribution capacitive résiduelle et les courants parasites. Proportionnel à la surface réelle de l'électrode ($\propto \text{RF}$) et à la capacité de double couche $C_{dl}$.

### 3.6 $IR_{drop}$ — chute ohmique (mV)

$$IR_{drop} = I_{peak} \times R_u$$

Ce déplacement décale le pic vers des potentiels plus négatifs et l'élargit. Aux courants de l'ordre du nanoampère et avec $R_u < 100\;\Omega$, le $IR_{drop}$ reste généralement négligeable ($< 1$ mV).

### 3.7 $K$ — paramètre cinétique adimensionnel

$$K = \frac{k^0_{eff}}{f}$$

où $k^0_{eff}$ est la constante de vitesse de transfert d'électron effective (s⁻¹) et $f$ la fréquence SWV (Hz).

| Régime | Valeur de $K$ | Comportement |
|--------|---------------|--------------|
| Réversible | $K > 5$ | Pic fin, $E_{peak} = E^0$ |
| Quasi-réversible | $0.1 < K < 5$ | Pic élargi, $E_{peak}$ se déplace |
| Irréversible | $K < 0.1$ | Pic très large, courant réduit |

Pour les biocapteurs à aptamères avec MB, $k^0_{eff}$ est typiquement de l'ordre de 10 à 100 s⁻¹, plaçant le système en régime quasi-réversible aux fréquences SWV habituelles (25–200 Hz).

---

## 4. Tableau récapitulatif des métriques

| Métrique | Symbole | Unité | Valeur typique (25 Hz, électrode propre) | Sensible à |
|----------|---------|-------|------------------------------------------|------------|
| Courant de pic | $I_{peak}$ | nA | 30 – 80 | RF, Ni, contamination, $f$ |
| Potentiel de pic | $E_{peak}$ | V | −0.24 | $R_u$, $f$ (haute), Ni |
| Largeur à mi-hauteur | FWHM | mV | 45 – 60 | $f$, $R_u$, Ni |
| Rapport signal/bruit | SNR | — | 50 – 200 | Ni (dominant), RF, contamination |
| Courant de base | $I_{baseline}$ | µA | 0.1 – 1.0 | RF ($\propto$ RF) |
| Chute ohmique | $IR_{drop}$ | mV | < 0.1 | $R_u$, RF × $R_u$ |
| Paramètre cinétique | $K$ | — | 0.2 – 4.0 | $f$, Ni (via $k^0_{eff}$) |
