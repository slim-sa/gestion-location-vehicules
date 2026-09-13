import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
import os
from classes.vehicule import Vehicule
from classes.client import Client
from classes.location import Location

DATA_FILE = "data/stock.json"

def charger_donnees(vehicules, clients, locations):
    if not os.path.exists(DATA_FILE):
        os.makedirs("data", exist_ok=True)
        return 1, 1, 1

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    for v in data.get("vehicules", []):
        veh = Vehicule(v["id"], v["marque"], v["modele"], v["annee"], v["prix_jour"])
        veh.disponible = v.get("disponible", True)
        vehicules.append(veh)

    for c in data.get("clients", []):
        client = Client(c["id"], c["nom"], c["prenom"], c["telephone"])
        clients.append(client)

    for l in data.get("locations", []):
        client = next((c for c in clients if c.id == l["client_id"]), None)
        veh = next((v for v in vehicules if v.id == l["vehicule_id"]), None)
        if client and veh:
            location = Location(l["id"], client, veh, l["jours"])
            locations.append(location)

    return (
        data.get("next_vehicule_id", 1),
        data.get("next_client_id", 1),
        data.get("next_location_id", 1)
    )

def sauvegarder_donnees(vehicules, clients, locations, ids):
    data = {
        "next_vehicule_id": ids[0],
        "next_client_id": ids[1],
        "next_location_id": ids[2],
        "vehicules": [v.to_dict() for v in vehicules],
        "clients": [c.to_dict() for c in clients],
        "locations": [l.to_dict() for l in locations]
    }
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Données sauvegardées avec succès!")
