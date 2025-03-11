import mysql.connector

# Connection to the database using the data in the file
cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456789",
    database = "laplateforme"
)

# Create a cursor to execute queries
cur = cnx.cursor()

# Consultation to get all students
consult = "SELECT * FROM etudiant;"
cur.execute(consult)

# Retrieve and display results
resultats = cur.fetchall()
print("Etudiants:")
for ligne in resultats:
    print(ligne)

# Close cursor and connection
cur.close()
cnx.close()
