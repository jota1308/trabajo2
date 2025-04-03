from src import diccionario

rondas = [{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},         #rondas de la partida
'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
}]



final = {}      #diccionario para guardar los resultados finales
mvp = -1        #variable para guardar el MVP de la ronda
diccionario.crear(final,rondas)         #llamamos a la funcion para crear el diccionario
ronda = 0
for i in rondas:               #recorremos las rondas
    ronda += 1
    print("ronda nro: ",ronda)
    for j in i:               #recorremos los jugadores de la ronda
        puntos = i[j]["kills"] * 3 + i[j]["assists"] - i[j]["deaths"]          #calculamos los puntos de cada jugador
        if puntos > mvp:
            mvp = puntos          #guardamos el MVP de la ronda
            MVP = j
        final[j]["kills"] += i[j]["kills"]
        final[j]["assists"] += i[j]["assists"]                    #sumamos las estadisticas al jugador
        final[j]["deaths"] += i[j]["deaths"]
        final[j]["puntos"] += puntos
        finalordenado = diccionario.ordenarP(final)         #ordenamos el diccionario por puntos
    final[MVP]["MVP"] += 1          #despues de recorrer todos los jugadores sumamos 1 al MVP de la ronda
    finalordenado =diccionario.ordenarP(final)         #agregamos el MVP al diccionario final
    mvp = -1               #reiniciamos el MVP para la siguiente ronda
    diccionario.imprimir(finalordenado)       #llamamos a la funcion para imprimir el diccionario final

diccionario.imprimir(finalordenado)         #imprimimos el diccionario final