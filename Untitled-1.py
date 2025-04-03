

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

def crear (final,rondas):    
    if len(rondas)>0:  
        for nombre in rondas[0]:                      #recorremos el diccionario para inicializar los valores de cada jugador
            final[nombre]={"kills":0,"assists":0,"deaths":0,"MVP":0,"puntos":0}


def imprimir (diccionario):         #funcion para imprimir el diccionario de manera ordenada
    print("jugador     kills   assists    deaths   MVP    puntos")
    print("========================================================")
    for h in diccionario:
        print(f" {h[0]}{(" ")* (6-len(h[0]))}       {h[1]['kills']}        {h[1]['assists']}         {h[1]['deaths']}       {h[1]["MVP"]}       {h[1]['puntos']}")
    print("========================================================")
    print("=========================================================")

def ordenarP(diccionario):         #funcion para ordenar el diccionario por puntos
    return sorted(diccionario.items(), key=lambda x: x[1]['puntos'], reverse=True)

def ordenarM(diccionario):         #funcion para ordenar el diccionario por MVP
    return sorted(diccionario.items(), key=lambda x: x[1]['MVP'], reverse=True)

def ordenarK(diccionario):         #funcion para ordenar el diccionario por kills
    return sorted(diccionario.items(), key=lambda x: x[1]['kills'], reverse=True)

def ordenarA(diccionario):         #funcion para ordenar el diccionario por assists
    return sorted(diccionario.items(), key=lambda x: x[1]['assists'], reverse=True)

def ordenarD(diccionario):         #funcion para ordenar el diccionario por deaths
    return sorted(diccionario.items(), key=lambda x: x[1]['deaths'], reverse=True)

def ordenarN(diccionario):         #funcion para ordenar el diccionario por nombre
    return sorted(diccionario.items(), key=lambda x: x[0], reverse=False)


final = {}      #diccionario para guardar los resultados finales
mvp = -1        #variable para guardar el MVP de la ronda
crear(final,rondas)         #llamamos a la funcion para crear el diccionario
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
        finalordenado = ordenarP(final)         #ordenamos el diccionario por puntos
    final[MVP]["MVP"] += 1          #despues de recorrer todos los jugadores sumamos 1 al MVP de la ronda
    finalordenado =ordenarP(final)         #agregamos el MVP al diccionario final
    mvp = -1               #reiniciamos el MVP para la siguiente ronda
    imprimir(finalordenado)       #llamamos a la funcion para imprimir el diccionario final

imprimir(finalordenado)         #imprimimos el diccionario final