def bisection(f, a, b, TOL=1e-5, N0=100):

    if f(a) * f(b) >= 0:
        raise ValueError("El método de bisección requiere que f(a) y f(b) tengan signos opuestos.")

    i = 1
    FA = f(a)

    while i <= N0:
        p = a + (b - a) / 2.0
        FP = f(p)
        if FP == 0 or (b - a) / 2 < TOL:
            return p, i  
        i += 1
        if FA * FP > 0:
            a = p
            FA = FP 
        else:
            b = p

    raise ValueError(f"El método fracasó después de {N0} iteraciones.")

def fixed_point_iteration(g, p0, TOL=1e-5, N0=100):

    i = 1  
    while i <= N0:  
        p = g(p0)  
        if abs(p - p0) < TOL:  
            return p, i  
        i += 1  
        p0 = p  

    raise ValueError(f"El método falló después de {N0} iteraciones.")

def derivative(f, TOL=1e-5):
    return lambda x: (f(x + TOL) - f(x - TOL)) / (2 * TOL)

def newton_method(f, p0, TOL=1e-5, N0=100, factor=1e-8):
  
    df = derivative(f, TOL)
    i = 1  

    while i <= N0:  
        f_val = f(p0)
        df_val = df(p0)
        threshold = factor * (1 + abs(p0))
        
        if abs(df_val) < threshold:
            raise ValueError("La derivada es demasiado pequeña en p0, no se puede aplicar el método de Newton.")
        
        p = p0 - f_val / df_val
        
        if abs(p - p0) < TOL:
            return p, i
        
        i += 1
        p0 = p

    raise ValueError(f"El método falló después de {N0} iteraciones.")

