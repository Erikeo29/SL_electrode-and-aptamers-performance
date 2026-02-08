En pratique, la connexion entre l'électrode de travail et le potentiostat n'est jamais parfaite : résistance de la solution, contacts électriques imparfaits et films de surface introduisent une résistance non compensée $R_u$. Cette étude évalue la robustesse du biocapteur face à ces conditions non idéales et quantifie la distorsion du signal SWV causée par la chute ohmique.

**Sommaire :**
1. Physique de la résistance non compensée
2. Interactions $R_u$–électrode
3. Plan expérimental
4. Résultats attendus et conclusion pratique
5. Références bibliographiques

---

## 1. Physique de la résistance non compensée

### 1.1 Origine de $R_u$

La résistance non compensée est la résistance totale entre l'électrode de travail et l'électrode de référence qui n'est pas corrigée par le potentiostat. Elle provient de plusieurs sources :

- **Résistance de la solution** : proportionnelle à la distance électrode–référence et inversement proportionnelle à la conductivité du tampon.
- **Résistance de contact** : connexions électriques défectueuses, corrosion des contacts.
- **Résistance du film** : couche de passivation ou dépôt sur l'électrode.

### 1.2 Chute ohmique ($IR_{drop}$)

Lorsqu'un courant $I$ traverse la résistance $R_u$, le potentiel réellement appliqué à l'interface électrode–solution diffère du potentiel imposé par le potentiostat :

$$E_{réel} = E_{appliqué} - I \times R_u$$

La chute ohmique $IR_{drop} = I_{peak} \times R_u$ provoque trois effets :

1. **Déplacement du potentiel de pic** : le pic se déplace dans la direction de la réaction (vers des potentiels plus négatifs en réduction).
2. **Élargissement du pic** : la distribution de potentiel sur la surface de l'électrode est modifiée, élargissant la FWHM.
3. **Réduction apparente du courant de pic** : le pic étalé contient la même quantité de charge mais avec une amplitude réduite.

### 1.3 Ordre de grandeur

Pour le biocapteur à aptamère à 25 Hz, les courants typiques sont de l'ordre du nanoampère :

| $R_u$ ($\Omega$) | $I_{peak}$ typique (nA) | $IR_{drop}$ (mV) | Impact |
|-------------------|--------------------------|-------------------|--------|
| 0 | 50 | 0 | Aucun |
| 50 | 50 | 0.0025 | Négligeable |
| 100 | 50 | 0.005 | Négligeable |
| 200 | 50 | 0.010 | Négligeable |
| 500 | 50 | 0.025 | Faible |
| 1000 | 50 | 0.050 | Modéré |

À 25 Hz avec des courants de l'ordre du nanoampère, la chute ohmique reste modérée même pour $R_u = 1000\;\Omega$. Cependant, l'effet de $R_u$ ne se limite pas à la simple chute $IR$ : la résistance non compensée modifie également la forme du signal SWV en filtrant les composantes rapides du courant.

### 1.4 Effet de filtrage RC

La résistance non compensée, combinée à la capacité de double couche $C_{dl}$, forme un filtre RC :

$$\tau_{RC} = R_u \times C_{dl}$$

Si $\tau_{RC}$ est comparable à la durée de l'impulsion $\left(\frac{1}{2f}\right)$, le courant n'atteint pas sa valeur stationnaire avant l'échantillonnage, ce qui distord le voltammogramme. Cet effet est plus prononcé à haute fréquence, mais dans cette étude la fréquence est fixée à 25 Hz (durée d'impulsion $= 20$ ms), ce qui laisse généralement assez de temps pour la relaxation RC.

### 1.5 Élargissement de la FWHM avec $R_u$

La FWHM augmente avec $R_u$ selon une relation qui dépend du mécanisme :

- Pour des courants faibles (nA), l'élargissement est principalement dû à la redistribution du potentiel sur la surface hétérogène.
- L'élargissement est plus prononcé pour les électrodes à RF élevé (courants plus grands, donc $IR_{drop}$ plus important).

---

## 2. Interactions $R_u$–électrode

### 2.1 Interaction RF $\times$ $R_u$

Les électrodes à RF élevé produisent des courants plus importants (surface réelle plus grande), ce qui amplifie l'effet de $R_u$ :

$$IR_{drop}(\text{RF},\, R_u) = I_{peak}(\text{RF}) \times R_u \propto \text{RF} \cdot R_u$$

Ainsi, une électrode très rugueuse (RF $= 3$) à $R_u = 1000\;\Omega$ subit une chute ohmique trois fois supérieure à celle d'une électrode plate (RF $= 1$) dans les mêmes conditions.

### 2.2 Interaction Ni $\times$ $R_u$

