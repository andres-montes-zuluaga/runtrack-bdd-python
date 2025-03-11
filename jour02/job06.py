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

# Consultation to get the capacitys of the building's floors
consult = "SELECT capacite FROM salle;"
cur.execute(consult)

# Retrieve results from query execution
resultats = cur.fetchall()

# Show room names and capacities on screen
print(f"La capacité de toutes les salles est de : {sum([fila[0] for fila in resultats])}") 


# Close cursor and connection
cur.close()
cnx.close()