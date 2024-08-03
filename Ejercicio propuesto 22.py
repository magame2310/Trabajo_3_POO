nombre_empleado = input('Ingrese el nombre del empleado: ')
salario_basico_por_hora = float(input('Ingrese el salario básico por hora: '))
horas_trabajadas = float(input('Ingrese las horas trabajadas en el mes: '))

print('El nombre del empleado es: ', nombre_empleado)

salario_mensual = salario_basico_por_hora * horas_trabajadas

if salario_mensual > 450000:
  print('El salario mensual es: ', salario_mensual)