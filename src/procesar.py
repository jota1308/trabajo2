from src import diccionario
def procesarpartida (partida):      #funcion que procesa cada ronda de la partida y devuelve la partida en fotmato lista de tuplas
    final = {}      #diccionario para guardar los resultados finales
    mvp = -1        #variable para guardar el MVP de la ronda
    diccionario.crear(final,partida)         #llamamos a la funcion para crear el diccionario
    ronda = 0
    for i in partida:               #recorremos las rondas
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
        diccionario.imprimir(finalordenado)    #imprmimos dos veces pq una es por ronda y la otra es el final
    print("Partida finalizada")
    diccionario.imprimir(finalordenado)         