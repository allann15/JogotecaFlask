from jogoteca import app
from flask import render_template, request, redirect, session, flash, url_for
from helpers import  FormularioUsuario
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
  proxima = request.args.get('proxima')
  form = FormularioUsuario()
  return render_template('login.html', titulo='Faça seu Login', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
  from models import Usuarios
  form = FormularioUsuario(request.form)
  usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
  senha = check_password_hash(usuario.senha, form.senha.data)
  if usuario and senha:
    session['usuario_logado'] = usuario.nickname
    flash(usuario.nickname + ' foi logado com sucesso')
    proxima_pagina = request.form['proxima']
    return redirect(url_for('ola'))



  else:
    flash('Usuário Não foi logado')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
  session['usuario_logado'] = None
  flash('Logout realizado com Sucesso')
  return redirect(url_for('ola'))
