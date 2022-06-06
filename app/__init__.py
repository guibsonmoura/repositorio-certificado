import os
from pathlib import Path
from mega import Mega
from flask import Flask,request,send_from_directory
from flask_cors import CORS,cross_origin



def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/certificado'
    
    @app.route("/")
    def home():
        return 'funcionando'


    @app.route("/certificado",methods=['GET', 'POST'])
    @cross_origin()
    def index():
        print(request.method)

        if request.method == "GET":
            caminho_raiz_aplicacao = os. getcwd()
            end_point =  request.args.get('end_point')
            path_diretorio = f"{caminho_raiz_aplicacao}\\app\\certificados\\{end_point}"
            nome_arquivo = ''
            try:
                arquivos = os.listdir(path_diretorio)
                nome_arquivo = arquivos[0]
            except:
                pass
            print(end_point)
            
            return send_from_directory(path_diretorio,nome_arquivo, as_attachment=True)
            # return 'funcionando'
        elif request.method == "POST":
            mega = Mega()
            login_mega = mega.login(email='mouraguibson12@gmail.com',password='81015021vai')
            print(f'login: {login_mega}')
            caminho_raiz_aplicacao = os.getcwd()
            
            file = request.files['file']
            
            print(file.name)
            print(file.filename)
            file.save(f"./{file.filename}")
            req = {
                "end_point": request.form['end-point'],
                'nome_arquivo': file.filename
            }
            stream_file = file.stream
            
            folder_no = login_mega.find(f"certificados")
            if folder_no != None:
                print('pasta certificados existe')
                #vai gravar na pasta ''certificados''
                folder = login_mega.find(req['end_point'],exclude_deleted=True)
                if folder != None:
                    print('pasta do ent-ponint existe')
                    file_save = login_mega.find(req['nome_arquivo'],exclude_deleted=True)
                    if file_save != None:
                        print('vai fazer upload do arquivo')
                        login_mega.delete(file_save[0])
                        login_mega.upload(req['nome_arquivo'], folder[0])
                        return 'upload do arquivo feito'
                    else:
                        login_mega.upload(req['nome_arquivo'], folder[0])
                        return 'upload do arquivo feito'
                else: 
                    print('vai criar pasta com end-point')
                    login_mega.create_folder(req['end_point'],folder_no[0])
                    folder = login_mega.find(req['end_point'],exclude_deleted=True)
                    login_mega.upload(req['nome_arquivo'], folder[0])
                    return 'upload do arquivo feito'
            else:
                return 'pasta certificados não existe'
    return app
    



