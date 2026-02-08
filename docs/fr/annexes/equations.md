**Sommaire :**
1. Forme d'onde SWV
2. Cinétique de Butler-Volmer (espèces adsorbées)
3. Courant faradique (espèces adsorbées)
4. Paramètre cinétique adimensionnel
5. Paramètres de surface d'électrode
6. Chute ohmique et filtrage RC
7. Métriques extraites
8. Références bibliographiques

---

En voltamétrie à vague carrée (SWV), le signal appliqué combine un escalier de potentiel et des impulsions symétriques. Contrairement à la voltamétrie cyclique classique (CV) où le transport par diffusion domine, les études paramétriques de cette application portent sur des **espèces adsorbées en surface** (bleu de méthylène sur aptamères). La cinétique est donc gouvernée par le taux de couverture de surface et non par un gradient de concentration en solution.

## 1. Forme d'onde SWV

Le potentiel appliqué $E(t)$ se décompose en un escalier (staircase) auquel se superposent des impulsions carrées (pulses) :

### 1.1 Escalier de potentiel

À chaque pas $k$ (période $\tau = 1/f$), le potentiel de base avance de $\delta E_s$ :

$$ E_{base}(k) = E_{start} + k \times \delta E_s $$

### 1.2 Impulsions directe et inverse

Sur chaque marche d'escalier, une impulsion d'amplitude $\delta E_p$ est appliquée :

$$ E_{forward} = E_{base}(k) + \delta E_p $$
$$ E_{reverse} = E_{base}(k) - \delta E_p $$

### 1.3 Courant net

Le courant est échantillonné à la fin de chaque demi-période. Le courant net est la différence :

$$ I_{net} = I_{forward} - I_{reverse} $$

Ce courant différentiel **élimine le courant capacitif** (qui est identique en amplitude sur les deux impulsions) et maximise la composante faradique.

### Paramètres de la forme d'onde

| Symbole | Nom | Valeur typique | Unité |
|---------|-----|----------------|-------|
| $f$ | fréquence SWV | 1 -- 500 | Hz |
| $\delta E_s$ | pas d'escalier (step) | 1 -- 10 | mV |
| $\delta E_p$ | amplitude d'impulsion (pulse) | 10 -- 100 | mV |
| $E_{start}$ | potentiel initial | variable | V |
| $E_{end}$ | potentiel final | variable | V |

---

## 2. Cinétique de Butler-Volmer (espèces adsorbées)

Pour des espèces confinées en surface (bleu de méthylène lié à un aptamère), les constantes de vitesse directe et inverse s'expriment :

$$ k_f = k^0_{eff} \exp\left(-\frac{\alpha \, n \, F}{R \, T} \, \eta \right) $$

$$ k_b = k^0_{eff} \exp\left(\frac{(1-\alpha) \, n \, F}{R \, T} \, \eta \right) $$

Avec la surtension corrigée de la chute ohmique :

$$ \eta = E(t) - E^0 - I \times R_u $$

Où :
- $k^0_{eff}$ = constante cinétique effective de surface [s$^{-1}$] (et non m/s, car espèces adsorbées)
- $\alpha$ = coefficient de transfert de charge (sans dimension)
- $n$ = nombre d'électrons échangés (2 pour MB)
- $F$ = constante de Faraday (96 485 C/mol)
- $R$ = constante des gaz parfaits (8.314 J/(mol$\cdot$K))
- $T$ = température [K]
- $E^0$ = potentiel formel du couple MB/LB [V]
- $R_u$ = résistance non compensée [$\Omega$]

### Paramètres cinétiques

| Symbole | Nom | Valeur | Unité |
|---------|-----|--------|-------|
| $F$ | constante de Faraday | 96 485 | C/mol |
| $R$ | constante des gaz | 8.314 | J/(mol$\cdot$K) |
| $T$ | température | 298.15 | K |
| $\alpha$ | coefficient de transfert | 0.5 | -- |
| $n$ | nombre d'électrons (MB) | 2 | -- |
| $E^0$ | potentiel formel MB/LB | $\approx -0.24$ | V vs Ag/AgCl |

