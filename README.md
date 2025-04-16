![Imagen de Fifura Geometrica](https://cdn-icons-png.flaticon.com/512/6412/6412478.png)
# Figuras Geométricas 

##  Propósito del repositorio

Este repositorio contiene una implementación en Python de clases que representan figuras geométricas como rectángulo, triángulo y círculo. Cada clase permite calcular el área de su figura respectiva utilizando herencia y clases abstractas. El objetivo es aplicar buenas prácticas de programación orientada a objetos y seguir las normas del estilo PEP8.

##  Cambios realizados

Se aplicaron las siguientes correcciones al código original para cumplir con la guía de estilo PEP8 y mejorar la calidad del código. A continuación se detallan los principales problemas encontrados por pylint y las soluciones aplicadas:

1. **Error: C0114: Missing module docstring**
   - **Descripción**: El módulo no tenía una descripción general (docstring).
   - **Corrección**: Se agregó un docstring al inicio del archivo para explicar el propósito general del código.

2. **Error: R0903: Too few public methods (1/2)**
   - **Descripción**: Varias clases (como FiguraGeometrica, Rectangulo, Triangulo, y Circulo ) solo contenían un método público (calcular_area).
   - **Corrección**: Aunque el código está basado en clases abstractas, se añadió un comentario explicativo sobre la naturaleza de las clases para aclarar que solo implementan un método público como parte de una interfaz.

3. **Error: W0107: Unnecessary pass statement (unnecessary-pass)**
   - **Descripción**: La clase FiguraGeometrica tenía un pass innecesario en su método abstracto.
   - **Corrección**: Se reemplazó el pass por raise NotImplementedError() para indicar de manera más explícita que el método debe ser implementado por las clases hijas.

4. **Error: C0305: Trailing newlines**
   - **Descripción**: Había líneas en blanco al final del archivo, lo que no era conforme con las normas PEP8.
   - **Corrección**: Se eliminó cualquier línea vacía adicional después del código para que el archivo termine de forma adecuada.

5. **Error: C0115: Missing class docstring**
   - **Descripción**: Las clases FiguraGeometrica, Rectangulo, Triangulo, y Circulo no tenían una descripción en forma de docstring.
   - **Corrección**: Se agregaron docstrings a cada clase para describir su propósito y funcionalidad, siguiendo las recomendaciones de PEP8.

##  Integrante

| Apellidos | Nombre     |
|-----|--------------------------|
| Javier Curi  | Dayana  |

