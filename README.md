# numath – Librería de Matemática Numérica en Python

**numath** es una librería en Python diseñada para resolver problemas clásicos de **matemática numérica**, mediante métodos clásicos como Newton, Simpson, Romberg, métodos de Newton-Cotes, bisección, Müller, entre muchos otros. Está orientada a estudiantes, docentes y profesionales que necesiten implementar métodos numéricos de forma rápida y confiable.  

> Esta librería es parte de un Trabajo de Fin de Grado (TFG) y ha sido desarrollada con un enfoque didáctico, modular y bien documentado.

---

## Características principales

- Implementación clara y estructurada de los principales métodos numéricos  
- Acepta funciones como cadenas (por ejemplo, `"x^2 + sin(x)"`)  
- Soporte para funciones multivariables en integración doble y triple  
- Compatible con Python 3.10+  
- Documentación y tests incluidos en el repositorio

---

## Contenido de la librería

### 📁 `numath/` – Código fuente

| Archivo | Descripción |
|--------|-------------|
| `transformacion.py` | Transforma cadenas con expresiones matemáticas en funciones Python evaluables. |
| `diferenciacion_numerica_e_integracion.py` | Métodos de derivación numérica e integración (Simpson, Romberg, Newton-Cotes, etc.). |
| `ecuaciones_una_variable.py` | Métodos para resolver ecuaciones no lineales (bisección, Newton, secante, Müller, etc.). |

### 📁 `test/` – Pruebas automatizadas

Contiene tests unitarios con `pytest` para validar el comportamiento de cada módulo.

### 📁 `documentation/` – Documentación técnica (en `.md`)

Explicación detallada de:
- La teoría detrás de cada método
- Cómo están implementados
- Casos de prueba validados

---

## Documentación completa

Toda la documentación detallada de los módulos y los tests se encuentra en la carpeta [`documentation/`](./documentation/).

---

## Tests

Puedes ejecutar las pruebas usando `pytest`:

```bash
pip install pytest
pytest 
```

---

## Instalación

Puedes instalar `numath` ejecutando el siguiente comando:

```bash
pip install numath
```

## Licencia

Este proyecto está bajo licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## Contribuir

Si quieres proponer mejoras, añadir métodos o ayudar a ampliar los tests, ¡bienvenido/a!
Puedes abrir un *Pull Request* o proponer ideas vía *Issues*.
