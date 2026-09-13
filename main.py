from classes.vehicule import Vehicule
from classes.client import Client
from classes.location import Location
from utils.api_nhtsa import ajouter_vehicule_via_api
from utils.json_manager import charger_donnees, sauvegarder_donnees

vehicules = []
clients = []
locations = []

next_v_id, next_c_id, next_l_id = charger_donnees(vehicules, clients, locations)

def menu():
    global next_v_id, next_c_id, next_l_id

    while True:
        print("\n" + "="*50)
        print("    GESTION LOCATION DE VÉHICULES")
        print("="*50)
        print("1.  Ajouter véhicule")
        print("2.  Ajouter véhicule via API")
        print("3.  Afficher véhicules")
        print("4.  Supprimer véhicule")
        print("5.  Ajouter client")
        print("6.  Supprimer client")
        print("7.  Louer un véhicule")
        print("8.  Supprimer une location")
        print("9.  Afficher toutes les locations")
        print("10. Sauvegarder")
        print("11. Charger (recharge manuelle)")
        print("12. Quitter")
        choix = input("\nChoisissez une option : ").strip()

        if choix == "1":
            marque = input("Marque : ")
            modele = input("Modèle : ")
            annee = int(input("Année : "))
            prix = float(input("Prix par jour (€) : "))
            vehicules.append(Vehicule(next_v_id, marque, modele, annee, prix))
            next_v_id += 1
            print("Véhicule ajouté !")

        elif choix == "2":
            data = ajouter_vehicule_via_api()
            if data:
                vehicules.append(Vehicule(next_v_id, data["marque"], data["modele"], data["annee"], data["prix_jour"]))
                next_v_id += 1
                print("Véhicule ajouté via API !")

        elif choix == "3":
            print("\nListe des véhicules :")
            for v in vehicules:
                print(v)

        elif choix == "4":
            if not vehicules:
                print("Aucun véhicule.")
                continue
            for v in vehicules:
                print(v)
            id_sup = int(input("ID du véhicule à supprimer : "))
            veh = next((v for v in vehicules if v.id == id_sup), None)
            if veh:
                locations[:] = [loc for loc in locations if loc.vehicule.id != id_sup]
                vehicules[:] = [v for v in vehicules if v.id != id_sup]
                print(f"Véhicule {id_sup} et ses locations supprimés.")
            else:
                print("Véhicule non trouvé.")

        elif choix == "5":
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            tel = input("Téléphone : ")
            clients.append(Client(next_c_id, nom, prenom, tel))
            next_c_id += 1
            print("Client ajouté !")

        elif choix == "6":
            if not clients:
                print("Aucun client.")
                continue
            for c in clients:
                print(c)
            id_client = int(input("ID du client à supprimer : "))
            client = next((c for c in clients if c.id == id_client), None)
            if client:
                locations[:] = [loc for loc in locations if loc.client.id != id_client]
                clients[:] = [c for c in clients if c.id != id_client]
                print(f"Client {id_client} et toutes ses locations supprimés.")
            else:
                print("Client non trouvé.")

        elif choix == "7":
            if not clients or not any(v.disponible for v in vehicules):
                print("Pas de clients ou de véhicules disponibles !")
                continue
            print("\nClients :")
            for c in clients: print(c)
            client_id = int(input("ID client : "))
            client = next((c for c in clients if c.id == client_id), None)

            print("\nVéhicules disponibles :")
            dispo = [v for v in vehicules if v.disponible]
            for v in dispo: print(v)
            veh_id = int(input("ID véhicule : "))
            veh = next((v for v in vehicules if v.id == veh_id and v.disponible), None)

            if client and veh:
                jours = int(input("Nombre de jours : "))
                locations.append(Location(next_l_id, client, veh, jours))
                next_l_id += 1
                print(f"Location créée ! Montant total : {jours * veh.prix_jour} €")
            else:
                print("Client ou véhicule invalide ou non disponible")

        elif choix == "8":
            if not locations:
                print("Aucune location.")
                continue
            for loc in locations:
                print(loc)
            id_loc = int(input("ID de la location à supprimer : "))
            location = next((loc for loc in locations if loc.id == id_loc), None)
            if location:
                location.vehicule.disponible = True
                locations[:] = [loc for loc in locations if loc.id != id_loc]
                print(f"Location {id_loc} supprimée. Véhicule remis disponible.")
            else:
                print("Location non trouvée.")

        elif choix == "9":
            print("\nToutes les locations :")
            if not locations:
                print("Aucune location.")
            for loc in locations:
                print(loc)

        elif choix == "10":
            sauvegarder_donnees(vehicules, clients, locations, (next_v_id, next_c_id, next_l_id))

        elif choix == "11":
            vehicules.clear()
            clients.clear()
            locations.clear()
            next_v_id, next_c_id, next_l_id = charger_donnees(vehicules, clients, locations)
            print("Données rechargées avec succès !")

        elif choix == "12":
            sauvegarder_donnees(vehicules, clients, locations, (next_v_id, next_c_id, next_l_id))
            print("Au revoir !")
            break

if __name__ == "__main__":
    menu()
