class Vehicule:
    def __init__(self, id_vehicule, marque, modele, annee, prix_jour):
        self.id = id_vehicule
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix_jour = prix_jour
        self.disponible = True

    def to_dict(self):
        return {
            "id": self.id,
            "marque": self.marque,
            "modele": self.modele,
            "annee": self.annee,
            "prix_jour": self.prix_jour,
            "disponible": self.disponible
        }

    def __str__(self):
        statut = "Disponible" if self.disponible else "Loué"
        return f"{self.id} | {self.marque} {self.modele} ({self.annee}) - {self.prix_jour}€/jour [{statut}]"
