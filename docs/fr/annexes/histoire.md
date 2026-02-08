**Sommaire :**
1. L'ère de la polarographie et des méthodes pulsées (1922-1969)
2. Naissance de la SWV moderne (1969-1990)
3. L'essor des aptamères (1990-2010)
4. Biocapteurs électrochimiques à aptamères : l'ère actuelle (2010-)
5. Vers la modélisation numérique des biocapteurs
6. Références bibliographiques

---

La voltamétrie à onde carrée (SWV) est aujourd'hui la technique de choix pour interroger les biocapteurs à aptamères. Son histoire croise celle de l'électrochimie analytique, de la biologie combinatoire et de la simulation numérique. Retraçons ici les grandes étapes qui ont conduit aux études paramétriques de ce projet.

## 1. L'ère de la polarographie et des méthodes pulsées (1922-1969)

Tout commence, comme pour la voltamétrie cyclique, avec la goutte de mercure de Heyrovský à Prague. Sa surface constamment renouvelée offrait une reproductibilité inédite. Mais très vite, les électrochimistes cherchent à dépasser les limites de la polarographie classique -- trop lente, trop sensible au courant capacitif -- en superposant des impulsions au signal continu.

| Année | Événement |
|-------|-----------|
| 1922 | **Jaroslav Heyrovský** invente la polarographie à l'électrode à goutte de mercure tombante (DME) à Prague |
| 1942 | **Barker** commence ses travaux sur les techniques pulsées au laboratoire d'Harwell (Royaume-Uni) |
| 1957 | **Barker & Jenkins** développent la première polarographie à onde carrée, superposant un signal carré de faible amplitude à la rampe de potentiel |
| 1959 | Heyrovský reçoit le **Prix Nobel de Chimie** pour ses travaux sur la polarographie |
| 1969 | **Janet & Robert Osteryoung** modernisent la technique en couplant l'onde carrée à un signal en escalier (staircase), posant les bases de la SWV moderne |

*L'idée clé* : en appliquant des impulsions plutôt qu'une rampe continue, on échantillonne le courant faradique au moment où le courant capacitif a décru, améliorant considérablement le rapport signal/bruit. Cette astuce, simple en apparence, allait transformer l'électrochimie analytique.

## 2. Naissance de la SWV moderne (1969-1990)

La SWV se distingue progressivement de la voltamétrie à impulsions différentielles (DPV) par sa rapidité et sa sensibilité supérieures. Là où la DPV nécessite plusieurs minutes pour balayer une fenêtre de potentiel, la SWV y parvient en quelques secondes.

| Contribution | Impact |
|--------------|--------|
| **Osteryoung & O'Dea** | Raffinement de la théorie pour les systèmes réversibles et quasi-réversibles ; la SWV peut acquérir un voltammogramme complet en quelques secondes |
| **Lovrić & Komorsky-Lovrić** | Développement de la théorie pour les espèces adsorbées en surface, directement applicable aux biocapteurs à aptamères |
| **Courant net** | Le signal net $I_{net} = I_{forward} - I_{reverse}$ élimine la composante capacitive, offrant une sensibilité supérieure à la CV et à la DPV |
| **Ramaley & Krause** | Premiers travaux théoriques reliant la forme du pic SWV aux paramètres cinétiques du système |

Le principe de mesure repose sur trois courants mesurés à chaque pas de potentiel : le courant direct (*forward*), le courant inverse (*reverse*) et le courant net qui est leur différence. Cette décomposition permet non seulement d'éliminer le bruit capacitif, mais aussi de diagnostiquer la réversibilité du système.

Pour une espèce adsorbée en surface (cas des aptamères), le courant de pic en SWV s'exprime :

$$ I_{pic} \propto n \cdot F \cdot A \cdot \Gamma \cdot f $$

où $n$ est le nombre d'électrons, $F$ la constante de Faraday, $A$ l'aire de l'électrode, $\Gamma$ la densité surfacique de l'espèce redox et $f$ la fréquence de l'onde carrée. Cette relation linéaire avec la fréquence est une signature caractéristique du régime d'adsorption, à la différence du régime diffusionnel ($I_{pic} \propto f^{1/2}$).

## 3. L'essor des aptamères (1990-2010)

Au tournant des années 1990, une révolution parallèle se produit en biologie moléculaire : la sélection in vitro d'oligonucléotides capables de reconnaître des cibles spécifiques avec une affinité comparable à celle des anticorps.

