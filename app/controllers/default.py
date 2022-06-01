from flask import request,send_from_directory
from pathlib import Path
from app import app

import os


@app.route("/")
def home():
    return 'funcionando'


@app.route("/certificado",methods=['GET', 'POST'])
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

        caminho_raiz_aplicacao = os.getcwd()
        
        file = request.files['file']
        req = {
            "end_point": request.form['end-point'],
            'nome_arquivo': request.form['nome_arquivo']
        }
        path_diretorio = f"{caminho_raiz_aplicacao}\\app\\certificados\\{req['end_point']}"
        
        diretorio = Path(path_diretorio)
        diretorio.mkdir(parents=True, exist_ok=True)

        file.save(f"{path_diretorio}\\{req['nome_arquivo']}")
        
        return 'arquivo salvo'