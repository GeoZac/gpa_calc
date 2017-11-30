"""
Module to handle all the mech stuff
"""
from math import sqrt, pi
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from pylab import arange, array
from io import BytesIO
import base64
import numpy as np
from numpy.linalg import eig

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
    return return_img(figfile)


'''
To run as standalone module,
replace the arguments sof the function call and uncomment line 45
To save file on disk, uncomment line 46
Syntax  vibration_response(
                            stiffness,
                            mass,
                            system type, 1 = mass,spring    2 = mass,spring,damper
                            damping coefficient,
                            initial displacement,
                            initial velocity,
                            )
'''


def mohr2d(sx, sy, txy,return_value = 'plot'):
    cen = (sx + sy) * .5
    rad = sqrt(((sx - sy) * .5) ** 2 + txy ** 2)
    s1 = round(cen + rad, ndigits=2)
    s2 = round(cen - rad, ndigits=2)
    s3 = round(rad, ndigits=2)
    t = np.arange(0, np.pi * 2.0, 0.01)
    x_c = cen + rad * np.cos(t)
    y_c = rad * np.sin(t)
    fig= plt.figure()
    # img = plt.imread("mohr.png")    # TODO improve bg image
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.plot(x_c, y_c, color='black')
    ax = plt.gca()
    ax.set_aspect('equal')  # need circle, not a ellipse
    plt.annotate('$\sigma_1=$' + str(s1), xy=(cen + rad, 0), xytext=(cen + rad / 2, rad / 2),
                 arrowprops=dict(facecolor='green', shrink=0.01)
                 )
    plt.annotate('$\sigma_2=$' + str(s2), xy=(cen - rad, 0), xytext=(cen - rad / 2, rad / 2),
                 arrowprops=dict(facecolor='red', shrink=0.01)
                 )
    plt.annotate('$\\tau_{max}=$' + str(s3), xy=(cen, rad), xytext=(cen / .75, rad / 1.4),
                 arrowprops=dict(facecolor='blue', shrink=0.01)
                 )
    plt.annotate('(0,0)', xy=(0, 0), xytext=(0, 0))
    plt.axis('off')
    # TODO annotate max shear
    # pylab.show()
    pylab.title('Mohr Circle for the requested 2D stress field')
    figfile = BytesIO()
    if return_value == 'value':
        return s1, s2, s3
    return return_img(figfile)


def mohr3d(sxx, syy, szz, sxy, sxz, syz):
    stress = np.array([[sxx, sxy, sxz],
                       [sxy, syy, syz],
                       [sxz, syz, szz]])
    eign = eig(stress)
    pstress = eign[0]
    pstress.sort()

    # define circles
    circ = np.zeros((3, 2), dtype=float)  # 3 circles in order center,radius
    circ[0][0] = .5 * (pstress[2] + pstress[0])
    circ[0][1] = .5 * (pstress[2] - pstress[0])
    circ[1][0] = .5 * (pstress[1] + pstress[0])
    circ[1][1] = .5 * (pstress[1] - pstress[0])
    circ[2][0] = .5 * (pstress[2] + pstress[1])
    circ[2][1] = .5 * (pstress[2] - pstress[1])
    s1 = round(circ[0][0] + circ[0][1], ndigits=2)
    s2 = round(circ[1][0] + circ[1][1], ndigits=2)
    s3 = round(circ[0][0] - circ[0][1], ndigits=2)
    rad = .10 * circ[0][1]

    # Plotting
    circle1 = pylab.Circle((circ[0][0], 0), radius=circ[0][1], color='red')
    circle2 = pylab.Circle((circ[1][0], 0), radius=circ[1][1], color='blue')
    circle3 = pylab.Circle((circ[2][0], 0), radius=circ[2][1], color='green')
    fig = plt.figure()
    ax = pylab.gca()
    pylab.title('Mohr Circle for the requested 3D stress field')
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.axis('off')
    plt.annotate('$\sigma_1=$' + str(s1), xy=(s1, 0), xytext=(s1, rad),
                 arrowprops=dict(facecolor='green', shrink=0.01)
                 )
    plt.annotate('$\sigma_2=$' + str(s2), xy=(s2, 0), xytext=(s2, rad),
                 arrowprops=dict(facecolor='red', shrink=0.01)
                 )
    plt.annotate('$\sigma_3=$' + str(s3), xy=(s3, 0), xytext=(s3, 1.5*rad),
                 arrowprops=dict(facecolor='blue', shrink=0.01)
                 )
    # TODO Annotate for Tau_max
    plt.axis('scaled')
    # pylab.show()
    figfile = BytesIO()
    return return_img(figfile)


def return_img(figfile):
    pylab.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    return figdata_png


if __name__ == '__main__':
    # vibration_response(12345, 45, 2, 4.56, 0.0, 1.0)
    mohr3d(1,2,3,4,5,6)
