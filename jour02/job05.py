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

# Consultation to get the superficies of the building's floors
consult = "SELECT superficie FROM etage;"
cur.execute(consult)

# Retrieve results from query execution
resultats = cur.fetchall()

# Show room names and capacities on screen
print(f"La superficie de La Plateforme est de : {sum([fila[0] for fila in resultats])} m²") 


# Close cursor and connection
cur.close()
cnx.close()