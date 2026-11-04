<div align="center">

# Calculateur de Tsiolkovski

### Propulsion · Python · Visualisation interactive

Estime le delta-v idéal d’une étape de fusée et visualise la répartition de masse.

[**Ouvrir le calculateur interactif ↗**](https://you21293.github.io/Calculateur-d-quation-de-Tsiolkovski/)

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Sans dépendance](https://img.shields.io/badge/dépendances-aucune-2E8B57)
![Propulsion spatiale](https://img.shields.io/badge/sujet-propulsion-5865F2)

</div>

---

## Le projet

Un outil pédagogique pour étudier l’équation de Tsiolkovski. Le calculateur web met à jour les résultats pendant la saisie ; le programme Python fournit le même calcul dans le terminal.

## Résultats calculés

- Delta-v idéal, en m/s et en km/s.
- Masse de propergol consommée.
- Rapport de masse et fraction de propergol.

## Utilisation

### Calculateur web

Ouvre [le calculateur interactif](https://you21293.github.io/Calculateur-d-quation-de-Tsiolkovski/) dans un navigateur récent. Aucune installation n’est nécessaire.

### Programme Python

Python 3.10 ou version ultérieure est requis. Lance le programme depuis le dossier du projet :

\`\`\`bash
python main.py
\`\`\`

Sous Windows, tu peux aussi utiliser \`py main.py\`.

Saisis la vitesse d’éjection en m/s et les masses en kg. Les valeurs doivent être positives, avec une masse initiale supérieure à la masse finale.

## Modèle

$$
\Delta v = v_e \ln\left(\frac{m_0}{m_f}\right)
\qquad
m_{\mathrm{propergol}} = m_0 - m_f
$$

où $v_e$ est la vitesse d’éjection effective, $m_0$ la masse initiale et $m_f$ la masse finale.

## Hypothèses et limites

Le calcul suppose une étape idéale. Il ne prend pas en compte la gravité pendant la poussée, la traînée atmosphérique, les pertes de pilotage ni les limites réelles du moteur. Pour un lanceur à plusieurs étages, calcule chaque étape séparément.

## Fichiers

| Fichier | Rôle |
|---|---|
| [\`index.html\`](index.html) | Calculateur interactif et visualisation de masse |
| [\`main.py\`](main.py) | Fonctions de calcul et interface en ligne de commande |

---

<div align="center">

Projet personnel d’apprentissage en propulsion spatiale et programmation.

</div>