L'exposition au nickel réduit $I_{peak}$ (via la réduction de $k^0_{eff}$ et les courants parasites). Paradoxalement, cela réduit aussi le $IR_{drop}$ faradique. Cependant, les courants parasites générés par le Ni contribuent eux aussi à la chute ohmique sur $R_u$, de sorte que l'effet net dépend de l'équilibre entre ces deux contributions.

| Condition | $I_{peak}$ relatif | $IR_{drop}$ à $R_u = 1000\;\Omega$ | Effet net |
|-----------|---------------------|--------------------------------------|-----------|
| Ni = 0 %, RF = 1 | Référence | Faible | Minimal |
| Ni = 0 %, RF = 3 | $\times 3$ | $\times 3$ | Significatif |
| Ni = 10 %, RF = 1 | Réduit | Très faible | Courants parasites dominants |
| Ni = 10 %, RF = 3 | Réduit mais amplifié par RF | Modéré | Compétition signal/bruit |

---

## 3. Plan expérimental

### 3.1 Objectif

Cette étude examine l'influence de la résistance non compensée ($R_u$) sur la réponse voltammétrique du biocapteur à aptamère, en interaction avec les paramètres de surface d'électrode (RF et Ni exposé). L'objectif est de quantifier la distorsion du signal causée par la chute ohmique et d'évaluer la robustesse du biocapteur face à des conditions de contact non idéales.

### 3.2 Facteurs et niveaux

| Facteur | Niveaux | Valeurs |
|---------|---------|---------|
| RF | 3 | 1.0, 1.5, 3.0 |
| $\text{Ni}_{exposed}$ | 3 | 0, 3, 10 % |
| $R_u$ | 6 | 0, 50, 100, 200, 500, 1000 $\Omega$ |

### 3.3 Nombre total de combinaisons

$$3 \;(\text{RF}) \times 3 \;(\text{Ni}) \times 6 \;(R_u) = 54 \text{ combinaisons}$$

### 3.4 Paramètres fixes

| Paramètre | Symbole | Valeur | Justification |
|-----------|---------|--------|---------------|
| Fréquence | $f$ | 25 Hz | Fréquence de référence |
| Cuivre exposé | $\text{Cu}_{exposed}$ | 0 % | Isoler l'effet de $R_u$ |
| Contamination | — | 0 % | Surface propre |
| Incrément de potentiel | $\delta E_s$ | 4 mV | Standard SWV |
| Amplitude d'impulsion | $\delta E_p$ | 25 mV | Standard SWV |

---

## 4. Résultats attendus et conclusion pratique

### 4.1 Synthèse par métrique

| Métrique | Comportement attendu |
|----------|---------------------|
| $IR_{drop}$ vs $R_u$ | Relation linéaire ; pente $\propto I_{peak}$ |
| $E_{peak}$ vs $R_u$ | Déplacement linéaire vers les potentiels plus négatifs ; pente $\propto I_{peak}$ |
| FWHM vs $R_u$ | Élargissement progressif, plus marqué pour RF élevé |
| $I_{peak}$ vs $R_u$ | Diminution légère (redistribution de la charge) |
| SNR vs $R_u$ | Dégradation progressive ; modérée à 25 Hz, significative pour $R_u > 500\;\Omega$ |

### 4.2 Résultats détaillés

1. **$IR_{drop}$ vs $R_u$** : relation linéaire pour chaque combinaison (RF, Ni). Pente proportionnelle à $I_{peak}$.
2. **$E_{peak}$ vs $R_u$** : déplacement linéaire vers les potentiels plus négatifs. Pente proportionnelle à $I_{peak}$.
3. **FWHM vs $R_u$** : élargissement progressif, plus marqué pour RF élevé.
4. **$I_{peak}$ vs $R_u$** : diminution légère due à l'élargissement du pic (redistribution de la charge sur une gamme de potentiels plus large).
5. **SNR vs $R_u$** : dégradation progressive. L'effet est modéré à 25 Hz car les courants sont faibles, mais significatif pour $R_u > 500\;\Omega$.

### 4.3 Conclusion pratique

À la fréquence de référence de 25 Hz, la résistance non compensée a un effet modéré sur le signal du biocapteur, même à $R_u = 1000\;\Omega$. Le déplacement de $E_{peak}$ reste inférieur à $0.1$ mV pour des courants de l'ordre du nanoampère. L'effet principal est l'élargissement de la FWHM, qui réduit la résolution du pic et peut affecter la précision de l'ajustement gaussien utilisé pour l'extraction des métriques.

---

## 5. Références bibliographiques

*Pour la liste complète des références, consultez la section Références bibliographiques dans le menu Annexes.*
