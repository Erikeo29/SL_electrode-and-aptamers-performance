**Note de l'auteur** — *Ce projet a été conçu intégralement par l'auteur, depuis une page blanche jusqu'à sa mise en ligne. Le contenu a été élaboré sur la base de ses connaissances complétées par des recherches en ligne pour la partie documentaire, définition des concepts physiques, mise en oeuvre des outils numériques pertinents...*

*Pour les sujets (très nombreux !) dépassant son domaine de compétence initial, des outils d'intelligence artificielle et d'automatisation ont été utilisés pour réaliser des recherches internet approfondies (paramétrage des équations des modèles physiques, sélection et utilisation des bibliothèques numériques), la rédaction, le test et la correction des codes (Python, C++), la création de l'interface de cette application, la traduction automatique français / anglais...*

*Il n'en demeure pas moins que tous les résultats présentés dans ce projet sont issus de modèles physiques analytiques et déterministes résolus par des solveurs numériques reconnus et validés. L'objectif est de permettre la réalisation de modélisations multiphysiques avancées au moyen d'outils open-source et gratuits.*

*Les données d'entrées utilisées (équations, valeurs...) sont publiques et disponibles en accès libres sur internet même si très éparpillées. Les codes sont originaux même si non innovants. De fait, ce travail est mis à disposition pour être librement utilisé, reproduit et amélioré à des fins d'apprentissage ou d'exploitation des modèles physiques et numériques présentés.*

&nbsp;

**Sommaire :**
1. Objectif
2. Études disponibles
3. Navigation
4. Note méthodologique

---

## 1. Objectif

Les **biocapteurs électrochimiques à aptamères** (E-AB, de l'anglais *Electrochemical Aptamer-Based biosensors*) permettent la détection en temps réel de molécules cibles dans des fluides biologiques. Un aptamère est un brin d'ADN ou d'ARN synthétique, sélectionné pour se lier spécifiquement à une cible donnée (protéine, petite molécule, ion…). Lorsque la cible se fixe sur l'aptamère, celui-ci change de forme (*conformation*), ce qui modifie un signal électrique mesurable.

Leur signal repose sur la **voltammétrie à onde carrée** (SWV, de l'anglais *Square Wave Voltammetry*), une technique électrochimique pulsée qui interroge un rapporteur redox — le bleu de méthylène — greffé à l'extrémité de l'aptamère, lui-même ancré sur une électrode d'or.

La qualité du signal dépend de nombreux facteurs : état de surface de l'électrode (rugosité, composition, contamination), paramètres instrumentaux (fréquence SWV) et conditions de mesure (résistance de contact). Cette application regroupe **trois études paramétriques** simulées numériquement afin de quantifier l'influence de chaque facteur sur les métriques du voltammogramme :

- $I_{peak}$ — courant de pic (nA)
- $E_{peak}$ — potentiel de pic (V)
- FWHM (*Full Width at Half Maximum*) — largeur à mi-hauteur du pic (mV)
- SNR (*Signal-to-Noise Ratio*) — rapport signal-sur-bruit
- RF (*Roughness Factor*) — facteur de rugosité de l'électrode

---

## 2. Études disponibles

### Étude 1 : paramètres d'électrode

Influence de quatre paramètres de surface — facteur de rugosité (RF), nickel exposé, cuivre exposé et contamination — sur la réponse SWV du biocapteur. Résultat principal : le nickel exposé est le facteur dominant, dégradant le SNR d'un facteur $\sim 10$ entre 0 et 10 %.

### Étude 2 : fréquence SWV

Influence de la fréquence (10 à 500 Hz) en interaction avec la rugosité et le nickel exposé. Résultat principal : le paramètre cinétique $K = k^0_{eff}/f$ détermine le régime (réversible → irréversible) et la fréquence optimale dépend de l'état de surface.

### Étude 3 : résistance non compensée

Influence de la résistance non compensée $R_u$ (0 à 1000 $\Omega$) en interaction avec la rugosité et le nickel exposé. Résultat principal : à 25 Hz et courants nA, la chute ohmique reste modérée même à $R_u = 1000\;\Omega$ ; l'effet principal est l'élargissement de la FWHM.

---

## 3. Navigation

La navigation dans les différentes pages de cette application est structurée avec les outils suivants :

1. **Menu latéral (à gauche)** : outil de navigation entre les différentes sections du projet :
   - **Introduction** : principe de la SWV, pic du bleu de méthylène, métriques extraites.
   - **Résultats de modélisation** : chaque étude contient des onglets Physique (modèles physiques et équations), Code (codes sources commentés), Résultats (filtres en cascade et comparaison côte à côte de 2 simulations) et Analyse (graphiques d'ensemble et rapport statistique).
   - **Annexes** : synthèse et conclusion, lexique, équations clés, références bibliographiques et une page d'histoire sur les principaux chercheurs et scientifiques ayant contribué aux concepts physiques et numériques présentés.

2. **Boutons de navigation flottants (à droite)** : déplacement rapide haut/bas de page.

---

## 4. Note méthodologique

Les résultats présentés proviennent de simulations numériques basées sur un **modèle ODE de surface** (espèces adsorbées, pas de maillage spatial). Le solveur résout l'équation cinétique de Butler-Volmer pour les fractions de couverture de l'espèce redox adsorbée ($\Gamma_{ox}$, $\Gamma_{red}$), couplée au protocole SWV (escalier + impulsions). L'intégration temporelle utilise un schéma d'**Euler implicite** (Python/NumPy). L'extraction des métriques ($I_{peak}$, $E_{peak}$, FWHM, SNR) est réalisée par ajustement gaussien du pic SWV. Ce travail s'inscrit dans un projet plus large utilisant **Firedrake** et **EchemFEM** pour la modélisation électrochimique par éléments finis.

Cette application est un **visualiseur de résultats**, non un simulateur en temps réel. Les codes sont disponibles dans les onglets « Code » de chaque étude afin de permettre leur reproduction.
