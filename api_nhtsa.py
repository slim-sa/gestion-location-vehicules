import requests

def ajouter_vehicule_via_api():
    try:
        vin = input("Entrez le VIN du véhicule : ").strip()
        url = f"https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/{vin}?format=json"
        response = requests.get(url, timeout=10)
        data = response.json()

        if data["Results"]:
            make = data["Results"][0].get("Make", "Inconnu")
            model = data["Results"][0].get("Model", "Inconnu")
            year = data["Results"][0].get("ModelYear", "Inconnu")
            print(f"\nDonnées trouvées → Marque: {make}, Modèle: {model}, Année: {year}")
            prix = float(input("Prix de location par jour (€) : "))
            return {"marque": make, "modele": model, "annee": year, "prix_jour": prix}
        else:
            print("Aucune donnée trouvée pour ce VIN.")
            return None
    except Exception as e:
        print("Erreur API ou connexion :", e)
        return None