| Année | Événement |
|-------|-----------|
| 1990 | **Ellington & Szostak** (Harvard) inventent le terme "aptamère" (du latin *aptus*, adapté) et développent la méthode SELEX (Systematic Evolution of Ligands by EXponential enrichment) |
| 1990 | **Tuerk & Gold** (Colorado) développent indépendamment la même méthode de sélection in vitro |
| 1996 | Premiers aptamères ADN sélectionnés pour des cibles de petite taille (ATP, théophylline) |
| 2003 | **Xiao, Piorek, Plaxco & Heeger** (UCSB) réalisent le premier biocapteur électrochimique à aptamère (E-AB) pour la détection de la thrombine |
| 2005 | Extension du concept E-AB à la détection de petites molécules (cocaïne, ATP) |

*Le principe fondamental* : l'aptamère, immobilisé sur l'électrode via une liaison thiol-or, porte un marqueur redox (typiquement le bleu de méthylène, MB). Lors de la reconnaissance de la cible, le changement conformationnel de l'aptamère rapproche ou éloigne le MB de la surface de l'électrode, modulant le transfert d'électrons et donc le courant mesuré en SWV.

Les aptamères présentent plusieurs avantages par rapport aux anticorps traditionnels :
- **Stabilité thermique** supérieure (résistance à la dénaturation)
- **Synthèse chimique** reproductible et peu coûteuse
- **Régénération** possible de la surface du capteur par simple rinçage
- **Compatibilité directe** avec la transduction électrochimique (marquage redox en position terminale)

## 4. Biocapteurs électrochimiques à aptamères : l'ère actuelle (2010-)

Depuis 2010, les biocapteurs E-AB ont connu un essor considérable, portés notamment par le groupe de **Kevin Plaxco** à l'UCSB.

| Avancée | Description |
|---------|-------------|
| **Plateforme structure-switching** | Plaxco et collaborateurs généralisent le concept de commutation conformationnelle à de nombreuses cibles (petites molécules, protéines, antibiotiques) |
| **Mesures in vivo en temps réel** | Démonstration de capteurs E-AB implantables mesurant en continu la concentration de médicaments dans le sang d'animaux vivants |
| **SWV comme technique de choix** | La SWV s'impose face à la CV et à la DPV pour les capteurs E-AB grâce à son rapport signal/bruit supérieur et sa capacité à discriminer le signal faradique du bruit capacitif |
| **Correction cinétique (KDM)** | Développement de méthodes de correction basées sur la dépendance en fréquence du signal SWV, permettant de s'affranchir de la dérive du capteur |

**Défis actuels :**
- Qualité de la surface de l'électrode (rugosité, cristallinité Au/Ni/Cu)
- Adsorption non spécifique de molécules interférentes
- Stabilité à long terme de la monocouche d'aptamères (dégradation du thiol)
- Optimisation des paramètres SWV (fréquence, amplitude, pas de potentiel) pour chaque couple électrode-aptamère
- Passage du laboratoire à des dispositifs portables pour le diagnostic au point de soin (*point-of-care*)

## 5. Vers la modélisation numérique des biocapteurs

L'approche expérimentale seule ne suffit plus pour comprendre et optimiser les biocapteurs E-AB. La modélisation numérique permet d'explorer systématiquement l'espace des paramètres et de prédire le comportement du capteur avant sa fabrication.

| Approche | Outils |
|----------|--------|
| **Transport électrochimique** | Firedrake, FEniCSx : résolution par éléments finis des équations de Nernst-Planck couplées à la cinétique de Butler-Volmer |
| **Cinétique de transfert d'électrons** | Modélisation de la constante de transfert $k_0$ et de son lien avec la fréquence SWV optimale |
| **Études paramétriques** | Ce projet : simulations balayant l'espace électrode (Au, Ni, Cu) $\times$ fréquence $\times$ résistance |
| **Analyse des performances** | Extraction automatisée des courants de pic, rapports signal/bruit et figures de mérite pour chaque configuration |

La transition de la caractérisation empirique vers la simulation numérique permet d'identifier les configurations optimales (matériau d'électrode, fréquence SWV, résistance de solution) sans recourir à des campagnes expérimentales exhaustives.

C'est précisément l'objectif des simulations présentées dans cette application : en explorant systématiquement l'espace des paramètres, on peut cartographier les performances de chaque configuration et guider le choix expérimental vers les combinaisons les plus prometteuses.

---

## 6. Références bibliographiques

*Pour la liste complète des références, consultez la section Références bibliographiques dans le menu Annexes.*
