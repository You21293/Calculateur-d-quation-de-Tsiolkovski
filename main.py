import math


def calcul_delta_v(vitesse_ejection, masse_initiale, masse_finale):
    """
    Calcule le delta-v avec l'équation de Tsiolkovski.
    """
    return vitesse_ejection * math.log(masse_initiale / masse_finale)


def calcul_masse_propergol(masse_initiale, masse_finale):
    """
    Calcule la masse de propergol consommée.
    """
    return masse_initiale - masse_finale


print("=== Calculateur d'équation de Tsiolkovski ===\n")

# Saisie des données
vitesse_ejection = float(input("Vitesse d'éjection des gaz (m/s) : "))
masse_initiale = float(input("Masse initiale (kg) : "))
masse_finale = float(input("Masse finale (kg) : "))

# Vérification des données
if masse_initiale <= 0 or masse_finale <= 0:
    print("Erreur : les masses doivent être positives.")

elif masse_finale >= masse_initiale:
    print("Erreur : la masse finale doit être inférieure à la masse initiale.")

else:
    # Calculs
    delta_v_ms = calcul_delta_v(
        vitesse_ejection,
        masse_initiale,
        masse_finale
    )

    delta_v_kmh = delta_v_ms * 3.6

    masse_propergol = calcul_masse_propergol(
        masse_initiale,
        masse_finale
    )

    # Résultats
    print("\n--- Résultats ---")
    print(f"Delta-v : {delta_v_ms:.2f} m/s")
    print(f"Delta-v : {delta_v_kmh:.2f} km/h")
    print(f"Masse de propergol : {masse_propergol:.2f} kg")
