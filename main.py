"""Calculateur en ligne de commande pour l'équation de Tsiolkovski."""

import math


def calcul_delta_v(vitesse_ejection: float, masse_initiale: float, masse_finale: float) -> float:
    """Calcule le delta-v idéal, en m/s, pour une étape de fusée."""
    valeurs = (vitesse_ejection, masse_initiale, masse_finale)
    if not all(math.isfinite(valeur) for valeur in valeurs):
        raise ValueError("Les valeurs doivent être des nombres finis.")
    if vitesse_ejection <= 0:
        raise ValueError("La vitesse d'éjection doit être positive.")
    if masse_finale <= 0 or masse_initiale <= masse_finale:
        raise ValueError("Il faut avoir masse initiale > masse finale > 0.")
    return vitesse_ejection * math.log(masse_initiale / masse_finale)


def calcul_masse_propergol(masse_initiale: float, masse_finale: float) -> float:
    """Calcule la masse de propergol consommée, en kg."""
    if not math.isfinite(masse_initiale) or not math.isfinite(masse_finale):
        raise ValueError("Les masses doivent être des nombres finis.")
    if masse_finale <= 0 or masse_initiale <= masse_finale:
        raise ValueError("Il faut avoir masse initiale > masse finale > 0.")
    return masse_initiale - masse_finale


def demander_nombre(message: str) -> float:
    """Lit une valeur numérique finie depuis le terminal."""
    valeur = float(input(message))
    if not math.isfinite(valeur):
        raise ValueError("Saisis une valeur numérique finie.")
    return valeur


def main() -> None:
    print("=== Calculateur de l'équation de Tsiolkovski ===")
    try:
        vitesse_ejection = demander_nombre("Vitesse d'éjection des gaz (m/s) : ")
        masse_initiale = demander_nombre("Masse initiale (kg) : ")
        masse_finale = demander_nombre("Masse finale (kg) : ")

        delta_v = calcul_delta_v(vitesse_ejection, masse_initiale, masse_finale)
        propergol = calcul_masse_propergol(masse_initiale, masse_finale)

    except ValueError as erreur:
        print(f"Erreur : {erreur}")
        return

    print("\n--- Résultats idéaux ---")
    print(f"Delta-v : {delta_v:,.2f} m/s")
    print(f"Delta-v : {delta_v * 3.6:,.2f} km/h")
    print(f"Masse de propergol : {propergol:,.2f} kg")


if __name__ == "__main__":
    main()
