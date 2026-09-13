from datetime import datetime

class Location:
    def __init__(self, id_location, client, vehicule, jours):
        self.id = id_location
        self.client = client
        self.vehicule = vehicule
        self.date_debut = datetime.now().strftime("%Y-%m-%d")
        self.jours = jours
        self.montant = jours * vehicule.prix_jour
        vehicule.disponible = False

    def to_dict(self):
        return {
            "id": self.id,
            "client_id": self.client.id,
            "vehicule_id": self.vehicule.id,
            "date_debut": self.date_debut,
            "jours": self.jours,
            "montant": self.montant
        }

    def __str__(self):
        return f"Location {self.id} | {self.client} → {self.vehicule.marque} {self.vehicule.modele} | {self.jours} jours | {self.montant}€"
