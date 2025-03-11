import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        # Initialize the database connection
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conexion.cursor()
        print("Database connection established.")

    def creer_employe(self, nom, prenom, salaire, id_service):
        # Create a new record in the employe table
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.conexion.commit()
        print(f"Employé {nom} {prenom} créé avec succès.")

    def lire_employes(self):
        # Retrieve all employees
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        print("Liste des employés :")
        for fila in resultados:
            print(fila)

    def mettre_a_jour_employe(self, employe_id, nom=None, prenom=None, salaire=None, id_service=None):
        # Update an existing employee
        query = "UPDATE employe SET "
        updates = []
        valores = []

        if nom:
            updates.append("nom = %s")
            valores.append(nom)
        if prenom:
            updates.append("prenom = %s")
            valores.append(prenom)
        if salaire:
            updates.append("salaire = %s")
            valores.append(salaire)
        if id_service:
            updates.append("id_service = %s")
            valores.append(id_service)

        query += ", ".join(updates) + " WHERE id = %s"
        valores.append(employe_id)

        self.cursor.execute(query, valores)
        self.conexion.commit()
        print(f"L'employé avec l'ID {employe_id} a été correctement mis à jour.")

    def supprimer_employe(self, employe_id):
        # Delete an employee by ID
        query = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(query, (employe_id,))
        self.conexion.commit()
        print(f"L'employé avec l'ID {employe_id} a été supprimé avec succès.")

    def fermer_conexion(self):
        if self.cursor and not self.cursor.close:
            self.cursor.close()
            print("Curseur fermé.")
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Connexion fermée.")


# SELECT * FROM employe WHERE salaire > 3000;


# Initialize the class with your database credentials
employe_manager = Employe(host="localhost", user="root", password="123456789", database="laplateforme")

# Create a new employee
employe_manager.creer_employe("Dupont", "Marie", 4500.00, 2)

# Read all employees
employe_manager.lire_employes()

# Update an employee (e.g., change the salary)
employe_manager.mettre_a_jour_employe(1, salaire=5000.00)

# Delete an employee
employe_manager.supprimer_employe(1)

# Explicitly close the connection
employe_manager.fermer_conexion()