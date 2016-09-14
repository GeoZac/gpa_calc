# import the Flask class from the flask module
from flask import Flask, render_template, request
from math import sqrt, pi
import matplotlib.pylab as pylab
from scipy.integrate import odeint
from pylab import arange, array
import matplotlib.pyplot as plt
from io import BytesIO

# create the application object
app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template('in.html')  # render a template

@app.route('/hello/', methods=['POST'])
def hello():
    def func(state,t):
        x,xd = state # displacement,x and velocity x'
        if ch==2:# metres per second**2
            xdd = -k*x/m -c*xd
        else: # metres per second**2
            xdd = ((-k*x)/m)
        return [xd, xdd]

    k = float(request.form['stiff'])
    m = float(request.form['mass'])
    ch = float(request.form['ch'])
    c = float(request.form['dc'])
    tpi = 2 * pi
    fn = sqrt(k / m)
    fn = fn/tpi
    x0 = float(request.form['x0'])
    v0 = float(request.form['v0'])
    state0 = [x0, v0]  #initial conditions [x0 , v0]  [m, m/sec]
    ti = 0.0  # initial time
    tf = 4.0  # final time
    step = 0.001  # step
    t = arange(ti, tf, step)
    if ch==2:
        state = odeint(func,state0, t)
        x = array(state[:,[0]])
        xd = array(state[:,[1]])

# Plotting displacement and velocity
    pylab.ion()
    pylab.rcParams['figure.figsize'] = (15, 12)
    pylab.rcParams['font.size'] = 18

    fig, ax1 = pylab.subplots()
    ax2 = ax1.twinx()
    ax1.plot(t,x*1e3,'b',label = r'$x (mm)$', linewidth=2.0)
    ax2.plot(t,xd,'g--',label = r'$\dot{x} (m/sec)$', linewidth=2.0)
    ax2.legend(loc='lower right')
    ax1.legend()
    ax1.set_xlabel('time , sec')
    ax1.set_ylabel('disp (mm)',color='b')
    ax2.set_ylabel('velocity (m/s)',color='g')
    pylab.title('System Response')
    pylab.grid()
    pylab.show(block=True)
    pylab.savefig('foo.png')
    return render_template("welcome.html", name=k, email=m, w=fn,ch=ch)



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()
