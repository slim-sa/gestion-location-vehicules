class Client:
    def __init__(self, id_client, nom, prenom, telephone):
        self.id = id_client
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "telephone": self.telephone
        }

    def __str__(self):
        return f"{self.id} | {self.prenom} {self.nom} - {self.telephone}"
