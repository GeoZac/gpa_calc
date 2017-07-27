from flask import request, render_template,Flask

# create the application object
app = Flask( __name__ )

#set total credit
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


#sem1 with 8 subs
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

#sem2 with 7 subs
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

#sem3 with 4 subs
def gpacalc3 (sub1, sub2, sub3, sub4, sem):
    totalcre = setsem( sem )
    sub1 = float( sub1 )
    sub2 = float( sub2 )
    sub3 = float( sub3 )
    sub4 = float( sub4 )
    gpa = (sub1 * 3) + (sub2 * 3) + (sub3 * 2) + (sub4 * 6)
    gpa = gpa / totalcre
    return gpa

#sem4 with 1 sub
def gpacalc4 (sub1, sem):
    totalcre = setsem( sem )
    sub1 = float( sub1 )
    gpa = (sub1 * 12)
    gpa = gpa / totalcre
    return gpa

# welcome page
@app.route( '/', methods=[ 'GET', 'POST' ] )
def welcome ( ):
    return render_template( 'main.html' )

#calulate gpa on s1 div
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
    gpar = round( gpa, ndigits=2 )
    gpstr = str( gpar )
    return render_template( 'out.html', gpa=gpstr, sem=sem ) # pass out sem and gpa


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
    gpar = round( gpa, ndigits=2 )
    gpstr = str( gpar )
    return render_template( 'out.html', gpa=gpstr, sem=sem )


@app.route( '/s3', methods=[ 'GET', 'POST' ] )
def s3 ( ):
    sem = 3
    sub1 = request.form[ 'sub1' ]
    sub2 = request.form[ 'sub2' ]
    sub3 = request.form[ 'sub3' ]
    sub4 = request.form[ 'sub4' ]
    gpa = gpacalc3( sub1, sub2, sub3, sub4, sem )
    gpar = round( gpa, ndigits=2 )
    gpstr = str( gpar )
    return render_template( 'out.html', gpa=gpstr, sem=sem )


@app.route( '/s4', methods=[ 'GET', 'POST' ] )
def s4 ( ):
    sem = 4
    sub1 = request.form[ 'sub1' ]
    gpa = gpacalc4( sub1, sem )
    gpar = round( gpa, ndigits=2 )
    gpstr = str( gpar )
    return render_template( 'out.html', gpa=gpstr, sem=sem )


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()