from math import sqrt, pi
import matplotlib.pylab as pylab
from scipy.integrate import odeint
from pylab import arange, array
from io import BytesIO
import base64

'''
All thanks to Neal Gordon of ifcuriousthenlearn.com to share his code sample
'''


def vibration_response(k, m, ch, c, x0, v0):
    def func(state, t):
        x, xd = state  # displacement,x and velocity x'
        if ch == 2:  # metres per second**2
            xdd = -k * x / m - c * xd
        else:  # metres per second**2
            xdd = ((-k * x) / m)
        return [xd, xdd]
    tpi = 2 * pi
    fn = sqrt(k / m)
    fn = fn / tpi
    state0 = [x0, v0]  # initial conditions [x0 , v0]  [m, m/sec]
    ti = 0.0  # initial time
    tf = 4.0  # final time
    step = 0.001  # step
    t = arange(ti, tf, step)
    if ch == 2:
        state = odeint(func, state0, t)
        x = array(state[:, [0]])
        xd = array(state[:, [1]])

    # Plotting displacement and velocity
    # pylab.ion()   Plot Inline
    pylab.rcParams['figure.figsize'] = (15, 12)
    pylab.rcParams['font.size'] = 18
    fig, ax1 = pylab.subplots()
    ax2 = ax1.twinx()
    ax1.plot(t, x * 1e3, 'b', label=r'$x (mm)$', linewidth=2.0)
    ax2.plot(t, xd, 'g--', label=r'$\dot{x} (m/sec)$', linewidth=2.0)
    ax2.legend(loc='lower right')
    ax1.legend()
    ax1.set_xlabel('time , sec')
    ax1.set_ylabel('disp (mm)', color='b')
    ax2.set_ylabel('velocity (m/s)', color='g')
    pylab.title('System Response')
    pylab.grid()
    # pylab.show(block=True)
    # pylab.savefig('vib.png')
    figfile = BytesIO()
    pylab.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    return figdata_png


'''
To run as standalone module,
replace the arguments sof the function call and uncomment line 45
To save file on disk, uncomment line 46
Syntax  vibration_response(
                            stiffness,
                            mass
                            system type, 1 = mass,spring    2 = mass,spring,damper
                            initial displacement
                            initial velocity
                            )
'''
if __name__ == '__main__':
    vibration_response(12345, 45, 2, 4.56, 0.0, 1.0)
