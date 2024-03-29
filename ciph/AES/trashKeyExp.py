key = "5468617473206d79204b756e67204675"
# keyTab = [54,68,61,74,73,20,6d,79,20,4b,75,6e,67,20,46,75]

key_words = [key[i:i+4] for i in range(0, len(key), 4)]
print("key_words")

# for (i = 0 ; i < 4 ; i++)
# [key[4*i] , key[4*i+1] , key[4*i+2] , key[4*i+3]]
# for (i = 4; i < 44 ; i++)
# temp = w[i – 1];
# if (i mod 4 = 0)
# temp = SubWord ( RotWord ( temp ) )  Rcon[i / 4];
# w[i] = w[i – 4]  temp

# ----------------------------------\# def login():
    # username = request.form['username']
    # password = request.form['pswd']

    # cursor = db.cursor()

    # # Vérification des informations de connexion dans la base de données
    # query = "SELECT * FROM cipher WHERE utilisateur = %s AND password = %s"
    # cursor.execute(query, (username, password))
    # user = cursor.fetchone()

    # if user:
    #     # Connexion réussie, rediriger vers une page de succès
    #     return redirect(url_for('index')) 
    # else:
    #     # Identifiants invalides, rediriger vers une page d'erreur
    #     return render_template('login.html', pageTitle="login", message="Erreur :( Compte inexistant.")

    # # return render_template('reg.html')