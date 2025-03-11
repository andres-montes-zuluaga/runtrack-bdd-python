import mysql.connector

# Connection to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="laplateforme"
)

# Create a cursor to execute queries
cur = cnx.cursor()

# Consultation to get the names and capacities of rooms
consult = "SELECT nom, capacite FROM salle;"
cur.execute(consult)

# Retrieve results from query execution
resultats = cur.fetchall()

# Show room names and capacities on screen
print("Noms et capacités des salles :")
for fila in resultats:
    print(f"Nom : {fila[0]}, Capacité : {fila[1]}")


# Close cursor and connection
cur.close()
cnx.close()