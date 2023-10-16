import numpy
import scipy
import sympy

def grad2gradminsec(grados):
    grados_tmp = int(grados)
    minutos_flotante = (grados - grados_tmp) * 60
    minutos = int(minutos_flotante)
    segundos = (minutos_flotante - minutos) * 60
    return grados_tmp, minutos, segundos
def calc_grad_angle_np(u, v):
    norma_u = numpy.linalg.norm(u)
    norma_v = numpy.linalg.norm(v)
    coseno = (u @ v) / (norma_u * norma_v)
    alpha = numpy.rad2deg(numpy.arccos(coseno))
    return alpha

def calc_rad_angle_np(u, v):
    norma_u = numpy.linalg.norm(u)
    norma_v = numpy.linalg.norm(v)
    coseno = (u @ v) / (norma_u * norma_v)
    alpha = numpy.arccos(coseno)
    return alpha

def calc_base_ortonormal_np(A, v):
    bon = scipy.linalg.null_space(A)
    u1 = bon[:, 0]
    u2 = bon[:, 1]
    P1 = (v @ u1) * u1
    P2 = (v @ u2) * u2
    P = P1 + P2
    return P

def calc_grad_angle_sp(u, v):
    norma_u = sympy.sqrt(u.dot(u))
    norma_v = sympy.sqrt(v.dot(v))
    coseno = u.dot(v) / (norma_u * norma_v)
    alpha = sympy.acos(coseno)
    alpha_deg = sympy.deg(alpha)
    return alpha_deg

def calc_rad_angle_sp(u, v):
    norma_u = sympy.sqrt(u.dot(u))
    norma_v = sympy.sqrt(v.dot(v))
    coseno = u.dot(v) / (norma_u * norma_v)
    alpha = sympy.acos(coseno)
    return alpha

def calc_base_ortonormal_sp(A, v):
    bon = sympy.nullspace(A)
    u1 = bon[0].normalized()
    u2 = bon[1].normalized()
    P1 = (v.dot(u1)) * u1
    P2 = (v.dot(u2)) * u2
    P = P1 + P2
    return P
