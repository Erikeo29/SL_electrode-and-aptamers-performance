La qualité de la surface d'une électrode d'or est déterminante pour la performance d'un biocapteur à aptamère. Dans un procédé de fabrication industriel, la couche d'or peut présenter des défauts : rugosité variable, sous-couches de nickel ou de cuivre partiellement exposées, ou contamination résiduelle. Cette étude quantifie l'impact de chacun de ces paramètres sur le signal SWV du biocapteur, afin d'établir des seuils de qualité et d'identifier les facteurs dominants.

**Sommaire :**
1. Paramètres d'électrode
2. Modèle physique
3. Plan expérimental
4. Hiérarchie des effets
5. Références bibliographiques

---

## 1. Paramètres d'électrode

### 1.1 Facteur de rugosité (RF)

Le facteur de rugosité est le rapport entre la surface réelle et la surface géométrique de l'électrode :

$$\text{RF} = \frac{A_{réelle}}{A_{géométrique}}$$

| Niveau | RF | Description |
|--------|----|-------------|
| 1 | 1.0 | Surface parfaitement plane |
| 2 | 1.5 | Rugosité modérée (typique) |
| 3 | 2.0 | Surface rugueuse |
| 4 | 3.0 | Très rugueuse |
| 5 | 5.0 | Extrêmement rugueuse |

**Effets physiques :**

- La surface réelle augmente proportionnellement à RF, ce qui accroît le courant capacitif ($I_{baseline}$).
- La densité surfacique d'aptamères $\Gamma_{eff}$ augmente avec RF (plus de sites d'ancrage disponibles).
- Le courant de pic $I_{peak}$ augmente avec RF, mais le rapport $I_{peak} / I_{baseline}$ peut se dégrader si la rugosité favorise l'adsorption non spécifique.
- Un optimum est généralement observé autour de RF $= 1.5$, où le gain en signal faradique dépasse l'augmentation du bruit de fond.

### 1.2 Nickel exposé ($\text{Ni}_{exposed}$)

Le pourcentage de surface où le nickel de la sous-couche est exposé à travers des défauts de la couche d'or :

| Niveau | $\text{Ni}_{exposed}$ (%) | Description |
|--------|---------------------------|-------------|
| 1 | 0 | Couche d'or intacte |
| 2 | 3 | Défauts mineurs |
| 3 | 5 | Défauts modérés |
| 4 | 10 | Défauts majeurs |

**Effets physiques :**

- Le nickel exposé catalyse la décomposition du tampon et génère des courants parasites importants.
- La constante de vitesse effective $k^0_{eff}$ est fortement réduite car le Ni n'est pas favorable au transfert d'électrons du MB.
- L'effet dominant est une **dégradation du SNR d'un facteur 10** lorsque $\text{Ni}_{exposed}$ passe de 0 à 10 %.
- Le nickel exposé est le facteur le plus influent de cette étude sur la qualité du signal.

### 1.3 Cuivre exposé ($\text{Cu}_{exposed}$)

Le pourcentage de surface où le cuivre de la sous-couche est exposé :

| Niveau | $\text{Cu}_{exposed}$ (%) | Description |
|--------|---------------------------|-------------|
| 1 | 0 | Pas d'exposition |
| 2 | 2 | Exposition modérée |
| 3 | 5 | Exposition importante |

**Effets physiques :**

- À pH 7.4 (tampon PBS), le cuivre est relativement stable et son effet est secondaire par rapport au nickel.
- Cu contribue faiblement au courant de fond et à une légère réduction de $k^0_{eff}$.
- L'impact sur le SNR est mesurable mais reste un facteur de second ordre.

### 1.4 Contamination (sites bloqués)

Le pourcentage de sites de surface bloqués par des contaminants (résidus organiques, oxydes) :

| Niveau | Contamination (%) | Description |
|--------|-------------------|-------------|
| 1 | 0 | Surface propre |
| 2 | 15 | Contamination modérée |
| 3 | 30 | Contamination forte |

**Effets physiques :**

- Les sites bloqués ne peuvent pas accueillir d'aptamères, réduisant $\Gamma_{eff}$ de manière proportionnelle (voir section 2.2).
- Le courant de pic $I_{peak}$ diminue linéairement avec la contamination.
- La contamination n'affecte pas directement $k^0_{eff}$ ni $E_{peak}$, mais réduit le SNR par diminution du signal.

