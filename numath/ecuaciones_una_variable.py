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

def _derivative(f, TOL=1e-5):
    return lambda x: (f(x + TOL) - f(x - TOL)) / (2 * TOL)

def newton_method(f, p0, TOL=1e-5, N0=100, factor=1e-8):
  
    df = _derivative(f, TOL)
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

def secant_method(f, p0, p1, TOL=1e-5, N0=100):
   
    i = 2 
    q0 = f(p0)
    q1 = f(p1)
    
    while i <= N0:
        if q1 - q0 == 0:
            raise ValueError("División por cero: f(p1) y f(p0) son iguales.")
        
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        if abs(p - p1) < TOL:
            return p, i
        i += 1
        p0, q0 = p1, q1
        p1 = p
        q1 = f(p1)
    
    raise ValueError(f"El método falló después de {N0} iteraciones.")

def false_position(f, p0, p1, TOL=1e-5, N0=100):
    
    if f(p0) * f(p1) >= 0:
        raise ValueError("Los puntos iniciales no encierran una raíz: f(p0) y f(p1) deben tener signos opuestos.")

    i = 2  
    q0 = f(p0)
    q1 = f(p1)
    
    while i <= N0:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        if abs(p - p1) < TOL:
            return p, i
        i += 1
        q = f(p)
        if q * q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q

    raise ValueError(f"El método falló después de {N0} iteraciones.")

def steffensen_method(g, p0, TOL=1e-5, N0=100):
    
    i = 1 
    while i <= N0:
        p1 = g(p0)    
        if abs(p1 - p0) < TOL:
            return p0, i  
        p2 = g(p1)      
        denominator = p2 - 2 * p1 + p0
        if denominator == 0:
            raise ValueError("Denominador cero en el cálculo de p; el método no puede continuar.")
       
        p = p0 - ((p1 - p0) ** 2) / denominator 
        if abs(p - p0) < TOL:  
            return p, i
        i += 1               
        p0 = p        

    raise ValueError(f"El método falló después de {N0} iteraciones.")