---

## 3. Courant faradique (espèces adsorbées)

Le courant faradique pour des espèces redox confinées en surface (et non en solution) est :

$$ I_{farad} = n \, F \, A \, \Gamma_{eff} \left( k_f \, \theta_{ox} - k_b \, \theta_{red} \right) $$

Avec la contrainte de conservation sur le taux de couverture :

$$ \theta_{ox} + \theta_{red} = 1 $$

Où :
- $A$ = surface géométrique de l'électrode [m$^2$]
- $\Gamma_{eff}$ = densité surfacique effective de l'espèce redox [mol/m$^2$]
- $\theta_{ox}$ = fraction de l'espèce sous forme oxydée (sans dimension)
- $\theta_{red}$ = fraction de l'espèce sous forme réduite (sans dimension)
- $k_f$, $k_b$ = constantes de vitesse directe et inverse [s$^{-1}$]

> **Remarque** : Contrairement au cas en solution (CV classique), il n'y a pas de couche de diffusion. Le pic SWV ne résulte pas d'une déplétion en solution mais de la conversion progressive des espèces adsorbées.

### Paramètres du courant faradique

| Symbole | Nom | Valeur typique | Unité |
|---------|-----|----------------|-------|
| $A$ | surface géométrique | $1.77 \times 10^{-6}$ | m$^2$ |
| $\Gamma_{eff}$ | densité surfacique effective | $10^{-11}$ -- $10^{-10}$ | mol/m$^2$ |
| $\Gamma_0$ | densité surfacique maximale (MB) | $\sim 4.5 \times 10^{-10}$ | mol/m$^2$ |

---

## 4. Paramètre cinétique adimensionnel

Le paramètre adimensionnel $K$ de Lovric compare la cinétique de transfert de charge à la fréquence d'excitation SWV :

$$ K = \frac{k^0_{eff}}{f} $$

Où $f$ est la fréquence SWV [Hz] et $k^0_{eff}$ la constante cinétique effective [s$^{-1}$].

### Régimes cinétiques

| Domaine de $K$ | Régime | Comportement |
|----------------|--------|--------------|
| $K > 5$ | réversible | $I_{net}$ proportionnel à $f$, FWHM minimale |
| $0.1 < K < 5$ | quasi-réversible | courant net maximal, sensibilité optimale |
| $K < 0.1$ | irréversible | pic large, courant net diminue |

### Largeur à mi-hauteur (FWHM) idéale

En régime réversible, la largeur à mi-hauteur du pic de courant net est :

$$ FWHM_{ideal} = \frac{90.6}{n} \text{ mV} $$

Pour le bleu de méthylène ($n = 2$) :

$$ FWHM_{ideal} = \frac{90.6}{2} = 45.3 \text{ mV} $$

Un élargissement au-delà de cette valeur théorique indique des interactions latérales entre adsorbats, une hétérogénéité de surface ou un régime quasi-réversible/irréversible.

---

## 5. Paramètres de surface d'électrode

### 5.1 Constante cinétique effective (électrodes composites Au/Ni/Cu)

Pour une électrode à composition variable, la constante cinétique effective est la moyenne pondérée par les fractions surfaciques :

$$ k^0_{eff} = k^0_{Au} \times f_{Au} + k^0_{Ni} \times f_{Ni} + k^0_{Cu} \times f_{Cu} $$

Où $f_{Au} + f_{Ni} + f_{Cu} = 1$ et chaque $k^0_i$ est la constante cinétique intrinsèque du métal $i$ [s$^{-1}$].

### 5.2 Densité surfacique effective

La densité surfacique effective d'espèce redox active tient compte du facteur de rugosité et de la contamination :

$$ \Gamma_{eff} = \Gamma_0 \times RF \times \left(1 - \frac{contamination}{100}\right) $$

