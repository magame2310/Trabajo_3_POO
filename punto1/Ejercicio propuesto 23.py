a = float(input('Ingrese el valor de a'))
b = float(input('Ingrese el valor de b'))
c = float(input('Ingrese el valor de c'))

discriminante = b ** 2 - 4 * a * c

if discriminante < 0:
  print('La ecuación no tiene solución real')
else:
  x1 = (-b + (discriminante) ** (1/2)) / (2 * a)
  x2 = (-b - (discriminante) ** (1/2)) / (2 * a)

  print('El valor de x1 es: ', x1)
  print('El valor de x2 es: ', x2)