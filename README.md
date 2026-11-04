<div align="center">

# Calculateur de Tsiolkovski

### Propulsion · Python · Calcul de delta-v

Estime le delta-v idéal d’une étape de fusée et la masse de propergol consommée.

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Sans dépendance](https://img.shields.io/badge/dépendances-aucune-2E8B57)
![Propulsion spatiale](https://img.shields.io/badge/sujet-propulsion-5865F2)

</div>

---

## Le projet

Un outil pédagogique pour étudier l’équation de Tsiolkovski. Le programme Python demande les paramètres d’un étage et affiche le delta-v idéal ainsi que la masse de propergol consommée.

## Résultats calculés

- Delta-v idéal, en m/s et en km/h.
- Masse de propergol consommée.
- Vérification des entrées et messages d’erreur en cas de valeurs incohérentes.

## Utilisation

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

[\`main.py\`](main.py) contient les fonctions de calcul et l’interface en ligne de commande.

---

<div align="center">

Projet personnel d’apprentissage en propulsion spatiale et programmation.

</div>