---

## 2. Modèle physique

### 2.1 Constante de vitesse effective

La constante de vitesse de transfert d'électron effective dépend des fractions de surface exposées :

$$k^0_{eff} = k^0_{Au} \cdot f_{Au} + k^0_{Ni} \cdot f_{Ni} + k^0_{Cu} \cdot f_{Cu}$$

où :
- $k^0_{Au} \gg k^0_{Ni},\; k^0_{Cu}$ (l'or est le meilleur conducteur pour le transfert d'électrons du MB)
- $f_{Au} = 1 - f_{Ni} - f_{Cu} - f_{contamination}$ (fraction de surface d'or libre)

En pratique, comme $k^0_{Ni}$ et $k^0_{Cu}$ sont très faibles comparées à $k^0_{Au}$, la réduction de $k^0_{eff}$ est principalement due à la diminution de la fraction d'or disponible.

### 2.2 Densité surfacique effective

$$\Gamma_{eff} = \Gamma_0 \times \text{RF} \times \left(1 - \frac{\text{contamination}}{100}\right)$$

Le facteur de rugosité multiplie la surface disponible tandis que la contamination réduit la fraction de sites accessibles.

---

## 3. Plan expérimental

### 3.1 Objectif

Cette étude explore l'influence de quatre paramètres de surface d'électrode sur la réponse voltammétrique du biocapteur à aptamère. L'objectif est de quantifier comment la qualité de la surface d'or affecte chaque métrique extraite du voltammogramme SWV ($I_{peak}$, $E_{peak}$, FWHM, SNR).

### 3.2 Plan factoriel complet

Le plan est un factoriel complet croisant les quatre paramètres :

$$5 \;(\text{RF}) \times 4 \;(\text{Ni}) \times 3 \;(\text{Cu}) \times 3 \;(\text{contamination}) = 180 \text{ combinaisons}$$

### 3.3 Paramètres fixes

| Paramètre | Symbole | Valeur | Justification |
|-----------|---------|--------|---------------|
| Fréquence | $f$ | 25 Hz | Fréquence de référence standard |
| Résistance non compensée | $R_u$ | 0 $\Omega$ | Isoler l'effet des paramètres d'électrode |
| Incrément de potentiel | $\delta E_s$ | 4 mV | Standard SWV |
| Amplitude d'impulsion | $\delta E_p$ | 25 mV | Standard SWV |
| Température | $T$ | 25 °C | Conditions ambiantes |
| pH | — | 7.4 | Tampon PBS physiologique |

---

## 4. Hiérarchie des effets

### 4.1 Classement par ordre d'influence

| Rang | Facteur | Effet principal | Métrique la plus affectée |
|------|---------|-----------------|---------------------------|
| 1 | $\text{Ni}_{exposed}$ | Courants parasites, réduction de $k^0_{eff}$ | SNR ($\div 10$ entre 0 et 10 %) |
| 2 | RF | Augmentation de $I_{baseline}$ et $I_{peak}$ | $I_{baseline}$ ($\propto$ RF) |
| 3 | Contamination | Réduction de $\Gamma_{eff}$ | $I_{peak}$ ($-30$ % à 30 % contam.) |
| 4 | $\text{Cu}_{exposed}$ | Faible contribution au courant de fond | SNR (effet secondaire à pH 7.4) |

### 4.2 Résultats attendus

1. **Ni exposé** : facteur dominant. Le SNR chute d'un facteur $\sim 10$ entre 0 et 10 % de Ni exposé, principalement à cause des courants parasites qui augmentent le bruit.
2. **RF** : augmente $I_{baseline}$ proportionnellement. Optimum autour de RF $= 1.5$ pour le compromis signal/bruit.
3. **Contamination** : réduit $I_{peak}$ linéairement. À 30 %, le signal est réduit de près d'un tiers.
4. **Cu exposé** : effet secondaire à pH 7.4. Contribution mesurable mais non dominante.

---

## 5. Références bibliographiques

*Pour la liste complète des références, consultez la section Références bibliographiques dans le menu Annexes.*