Avec le facteur de rugosité :

$$ RF = \frac{A_{r\acute{e}elle}}{A_{g\acute{e}om\acute{e}trique}} $$

### Paramètres de surface

| Symbole | Nom | Valeur typique | Unité |
|---------|-----|----------------|-------|
| $k^0_{Au}$ | constante cinétique or | 10 -- 100 | s$^{-1}$ |
| $k^0_{Ni}$ | constante cinétique nickel | 0.1 -- 10 | s$^{-1}$ |
| $k^0_{Cu}$ | constante cinétique cuivre | 1 -- 50 | s$^{-1}$ |
| $f_{Au}$, $f_{Ni}$, $f_{Cu}$ | fractions surfaciques | 0 -- 1 | -- |
| $RF$ | facteur de rugosité | 1 -- 3 | -- |
| $\Gamma_0$ | couverture maximale MB | $\sim 4.5 \times 10^{-10}$ | mol/m$^2$ |
| contamination | taux de contamination | 0 -- 50 | % |

---

## 6. Chute ohmique et filtrage RC

### 6.1 Chute ohmique ($IR$ drop)

La chute ohmique déplace le potentiel effectivement vu par l'interface :

$$ IR_{drop} = I_{peak} \times R_u $$

Le potentiel réel à l'interface est :

$$ E_{r\acute{e}el} = E_{appliqu\acute{e}} - I \times R_u $$

> Une chute ohmique excessive ($IR_{drop} > 5$ mV) déforme le pic SWV : élargissement, aplatissement et décalage en potentiel.

### 6.2 Constante de temps RC

La constante de temps du circuit RC formé par la résistance non compensée et la capacité de double couche limite la vitesse de réponse :

$$ \tau_{RC} = R_u \times C_{dl} $$

Pour que le courant capacitif se dissipe avant l'échantillonnage, il faut :

$$ \tau_{RC} \ll \frac{1}{2f} $$

soit typiquement $\tau_{RC} < \frac{1}{10f}$.

### Paramètres de chute ohmique

| Symbole | Nom | Valeur typique | Unité |
|---------|-----|----------------|-------|
| $R_u$ | résistance non compensée | 10 -- 1000 | $\Omega$ |
| $C_{dl}$ | capacité de double couche | 10 -- 100 | $\mu$F/cm$^2$ |
| $\tau_{RC}$ | constante de temps RC | 0.01 -- 10 | ms |

---

## 7. Métriques extraites

Les études paramétriques évaluent la performance du biocapteur selon sept métriques complémentaires :

### 7.1 Rapport signal-sur-bruit (SNR)

$$ SNR = \frac{I_{peak}}{\sigma_{r\acute{e}sidus}} $$

Où $\sigma_{résidus}$ est l'écart-type des résidus après soustraction de la ligne de base.

### 7.2 Tableau récapitulatif des métriques

| Métrique | Symbole | Formule | Unité | Objectif |
|----------|---------|---------|-------|----------|
| Courant de pic | $I_{peak}$ | max($I_{net}$) | $\mu$A | maximiser |
| Potentiel de pic | $E_{peak}$ | $E$ à $I_{peak}$ | V | $\approx E^0$ |
| Largeur à mi-hauteur | FWHM | largeur à $I_{peak}/2$ | mV | minimiser ($\geq 45.3$ mV) |
| Rapport signal/bruit | SNR | $I_{peak} / \sigma_{résidus}$ | -- | maximiser |
| Chute ohmique | $IR_{drop}$ | $I_{peak} \times R_u$ | mV | minimiser ($< 5$ mV) |
| Facteur de forme | $FF$ | $I_{peak} / (FWHM \times I_{base})$ | -- | maximiser |
| Score global | $S_{global}$ | moyenne pondérée normalisée | -- | maximiser |

---

## 8. Références bibliographiques

*Pour la liste complète des références, consultez la section Références bibliographiques dans le menu Annexes.*
