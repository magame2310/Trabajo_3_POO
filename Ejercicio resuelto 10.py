numero_inscripcion = input('Ingrese el número de inscripción')
nombre_alumno = input('Ingrese el nombre del alumno')
patrimonio = float(input('Ingrese el patrimonio del alumno'))
estrato = int(input('Ingrese el estrato del alumno'))

matricula = 50000

if patrimonio > 2000000 and estrato > 3:
  matricula += 0.03 * patrimonio

print(f'El estudiante con número de inscripción {numero_inscripcion} y nombre {nombre_alumno} debe pagar {matricula}')