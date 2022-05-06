from flask import render_template,flash, redirect, url_for, request
from app import app,db

import pandas as pd
from app.forms import RegisterForm,LoginForm,PasswordResetRequestForm,GetDataForm,CleanForm,CloudWordForm,Td_IdfForm,MoodForm,K_meansForm,ResetPasswordForm
from flask_login import login_user,login_required,current_user,logout_user
from app.models import User
from app.email import send_reset_password_mail
from app.Pachong import Pachong
from app.Clean import Clean
from app.TDIDF import TDIDF
from app.Mood import Mood
from app.K_means import K_means

@app.route('/')
@login_required
def index():
    title = '微博热点发现'
    return render_template('index.html', title=title)

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form =RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user=User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('恭喜注册成功!',category='success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
       return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        #check if password ismatched
        user = User.query.filter_by(username=username).first()
        if user and password==user.password:
            #User exists and password matched
            login_user(user, remember=remember)
            flash('登陆成功!',category='info')
            if request.args.get('next'):
                next_page = request.args.get('next')
                #return redirect(url_for(next_page))
                return redirect(next_page)
            return redirect(url_for('index'))
        flash('用户不存在或密码错误！',category='danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/send_password_reset_request',methods=['GET','POST'])
def send_password_reset_request():
    if current_user.is_authenticated:
       return redirect(url_for('index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        token = user.generate_reset_password_token()
        send_reset_password_mail(user,token)
        flash('密码重置邮件已经发送，请检查你的邮箱!',category='info')
    return render_template('send_password_reset_request.html', form=form)

@app.route('/reset_password/<token>',methods=['GET','POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = User.check_reset_password_token(token)
        if user:

            user.password = form.password.data
            db.session.commit()
            flash('密码修改成功，返回登陆！',category='info')
            return redirect(url_for('login'))
        else:
            flash('用户不存在',category='info')
            return redirect(url_for('login'))
    return render_template('reset_password.html',form = form)




@app.route('/getdata',methods=['GET','POST'])
def getdata():
    form = GetDataForm()
    if form.validate_on_submit():

        search = form.search.data

        filename = form.filename.data
        path = f'data/csvdata/{filename}.csv'
        pachong = Pachong(search,filename)
        pachong.action()
        data = pd.read_csv(path)
        title = len(data)

        flash('搜索成功!',category='success')
        return render_template('getdata.html', form=form, data=data, title=title, filename=filename,flag =1)
    return render_template('getdata.html', form=form,flag =0)


@app.route('/cleanfile',methods=['GET','POST'])
def cleanfile():
    form = CleanForm()
    if form.validate_on_submit():
        clean_filname = form.clean_filename.data
        clean = Clean(clean_filname)
        clean.action()
        path02 = str(clean_filname).replace(".csv", '')
        with open(f'data/txtdata/预处理后{path02}文本.txt', 'r', encoding='utf-8') as f:
            txt = f.readlines()
            num = len(txt)
        flash('清洗成功!',category='success')
        return render_template('cleanfile.html', form=form,txt=txt,filename = path02,num=num,flag=1)

    return render_template('cleanfile.html',form=form,flag=0)

@app.route('/cloudword',methods=['GET','POST'])
def cloudword():
    form = CloudWordForm()
    if form.validate_on_submit():
        cloudwordname = form.cloudwordname.data
        clean = Clean(cloudwordname)
        clean.picture(cloudwordname)
        path02 = str(cloudwordname).replace(".txt", '')
        photo = f'static/images/{path02}.png'
        flash('词云展示成功!',category='success')
        return render_template('cloudword.html',form=form,filename=cloudwordname,photo=photo,flag=1)

    return render_template('cloudword.html',form=form,flag=0)

@app.route('/td_idf',methods=['GET','POST'])
def td_idf():
    form = Td_IdfForm()
    if form.validate_on_submit():
        td_idfname = form.td_idfname.data
        tdidf1 = TDIDF(td_idfname)
        weight,word=tdidf1.tdidf()
        #print(word)
        lenword = len(word)
        lenweight = len(weight)
        flash('处理成功!',category='td_idftdtdsuccess')
        return render_template('td_idf.html',form=form,filename=td_idfname,weight=weight,word=word,lenweight=lenweight,lenword=lenword,flag=1)

    return render_template('td_idf.html',form=form,flag=0)

@app.route('/mood',methods=['GET','POST'])
def mood():
    form = MoodForm()
    if form.validate_on_submit():
        moodname = form.moodname.data
        mood = Mood(moodname)
        mood.action()
        path = str(moodname).replace(".csv", '')
        photo = f'static/images/{path}情感分析.png'
        flash('情感分析成功!',category='success')
        return render_template('mood.html',form=form,filename=moodname,photo=photo,flag=1)

    return render_template('mood.html',form=form,flag=0)

@app.route('/k_means',methods=['GET','POST'])
def k_means():
    form = K_meansForm()
    if form.validate_on_submit():
        filename = form.filename.data
        k = form.k.data
        k_means = K_means(filename, int(k))
        k_means.action()
        path = str(filename).replace("文本.txt", '')
        photo = f'static/images/{path}聚类.png'
        flash('K-means聚类成功!',category='success')
        return render_template('k_means.html',form=form,filename=filename,photo=photo,flag=1)

    return render_template('k_means.html',form=form,flag=0)