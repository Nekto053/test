from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send (msg_text):
    recipients_emails=['m089en40@gmail.com']
    login='artemudzumaki@yandex.ru'
    password = '50406793248_a300'

    msg = MIMEText(f'{msg_text}', 'plain', 'utf-8')
    msg['Sudject']=Header("важно", 'utf-8')
    msg['From']=login
    msg['To']=", ".join(recipients_emails)

    s= smtplib.SMTP('smtp.yandex.ru', 587, timeout=10)

    try:
        s.starttls()
        s.login(login, password)
        s.sendmail(msg['From'], recipients_emails, msg.as_string())
    except Exception as ex:
        print(ex)
    finally:
        s.quit()



def vrem():
    dt_now = datetime.datetime.now()
    return dt_now
main=Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///naw3.db'
db=SQLAlchemy(main)


def file(te,v,x):
    if v == 1:
        f = 'zaiavka.txt'
    else:
        f='zaiavka_k.txt'
    with open(f, 'r+', encoding='utf-8') as fil:
        for i in range(len(te)):
            l=fil.readline()
            fil.writelines(x[i]+'|=> '+str(te[i])+'\n')
        send(te)
        fil.write(str(vrem())+'\n')
        fil.write('=======================разделение========================\n\n\n')



class Post(db.Model):
#===================indi=======================================
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(300), nullable=False)
    pasp_dan = db.Column(db.String(300), nullable=False)
    propiska = db.Column(db.String(300), nullable=False)
    egrip = db.Column(db.String(300), nullable=False)
    inn=db.Column(db.String(300), nullable=False)
    bank_rikvezit=db.Column(db.String(300), nullable=False)
    telefon=db.Column(db.String(300), nullable=False)
    al_pochta=db.Column(db.String(300), nullable=False)
    al_pochta_cheta=db.Column(db.String(300), nullable=False)
    bygalteria=db.Column(db.String(300), nullable=False)
    operator_ado=db.Column(db.String(300), nullable=False)
#===================техника=======================================
    tex1 = db.Column(db.String(300), nullable=False)
    tex2 = db.Column(db.String(300), nullable=False)
    tex3 = db.Column(db.String(300), nullable=False)
    tex4 = db.Column(db.String(300), nullable=False)
    tex5= db.Column(db.String(300), nullable=False)
    tex6= db.Column(db.String(300), nullable=False)
    tex7= db.Column(db.String(300), nullable=False)
    tex8= db.Column(db.String(300), nullable=False)
    tex9= db.Column(db.String(300), nullable=False)
    # class kompani(db.Model):
#===================kompani=======================================
    pol_naim = db.Column(db.String(300), nullable=False)
    krat_naim = db.Column(db.String(300), nullable=False)
    ur_adres = db.Column(db.String(300), nullable=False)
    pochtov_adres = db.Column(db.String(300), nullable=False)
    telefax = db.Column(db.String(300), nullable=False)
    al_poc = db.Column(db.String(300), nullable=False)
    ogph = db.Column(db.String(300), nullable=False)
    nhh1 = db.Column(db.String(300), nullable=False)
    kpp = db.Column(db.String(300), nullable=False)
    nomer_rasch_ch = db.Column(db.String(300), nullable=False)
    naim_bank = db.Column(db.String(300), nullable=False)
    bik = db.Column(db.String(300), nullable=False)
    alpoc_chet = db.Column(db.String(300), nullable=False)
    nomer_korcch = db.Column(db.String(300), nullable=False)
    okpo = db.Column(db.String(300), nullable=False)
    gener_dir = db.Column(db.String(300), nullable=False)
    polnomochia_dir = db.Column(db.String(300), nullable=False)
    oper_ado = db.Column(db.String(300), nullable=False)


@main.route('/index')
def index():
    return render_template('index.html')


@main.route("/indi", methods=['POST', 'GET'])
def indi():
    if request.method == 'POST':
        fio = request.form['fio']
        pasp_dan = request.form['pasp_dan']
        propiska = request.form['propiska']
        egrip = request.form['egrip']
        tex1 = request.form['tex1']
        bank_rikvezit = request.form['bank_rikvezit']
        telefon = request.form['telefon']
        al_pochta = request.form['al_pochta']
        al_pochta_cheta = request.form['al_pochta_cheta']
        bygalteria = request.form['bygalteria']
        operator_ado = request.form['operator_ado']
