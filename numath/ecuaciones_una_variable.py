def bisection(f, a, b, tol=1e-5, max_iter=100):
    
    # Verificar que hay un cambio de signo entre f(a) y f(b)
    if f(a) * f(b) >= 0:
        raise ValueError("El método de bisección requiere que f(a) y f(b) tengan signos opuestos.")
    
    # Iteración para refinar la raíz
    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0  # Calcula el punto medio
        fc = f(c)
        
        # Condición de parada: si f(c) es suficientemente cercano a cero o el intervalo es pequeño
        if abs(fc) < tol or (b - a) / 2 < tol:
            return c, i
        
        # Determinar en qué subintervalo se encuentra la raíz
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    
    # Retorna la última aproximación si se alcanza el número máximo de iteraciones
    return c, max_iter
