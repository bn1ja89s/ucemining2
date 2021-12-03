@app.route('/uploader', methods = ['POST', 'GET'])
def uploader():
    username = session['username']
    user = database.session.query(RegistrosSyP).filter_by(username = username).first()   
    if request.method =="POST":
        if 'archivo' not in request.files:
            return "El formulario no tiene la parte que corresponde al archivo"
        f = request.files['archivo']
        if f.filename == "":
            return  "No se ha seleccionado ningun archivo, intente de nuevo"
        filename = secure_filename(f.filename)
        namefile = username + ".jpg"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], namefile))
        # return redirect(url_for("get_file", name = name))
        return render_template("prueba.html", image_name = namefile)
    return render_template('upload.html')