# ===============================================================

        tex2 = request.form['tex2']
        tex3 = request.form['tex3']
        tex4 = request.form['tex4']
        tex5 = request.form['tex5']
        tex6 = request.form['tex6']
        tex7 = request.form['tex7']
        tex8 = request.form['tex8']
        tex9 = request.form['tex9']
        x=["ФИО", "Паспортные данные", "Адрес прописки", "Данные листа записи ЕГРИП о регистрации", "ИНН",
        "Банковские реквезиты (РС,БИК,КС,банк)", "Контактный телефон", "эл. почта", "эл. почта для рассылки счетов",
        "Бухгалтерия", "Операторы ЭДО(если есть)", "данный о технике-1", "данный о технике-2", "данный о технике-3",
        "данный о технике-4", "данный о технике-5", "данный о технике-6", "Точный адрес, ФИО и номер телефона  получателя",
        "Заявку заполнил: ФИО, номер мобильного телефона"]
        te = [fio, pasp_dan, propiska, egrip, tex1, bank_rikvezit, telefon, al_pochta,
              al_pochta_cheta, bygalteria, operator_ado, tex2, tex3, tex4,
              tex5, tex6, tex7, tex8, tex9]


        #post = Post(fio=fio, pasp_dan=pasp_dan,propiska=propiska, egrip=egrip, inn=inn,
        #            bank_rikvezit=bank_rikvezit, telefon=telefon, al_pochta=al_pochta,
        #            al_pochta_cheta=al_pochta_cheta, bygalteria=bygalteria, operator_ado=operator_ado,
        #            tex1='tex1', tex2='tex2', tex3='tex3', tex4='tex4', tex5='tex5',
        #            tex6='tex6', tex7='tex7', tex8='tex8', tex9='tex9' )
        try:
            file(te, 1, x)
            return redirect('/main')
        except:
            return 'при добавлении статьи возникла ошибка'
    else:
        return render_template('indi.html')


@main.route("/kompani", methods=['POST', 'GET'])
def kompani():
    if request.method == 'POST':
        pol_naim = request.form['pol_naim']
        krat_naim = request.form['krat_naim']
        ur_adres = request.form['ur_adres']
        pochtov_adres = request.form['pochtov_adres']
        telefax = request.form['telefax']
        al_poc = request.form['al_poc']
        ogph = request.form['ogph']
        tex1 = request.form['tex1']
        kpp = request.form['kpp']
        nomer_rasch_ch = request.form['nomer_rasch_ch']
        naim_bank = request.form['naim_bank']
        bik = request.form['bik']
        alpoc_chet = request.form['alpoc_chet']
        nomer_korcch = request.form['nomer_korcch']
        okpo = request.form['okpo']
        gener_dir = request.form['gener_dir']
        polnomochia_dir = request.form['polnomochia_dir']
        oper_ado = request.form['oper_ado']
#===============================================================
        tex2 = request.form['tex2']
        tex3 = request.form['tex3']
        tex4 = request.form['tex4']
        tex5 = request.form['tex5']
        tex6 = request.form['tex6']
        tex7 = request.form['tex7']
        tex8 = request.form['tex8']
        tex9 = request.form['tex9']
        x=["Полное наименование", "Краткое наименование", "Юридический адрес", "Почтовый адрес", "Телефакс(отдел, подразделение)",
        "Эл. почта (отдел, подразделение)", "ОГРН", "ИНН", "КПП",
        "Номер расчётного счёта", "Наименование банка", "БИК", "Эл. почта для рассылки счетов(бухгалтерия)", "Номер корсчета",
        "ОКПО", "Гинеральный директор", "Полномочия генерального директора","Операторы ЭДО(если есть)","данный о технике-1",
        "данный о технике-2", "данный о технике-3",
        "данный о технике-4", "данный о технике-5", "данный о технике-6", "Точный адрес, ФИО и номер телефона  получателя",
        "Заявку заполнил: ФИО, номер мобильного телефона"]

        te=[pol_naim+'\n',krat_naim+'\n',ur_adres+'\n',pochtov_adres+'\n',telefax+'\n',al_poc+'\n',ogph+'\n',
            tex1+'\n',kpp+'\n',nomer_rasch_ch+'\n',naim_bank+'\n',bik+'\n',
            alpoc_chet+'\n',nomer_korcch+'\n',okpo+'\n',gener_dir+'\n',polnomochia_dir+'\n',oper_ado+'\n',
            tex2+'\n',tex3+'\n',tex4+'\n',tex5+'\n',tex6+'\n',tex7+'\n',tex8+'\n',tex9+'\n']


        #post = Post(pol_naim='pol_naim', krat_naim='krat_naim', ur_adres='ur_adres', pochtov_adres='pochtov_adres',
        #            telefax='telefax', al_poc='al_poc', ogph='ogph', nhh1='nhh1', kpp='kpp',
        #            nomer_rasch_ch='nomer_rasch_ch', naim_bank='naim_bank', bik='bik', alpoc_chet='alpoc_chet',
        #            nomer_korcch='nomer_korcch', okpo='okpo',gener_dir='gener_dir', polnomochia_dir='polnomochia_dir',
        #            oper_ado='oper_ado', tex1='tex1', tex2='tex2', tex3='tex3', tex4='tex4', tex5='tex5',
        #            tex6='tex6', tex7='tex7', tex8='tex8', tex9='tex9' )
#
        try:

            file(te, 2, x)
            return redirect('/main')


        except:
            return 'при добавлении статьи возникла ошибка'
    else:
        return render_template('kompani.html')


if __name__ == '__main__':
    main.run(debug=True)

