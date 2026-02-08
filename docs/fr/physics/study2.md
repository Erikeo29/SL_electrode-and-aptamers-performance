La fréquence de la voltammétrie à onde carrée est un levier d'optimisation puissant pour les biocapteurs à aptamères. En augmentant la fréquence, on accroît le courant de pic (meilleure sensibilité), mais on risque de basculer dans un régime cinétique irréversible où le signal se dégrade. Cette étude explore systématiquement l'interaction entre la fréquence et l'état de surface de l'électrode pour identifier les conditions optimales de mesure.

**Sommaire :**
1. Physique de l'effet de fréquence
2. Interactions fréquence–électrode
3. Plan expérimental
4. Résultats attendus
5. Références bibliographiques

---

## 1. Physique de l'effet de fréquence

### 1.1 Relation courant–fréquence

Pour un système quasi-réversible à espèces adsorbées (cas du MB lié à l'aptamère), le courant de pic SWV dépend de la fréquence selon :

$$I_{peak} \propto n \cdot F \cdot A \cdot \Gamma_{eff} \cdot f \cdot \Delta\psi$$

où :
- $n = 2$ (nombre d'électrons pour MB)
- $F = 96\,485$ C/mol (constante de Faraday)
- $A$ = surface réelle de l'électrode (cm²)
- $\Gamma_{eff}$ = densité surfacique effective d'aptamères (mol/cm²)
- $f$ = fréquence SWV (Hz)
- $\Delta\psi$ = fonction adimensionnelle du courant net, dépendante de $K$ et $\delta E_p$

Dans le régime quasi-réversible, $I_{peak}$ croît approximativement linéairement avec $f$. Cette linéarité est exploitée pour optimiser la sensibilité du biocapteur.

### 1.2 Paramètre cinétique adimensionnel $K$

Le paramètre $K$ relie la constante de vitesse de transfert d'électron à la fréquence :

$$K = \frac{k^0_{eff}}{f}$$

À mesure que $f$ augmente, $K$ diminue et le système évolue du régime réversible vers le régime irréversible :

| Fréquence (Hz) | $K$ (pour $k^0_{eff} = 50$ s⁻¹) | Régime |
|-----------------|----------------------------------|--------|
| 10 | 5.0 | Réversible |
| 25 | 2.0 | Quasi-réversible |
| 50 | 1.0 | Quasi-réversible |
| 100 | 0.5 | Quasi-réversible |
| 200 | 0.25 | Quasi-réversible / irréversible |
| 500 | 0.1 | Irréversible |

### 1.3 Déplacement du potentiel de pic

À haute fréquence ($K$ faible), le pic SWV se dédouble en deux composantes : la composante *forward* se déplace vers des potentiels plus négatifs et la composante *reverse* vers des potentiels plus positifs. Le pic net ($I_{forward} - I_{reverse}$) montre un déplacement apparent de $E_{peak}$ et un élargissement.

Pour un système purement réversible ($K \gg 1$), $E_{peak}$ reste constant et égal à $E^0$ quelle que soit la fréquence.

### 1.4 Élargissement de la FWHM

La FWHM augmente avec la fréquence en raison de la transition vers le régime irréversible :

- À 10 Hz ($K = 5$) : FWHM proche de la valeur idéale ($45.3$ mV).
- À 500 Hz ($K = 0.1$) : FWHM significativement élargie ($> 100$ mV).

L'élargissement suit une relation monotone avec $1/K$ et peut être modélisé par les équations de Lovric pour la SWV de systèmes adsorbés.

---

## 2. Interactions fréquence–électrode

### 2.1 Interaction RF $\times$ fréquence

Le facteur de rugosité amplifie l'effet de la fréquence sur $I_{peak}$ car il multiplie la surface effective :

$$I_{peak}(\text{RF},\, f) \propto \text{RF} \cdot f$$

Cependant, $I_{baseline}$ augmente aussi avec RF, de sorte que le gain en SNR n'est pas proportionnel à RF.

### 2.2 Interaction Ni $\times$ fréquence

À basse fréquence ($K$ élevé), le système a le temps d'atteindre l'équilibre même avec un $k^0_{eff}$ réduit par l'exposition au nickel. À haute fréquence, la réduction de $k^0_{eff}$ due au Ni se traduit par une chute plus marquée du courant car le système bascule dans le régime irréversible plus tôt.

L'interaction Ni $\times$ fréquence est donc **synergique et négative** : les électrodes avec Ni exposé sont encore plus pénalisées à haute fréquence.

| Condition | $k^0_{eff}$ (s⁻¹) | $K$ à 25 Hz | $K$ à 200 Hz | Conséquence à haute fréquence |
|-----------|---------------------|-------------|--------------|-------------------------------|
| Ni = 0 % | $\sim 50$ | 2.0 | 0.25 | Quasi-réversible |
| Ni = 10 % | $\sim 20$ | 0.8 | 0.10 | Irréversible |

---

## 3. Plan expérimental

### 3.1 Objectif

Cette étude examine l'influence de la fréquence de la voltammétrie à onde carrée sur la réponse du biocapteur à aptamère, en interaction avec les paramètres de surface d'électrode (RF et Ni exposé). L'objectif est de comprendre comment le régime cinétique évolue avec la fréquence et d'identifier les conditions optimales de mesure.

### 3.2 Facteurs et niveaux

| Facteur | Niveaux | Valeurs |
|---------|---------|---------|
| RF | 4 | 1.0, 1.5, 2.0, 3.0 |
| $\text{Ni}_{exposed}$ | 3 | 0, 3, 10 % |
| Fréquence $f$ | 6 | 10, 25, 50, 100, 200, 500 Hz |

### 3.3 Nombre total de combinaisons

$$4 \;(\text{RF}) \times 3 \;(\text{Ni}) \times 6 \;(f) = 72 \text{ combinaisons}$$

### 3.4 Paramètres fixes

| Paramètre | Symbole | Valeur | Justification |
|-----------|---------|--------|---------------|
| Cuivre exposé | $\text{Cu}_{exposed}$ | 0 % | Isoler l'effet fréquence–électrode |
| Contamination | — | 0 % | Surface propre de référence |
| Résistance non compensée | $R_u$ | 0 $\Omega$ | Pas de chute ohmique |
| Incrément de potentiel | $\delta E_s$ | 4 mV | Standard SWV |
| Amplitude d'impulsion | $\delta E_p$ | 25 mV | Standard SWV |

Le cuivre exposé, la contamination et la résistance non compensée sont fixés à zéro pour isoler exclusivement l'interaction entre la fréquence et les paramètres d'électrode dominants (RF et Ni).

---

## 4. Résultats attendus

### 4.1 Synthèse par métrique

| Métrique | Comportement attendu |
|----------|---------------------|
| $I_{peak}$ vs $f$ | Croissance $\approx$ linéaire sans Ni ; sous-linéarité avec Ni exposé |
| $E_{peak}$ vs $f$ | Stable à basse $f$, déplacement négatif à haute $f$ ; amplifié par Ni |
| FWHM vs $f$ | Élargissement progressif ; plus marqué pour les électrodes à Ni exposé |
| SNR vs $f$ | Augmente puis se dégrade à haute $f$ ; fréquence optimale dépendante de l'état de surface |
| $K$ vs $f$ | Décroissance hyperbolique ($K = k^0_{eff}/f$) |

### 4.2 Interprétation physique

1. **$I_{peak}$ vs $f$** : croissance approximativement linéaire pour les électrodes sans Ni. Sous-linéarité pour les électrodes avec Ni exposé (transition vers l'irréversibilité).
2. **$E_{peak}$ vs $f$** : stable à basse fréquence, déplacement négatif à haute fréquence. Déplacement amplifié par l'exposition au Ni.
3. **FWHM vs $f$** : élargissement progressif avec la fréquence. Plus marqué pour les électrodes à Ni exposé.
4. **SNR vs $f$** : augmente d'abord avec $f$ (plus de signal), puis se dégrade à haute fréquence (élargissement du pic et perte de courant). Fréquence optimale dépendante de l'état de surface.
5. **$K$ vs $f$** : décroissance hyperbolique ($K = k^0_{eff}/f$). Permet de cartographier le régime cinétique pour chaque combinaison électrode–fréquence.

---

## 5. Références bibliographiques

*Pour la liste complète des références, consultez la section Références bibliographiques dans le menu Annexes.*
