### Analyse des résultats — étude 3 : résistance non compensée

Les graphiques ci-dessous montrent l'influence de $R_u$ (0 à 1000 $\Omega$) sur les métriques SWV, pour différentes combinaisons de RF et Ni exposé. Voici les observations principales :

- **$IR_{drop}$ vs $R_u$** : relation linéaire pour chaque combinaison, avec une pente proportionnelle à $I_{peak}$. Les électrodes rugueuses (RF = 3) présentent une chute ohmique environ 3 fois supérieure aux électrodes plates (RF = 1).

- **$E_{peak}$ vs $R_u$** : déplacement vers les potentiels plus négatifs, mais très faible en valeur absolue (< 0.1 mV même à $R_u = 1000\;\Omega$) car les courants sont de l'ordre du nanoampère.

- **FWHM vs $R_u$** : c'est l'effet principal de la résistance non compensée. L'élargissement progressif du pic réduit la résolution et peut affecter la précision de l'ajustement gaussien. L'effet est plus marqué pour les électrodes à RF élevé.

- **Conclusion pratique** : à 25 Hz avec des courants nA, la résistance non compensée est un facteur secondaire. Les seuils recommandés sont $R_u < 200\;\Omega$ (optimal) et $R_u < 500\;\Omega$ (acceptable).
