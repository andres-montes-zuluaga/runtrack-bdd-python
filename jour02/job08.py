import mysql.connector

class Zoo:
    def __init__(self, host, user, password, database):
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conexion.cursor()
        print("Connexion zoo établie.")

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.conexion.commit()
        print(f"Animal {nom} ajouté avec succès.")

    def supprimer_animal(self, animal_id):
        query = "DELETE FROM animal WHERE id = %s"
        self.cursor.execute(query, (animal_id,))
        self.conexion.commit()
        print(f"Animal avec ID {animal_id} supprimé.")

    def modifier_animal(self, animal_id, nom=None, race=None, id_cage=None, date_naissance=None, pays_origine=None):
        updates = []
        values = []
        if nom:
            updates.append("nom = %s")
            values.append(nom)
        if race:
            updates.append("race = %s")
            values.append(race)
        if id_cage:
            updates.append("id_cage = %s")
            values.append(id_cage)
        if date_naissance:
            updates.append("date_naissance = %s")
            values.append(date_naissance)
        if pays_origine:
            updates.append("pays_origine = %s")
            values.append(pays_origine)
        
        query = f"UPDATE animal SET {', '.join(updates)} WHERE id = %s"
        values.append(animal_id)
        self.cursor.execute(query, values)
        self.conexion.commit()
        print(f"Animal avec ID {animal_id} modifié.")

    def ajouter_cage(self, superficie, capacite_max):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        values = (superficie, capacite_max)
        self.cursor.execute(query, values)
        self.conexion.commit()
        print("Cage ajoutée avec succès.")

    def supprimer_cage(self, cage_id):
        query = "DELETE FROM cage WHERE id = %s"
        self.cursor.execute(query, (cage_id,))
        self.conexion.commit()
        print(f"Cage avec ID {cage_id} supprimée.")

    def afficher_animaux(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        resultats = self.cursor.fetchall()
        print("Animaux dans le zoo:")
        for animal in resultats:
            print(animal)

    def afficher_animaux_par_cage(self):
        query = """
        SELECT cage.id AS id_cage, cage.superficie, animal.nom AS nom_animal, animal.race
        FROM cage
        LEFT JOIN animal ON cage.id = animal.id_cage
        """
        self.cursor.execute(query)
        resultats = self.cursor.fetchall()
        print("Animaux par cage:")
        for resultat in resultats:
            print(resultat)

    def calculer_superficie_totale(self):
        query = "SELECT SUM(superficie) AS superficie_totale FROM cage"
        self.cursor.execute(query)
        superficie_totale = self.cursor.fetchone()[0]
        print(f"La superficie totale des cages est: {superficie_totale} m².")

    
    def fermer_conexion(self):
        if self.cursor and not self.cursor.close:
            self.cursor.close()
            print("Curseur fermé.")
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Connexion fermée.")

# Inicializa la clase Zoo
zoo_manager = Zoo(host="localhost", user="root", password="123456789", database="zoo")

# Ejemplos de uso:
zoo_manager.ajouter_cage(50.5, 5)
zoo_manager.ajouter_cage(30.0, 3)

zoo_manager.ajouter_animal("Lion", "Panthera leo", 1, "2015-06-12", "Afrique")
zoo_manager.ajouter_animal("Tigre", "Panthera tigris", 1, "2017-04-03", "Asie")
zoo_manager.ajouter_animal("Éléphant", "Loxodonta", 2, "2010-01-15", "Afrique")

zoo_manager.afficher_animaux()
zoo_manager.afficher_animaux_par_cage()
zoo_manager.calculer_superficie_totale()

# Explicitly close the connection
zoo_manager.fermer_conexion()