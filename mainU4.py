#Importacion de archivo con las clases a usar.
import EvaluaciónUnidad4 as E

#Instanciacion de objetos.
Camila = E.Persona('Camila','Morales', 30, 1.62, 'Preparatoria', 2263850139)
Diego = E.Persona('Diego', 'Méndez', 18, 1.60, 'Preparatoria', 2311322030)
Veronica = E.Administrador('Veronica','Gamino', 39, 1.48, 'Licenciatura', 2311013784, 'M&M Company', 3000)
Juan = E.Contador('Juan','Reyes',43,1.65,'Licenciatura',2311297057, 'M&M Company', 4000)
Manuel = E.JefeDeMarketing('Manuel','Torres',25,1.88,'Licenciatura',2314782905,'M&M Company',2800)
Cristhian = E.Gerente('Cristhian', 'Morales', 21,1.68, 'Licenciatura',2261111837,'M&M Company',6000)

print('\n--Clase persona--')
Diego.Presentarce()
Diego.Vestir('Pantalon negro','Playera Blanca','Gafas')
Diego.Comer('Hamburguesa','Jugo de naranja')
Diego.AccionAleatoria()
Diego.Dormir(6)

Camila.Presentarce()
Camila.Vestir('Vestido Rojo', 'Saco negro', 'Chalina')
Camila.Comer('Coctel de frutas','Frappe')
Camila.AccionAleatoria()
Camila.Dormir(9)