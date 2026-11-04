<div align="center">

# Calculateur de l’équation de Tsiolkovski

**Estimer le delta-v idéal et la masse de propergol d’une étape de fusée.**

Écrit en Python, sans dépendance externe.

</div>

---

## Aperçu

Le programme demande la vitesse d’éjection des gaz, la masse initiale et la masse finale. Il calcule ensuite la variation de vitesse idéale et la masse de propergol consommée.

## Modèle

L’équation de Tsiolkovski s’écrit :

$$
\Delta v = v_e \ln\left(\frac{m_0}{m_f}\right)
$$

La masse de propergol consommée est :

$$
m_{\mathrm{propergol}} = m_0 - m_f
$$

où $v_e$ est la vitesse d’éjection effective, $m_0$ la masse initiale et $m_f$ la masse finale après consommation du propergol.

## Prérequis

- Python 3.10 ou version ultérieure.
- Aucune bibliothèque à installer.

## Lancer le programme

Depuis le dossier du projet :

\`\`\`bash
python main.py
\`\`\`

Sous Windows, cette commande peut aussi être :

\`\`\`powershell
py main.py
\`\`\`

Saisis les valeurs demandées en unités SI : vitesse en mètres par seconde et masses en kilogrammes.

### Exemple

\`\`\`text
=== Calculateur de l'équation de Tsiolkovski ===
Vitesse d'éjection des gaz (m/s) : 3000
Masse initiale (kg) : 50000
Masse finale (kg) : 20000

--- Résultats idéaux ---
Delta-v : 2,748.87 m/s
Delta-v : 9,895.93 km/h
Masse de propergol : 30,000.00 kg
\`\`\`

## Limites du modèle

Le résultat est une estimation idéale pour une étape. Cette équation seule ne prend pas en compte la gravité pendant la poussée, la traînée atmosphérique, les pertes de pilotage ni les limites du moteur. Pour une fusée à plusieurs étages, chaque étape doit être calculée séparément.

## Structure

- \`main.py\` : fonctions de calcul et interface en ligne de commande.

## Auteur

Projet personnel d’apprentissage en propulsion spatiale et en programmation Python.