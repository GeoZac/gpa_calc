from flask import request, render_template, Flask, jsonify, redirect, url_for

# create the application object
app = Flask( __name__ )

def gpa2per(gpa):
    per = 10*gpa -3.75
    return per

# set total credit
def setsem (sem):
    global totalcre
    if sem == 1:
        totalcre = float( 22 )
    if sem == 2:
        totalcre = float( 19 )
    if sem == 3:
        totalcre = float( 14 )
    if sem == 4:
        totalcre = float( 12 )
    return totalcre


# sem1 with 8 subs
def gpacalc1 (sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sem):
    totalcre = setsem( sem )
    sub1 = float( sub1 )
    sub2 = float( sub2 )
    sub3 = float( sub3 )
    sub4 = float( sub4 )
    sub5 = float( sub5 )
    sub6 = float( sub6 )
    sub7 = float( sub7 )
    sub8 = float( sub8 )
    gpa = (sub1 * 3) + (sub2 * 4) + (sub3 * 4) + (sub4 * 3) + (sub5 * 3) + (sub6 * 2) + (sub7 * 2) + (sub8 * 1)
    gpa = gpa / totalcre
    return gpa


# sem2 with 7 subs
def gpacalc2 (sub1, sub2, sub3, sub4, sub5, sub6, sub7, sem):
    totalcre = setsem( sem )
    sub1 = float( sub1 )
    sub2 = float( sub2 )
    sub3 = float( sub3 )
    sub4 = float( sub4 )
    sub5 = float( sub5 )
    sub6 = float( sub6 )
    sub7 = float( sub7 )
    gpa = (sub1 * 4) + (sub2 * 3) + (sub3 * 3) + (sub4 * 3) + (sub5 * 3) + (sub6 * 2) + (sub7 * 1)
    gpa = gpa / totalcre
    return gpa


# sem3 with 4 subs
def gpacalc3 (sub1, sub2, sub3, sub4, sem):
    totalcre = setsem( sem )
    sub1 = float( sub1 )
    sub2 = float( sub2 )
    sub3 = float( sub3 )
    sub4 = float( sub4 )
    gpa = (sub1 * 3) + (sub2 * 3) + (sub3 * 2) + (sub4 * 6)
    gpa = gpa / totalcre
    return gpa


# sem4 with 1 sub
def gpacalc4 (sub1, sem):
    totalcre = setsem( sem )
    sub1 = float( sub1 )
    gpa = (sub1 * 12)
    gpa = gpa / totalcre
    return gpa


# welcome page
@app.route( '/', methods=[ 'GET', 'POST' ] )
def welcome ( ):
    return render_template( 'index.html' )

@app.route( '/main', methods=[ 'GET', 'POST' ] )
def main():
    return render_template('main.html')

@app.route( '/wip', methods=[ 'GET', 'POST' ] )
def wip():
    return render_template('wip.html')



# calulate gpa on s1 div
@app.route( '/s1', methods=[ 'GET', 'POST' ] )
def s1 ( ):
    sem = 1
    sub1 = request.form[ 'sub1' ]
    sub2 = request.form[ 'sub2' ]
    sub3 = request.form[ 'sub3' ]
    sub4 = request.form[ 'sub4' ]
    sub5 = request.form[ 'sub5' ]
    sub6 = request.form[ 'sub6' ]
    sub7 = request.form[ 'sub7' ]
    sub8 = request.form[ 'sub8' ]
    gpa = gpacalc1( sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sem )
    per = round(gpa2per(gpa), ndigits=2)
    gpar = round( gpa, ndigits=2 )
    gpstr = str( gpar )
    return render_template( 'out.html', gpa=gpstr, sem=sem,per = per)  # pass out sem and gpa


@app.route( '/s2', methods=[ 'GET', 'POST' ] )
def s2 ( ):
    sem = 2
    sub1 = request.form[ 'sub1' ]
    sub2 = request.form[ 'sub2' ]

    sub3 = request.form[ 'sub3' ]
    sub4 = request.form[ 'sub4' ]
    sub5 = request.form[ 'sub5' ]
    sub6 = request.form[ 'sub6' ]
    sub7 = request.form[ 'sub7' ]
    gpa = gpacalc2( sub1, sub2, sub3, sub4, sub5, sub6, sub7, sem )
    per = round ( gpa2per ( gpa ), ndigits=2 )
    gpar = round( gpa, ndigits=2 )
    gpstr = str( gpar )
    return render_template( 'out.html', gpa=gpstr, sem=sem, per=per )


@app.route( '/s3', methods=[ 'GET', 'POST' ] )
def s3 ( ):
    sem = 3
    sub1 = request.form[ 'sub1' ]
    sub2 = request.form[ 'sub2' ]
    sub3 = request.form[ 'sub3' ]
    sub4 = request.form[ 'sub4' ]
    gpa = gpacalc3( sub1, sub2, sub3, sub4, sem )
    per = round ( gpa2per ( gpa ), ndigits=2 )
    gpar = round( gpa, ndigits=2 )
    gpstr = str( gpar )
    return render_template( 'out.html', gpa=gpstr, sem=sem, per=per )


@app.route( '/s4', methods=[ 'GET', 'POST' ] )
def s4 ( ):
    sem = 4
    sub1 = request.form[ 'sub1' ]
    gpa = gpacalc4( sub1, sem )
    per = round ( gpa2per ( gpa ), ndigits=2 )
    gpar = round( gpa, ndigits=2 )
    gpstr = str( gpar )
    return render_template( 'out.html', gpa=gpstr, sem=sem, per=per)


@app.route( '/sgpa', methods=[ 'GET', 'POST' ] )
def cgpacalc ( ):
    sgpa1 = request.args.get( 's1', 0, type=float )
    sgpa2 = request.args.get( 's2', 0, type=float )
    sgpa3 = request.args.get( 's3', 0, type=float )
    sgpa4 = request.args.get( 's4', 0, type=float )
    if sgpa1 == 0:
        return jsonify( result='Invalid Input' )
    else:
        cgpa = sgpa1
        sem = '1'
        if sgpa2 != 0:
            cgpa = sgpa1 * 22 + sgpa2 * 19
            cgpa = cgpa / 41
            sem = '2'
            if sgpa3 != 0:
                cgpa = sgpa1 * 22 + sgpa2 * 19 + sgpa3 * 14
                cgpa = cgpa / 55
                sem = '3'
                if sgpa4 != 0:
                    cgpa = sgpa1 * 22 + sgpa2 * 19 + sgpa3 * 14 + sgpa4 * 12
                    cgpa = cgpa / 67
                    sem = '4'
    cgpr = round(cgpa, ndigits=2 )
    percent = 10*cgpa - 3.75
    str = 'Your CGPA till semester {0} is {1} ,this is equivalent to {2} %'.format(sem, cgpr,percent)
    return jsonify(result=str)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()
#TODO add links to all pages,
# MAKE PAGES
#jsonify sgpa
#find fracture

