from flask import request, render_template, Flask, jsonify

from material import *
from mech import *
from gpa import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template('index.html')


@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/wip', methods=['GET', 'POST'])
def wip():
    return render_template('wip.html')


@app.route('/frame', methods=['GET', 'POST'])
def frame():
    return render_template('frame.html')


@app.route('/s1', methods=['GET', 'POST'])
def s1():
    sem = 1
    sub1 = request.form['sub1']
    sub2 = request.form['sub2']
    sub3 = request.form['sub3']
    sub4 = request.form['sub4']
    sub5 = request.form['sub5']
    sub6 = request.form['sub6']
    sub7 = request.form['sub7']
    sub8 = request.form['sub8']
    gpa = gpacalc1(sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sem)
    per = round(gpa2per(gpa), ndigits=2)
    gpar = round(gpa, ndigits=2)
    gpstr = str(gpar)
    return render_template('out.html', gpa=gpstr, sem=sem, per=per)  # pass out sem and gpa


@app.route('/s2', methods=['GET', 'POST'])
def s2():
    sem = 2
    sub1 = request.form['sub1']
    sub2 = request.form['sub2']
    sub3 = request.form['sub3']
    sub4 = request.form['sub4']
    sub5 = request.form['sub5']
    sub6 = request.form['sub6']
    sub7 = request.form['sub7']
    gpa = gpacalc2(sub1, sub2, sub3, sub4, sub5, sub6, sub7, sem)
    per = round(gpa2per(gpa), ndigits=2)
    gpar = round(gpa, ndigits=2)
    gpstr = str(gpar)
    return render_template('out.html', gpa=gpstr, sem=sem, per=per)


@app.route('/s3', methods=['GET', 'POST'])
def s3():
    sem = 3
    sub1 = request.form['sub1']
    sub2 = request.form['sub2']
    sub3 = request.form['sub3']
    gpa = gpacalc3(sub1, sub2, sub3, sem)
    per = round(gpa2per(gpa), ndigits=2)
    gpar = round(gpa, ndigits=2)
    gpstr = str(gpar)
    return render_template('out.html', gpa=gpstr, sem=sem, per=per)


@app.route('/s4', methods=['GET', 'POST'])
def s4():
    sem = 4
    sub1 = request.form['sub1']
    gpa = gpacalc4(sub1, sem)
    per = round(gpa2per(gpa), ndigits=2)
    gpar = round(gpa, ndigits=2)
    gpstr = str(gpar)
    return render_template('out.html', gpa=gpstr, sem=sem, per=per)


@app.route('/sgpa', methods=['GET', 'POST'])
def cgpacalc():
    sgpa1 = request.args.get('s1', 0, type=float)
    sgpa2 = request.args.get('s2', 0, type=float)
    sgpa3 = request.args.get('s3', 0, type=float)
    sgpa4 = request.args.get('s4', 0, type=float)
    if sgpa1 == 0:
        return jsonify(result='Invalid Input')
    else:
        cgpa = sgpa1
        sem = '1'
        if sgpa2 != 0:
            cgpa = sgpa1 * 22 + sgpa2 * 19
            cgpa = cgpa / 41
            sem = '2'
            if sgpa3 != 0:
                cgpa = sgpa1 * 22 + sgpa2 * 19 + sgpa3 * 8
                cgpa = cgpa / 49
                sem = '3'
                if sgpa4 != 0:
                    cgpa = sgpa1 * 22 + sgpa2 * 19 + sgpa3 * 8 + sgpa4 * 18
                    cgpa = cgpa / 67
                    sem = '4'
    cgpr = round(cgpa, ndigits=2)
    percent = gpa2per(cgpr)
    string = 'Your CGPA till semester {0} is {1} ,this is equivalent to {2} %'.format(sem, cgpr, percent)
    return jsonify(result=string)


@app.route('/vibdata', methods=['GET', 'POST'])
def vibdata():
    return render_template("vibdata.html")


@app.route('/vibres', methods=['GET', 'POST'])
def vibres():
    k = float(request.form['stiff'])
    m = float(request.form['mass'])
    ch = float(request.form['ch'])
    c = float(request.form['dc'])
    x0 = float(request.form['x0'])
    v0 = float(request.form['v0'])
    result = vibration_response(k, m, ch, c, x0, v0)
    return render_template('vibres.html', result=result)


@app.route('/material', methods=['GET', 'POST'])
def materialdata():
    mat = request.args.get('id', type=str)
    mat = mat.lower()  # just in case
    try:
        data = material(mat)
        return jsonify(data)
    except KeyError:
        return 'Requested Material not found in Database'


@app.route('/materialapi', methods=['GET', 'POST'])
def api():
    return render_template('mhapi.html')


@app.route('/mohr', methods=['GET', 'POST'])
def mohr():
    return render_template('mohr.html')


@app.route('/mohr2D', methods=['GET', 'POST'])
def mohr_2d():
    try:
        s11 = float(request.form['matrix[0][0]'])
        s22 = float(request.form['matrix[1][1]'])
        try:
            s12 = float(request.form['matrix[0][1]'])
        except ValueError:
            s12 = float(request.form['matrix[1][0]'])
    except ValueError:
        return 'The stress values need to be integers or floating point decimals'
    result = mohr2d(s11, s12, s22)
    return render_template('mohr2d.html', stress2=result)
    # TODO exception handling,following func too


@app.route('/mohr3D', methods=['GET', 'POST'])
def mohr_3d():
    try:
        s11 = float(request.form['matrix[0][0]'])
        s22 = float(request.form['matrix[1][1]'])
        s33 = float(request.form['matrix[2][2]'])
        try:
            s12 = float(request.form['matrix[0][1]'])
            s13 = float(request.form['matrix[1][2]'])
            s23 = float(request.form['matrix[1][2]'])
        except ValueError:
            s12 = float(request.form['matrix[1][0]'])
            s13 = float(request.form['matrix[2][1]'])
            s23 = float(request.form['matrix[2][1]'])
    except ValueError:
        return 'The stress values need to be integers or floating point decimals'
    result = mohr3d(s11, s22, s33, s12, s13, s23)
    return render_template('mohr3d.html', stress3=result)


if __name__ == '__main__':
    app.run()
