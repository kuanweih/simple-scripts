import numpy as np


def get_ra_deg(hour, minute, second):
    return (hour + minute / 60. + second / 3600.) * 15.


def get_dec_deg(degree, minute, second):
    deg_mag = np.absolute(degree)
    deg_sign = degree / deg_mag
    return deg_sign * (deg_mag + minute / 60. + second / 3600.)


gc_xs = [get_ra_deg(2., 37., 2.1),
         get_ra_deg(2., 38., 40.1),
         get_ra_deg(2., 39., 52.5),
         get_ra_deg(2., 40., 9.),
         get_ra_deg(2., 42., 21.15)]

gc_ys = [get_dec_deg(-34., 11., 0.),
         get_dec_deg(-34., 48., 5.),
         get_dec_deg(-34., 16., 8.),
         get_dec_deg(-34., 32., 24.),
         get_dec_deg(-34., 6., 4.7)]

print(gc_xs)
print(gc_ys)
