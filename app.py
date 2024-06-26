from flask import Flask, render_template, request, redirect, url_for

import json
from flask import jsonify
# import datetime
import database as base
from ciph import RSA_Algo as cipher


app = Flask(__name__)

# database 
db = base.connecter()
cursor = db.cursor()

# ============================
# sql="INSERT INTO etudiant(matricule, nom, postnom, dateNaissance) VALUES (%s,%s,%s,%s)"
# valeurs=("AFI23","JOSEPH","KAMALA", datetime.date.today())
# curseur=db.cursor()
# curseur.execute(sql,valeurs)
# db.commit()
# ============================

@app.route('/', methods=["GET", "POST"])
def login():
    cursor = db.cursor()
    if request.method == "POST":
        username = request.form['username']
        password = request.form['pswd']
        
        cursor.execute("SELECT * FROM cipher WHERE utilisateur = %s AND password = %s ", (username, password))
        # cursor.execute("SELECT * FROM cipher WHERE utlisateur = %s ", (username, ))
        
        response = cursor.fetchone()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++\n",response)

        if response:
            return redirect(url_for('index'))  
        return render_template('login.html', pageTitle="login", message="Erreur :( Compte inexistant soit mot de pass incorrect.")
    else:
        return render_template('login.html', pageTitle="login")


@app.route('/home', methods=["GET", "POST"])
def index():
    query = "SELECT * FROM etudiant"
    
    
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('index.html', pageTitle="Home",  users=data)
    # return render_template('reg.html')


@app.route("/inscription", methods=['POST','GET'])
def register():
    if request.method == 'POST':
        print('inscription')
        matricule = request.form['mat']
        nom = request.form['nom']
        svNom = cipher.rsa(nom, 33, 3)
        prenom = request.form['prenom']
        svPrenom = cipher.rsa(prenom, 33, 3)
        date = request.form['date']
        
        regQuery = "INSERT INTO etudiant(matricule, nom, postnom, dateNaissance) VALUES (%s,%s,%s,%s)"
        regValues = (matricule, svNom, svPrenom, date,)
        # regValues = (matricule, nom, prenom, date)

        cursor = db.cursor()
        cursor.execute(regQuery, regValues)
        db.commit()
        cursor.close()
        return redirect(url_for('index'))
    
    return render_template("inscription.html", pageTitle="Inscription")



@app.route("/delete/<string:mat>", methods=["GET"])
def delete(mat):
    cursor.execute("DELETE FROM etudiant WHERE matricule = %s", (mat,))
    return redirect(url_for('index'))


@app.route("/update/<string:mat>", methods=["GET", "POST"])
def update(mat):
    if request.method == "POST":
        nom = request.form['nom']
        postnom = request.form['prenom']
        date = request.form['date']
       
        # query = "SELECT * FROM etudiant WRERE matricule=%s"
    
    
        cursor.execute("""UPDATE etudiant SET nom=%s, postnom=%s, dateNaissance=%s WHERE matricule=%s""", (nom, postnom, date, mat))
        db.commit()
        return redirect(url_for('index'))    
    cursor.execute("SELECT * FROM etudiant WHERE matricule = %s", (mat,))
    data = cursor.fetch()
    return render_template("update.html",pageTitle="update", user=data)


# ========================================================== DECHIFFRER =======

# @app.route("/dechif/<string:mat>", methods=["GET"])
# def dechif(mat):
#     cursor.execute("SELECT * FROM etudiant WHERE matricule = %s", (mat,))
#     data = cursor.fetch()
#     mat = data[0]
#     nom = data[1]
#     dechNom = cipher.dechRSA(nom, 33, 3)
#     postnom = data[2]
#     deshP = cipher.dechRSA(postnom, 33, 3)
#     date = data[3]
  
    
    


#     decrypted_data = {
#         'mat' : mat,
#         'nom' : dechNom,
#         'postNom' : dechNom,
#         'date' : date
#     }  

#     return jsonify(decrypted_data)

@app.route("/dechif/<string:mat>", methods=["GET"])
def dechif(mat):
    cursor.execute("SELECT * FROM etudiant WHERE matricule = %s", (mat,))
    data = cursor.fetchall()
    mat = data[0]
    print("mat from the database " ,mat , "\\n😛")
    nom = data[1]
    
    dechNom = cipher.dechRSA(nom, 33, 3)
    postnom = data[2]
    deshP = cipher.dechRSA(postnom, 33, 3)
    date = data[3]
  
    decrypted_data = {
        'mat': mat,
        'nom': dechNom,
        'postNom': deshP,
        'date': date
    }  

    # Fermer le curseur et la connexion à la base de données
    cursor.close()

    return jsonify(decrypted_data)

message = "hi"

print(cipher.rsa(message, 33, 3))
print(" -----------Dechiffrement--------")



# print(rsa(message, 33, 3))
print(cipher.dechRSA(cipher.rsa(message, 33, 3),7,33))


if __name__ == '__main__':
    app.run(debug=True)
