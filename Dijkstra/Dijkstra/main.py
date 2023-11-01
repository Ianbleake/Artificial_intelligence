from Elements.graph import Graph
import argparse

Mexico_city_metro = Graph()
Mexico_city_metro_structure = {
    "Linea1": {
        "Stations": [
            "Observatorio",
            "Tacubaya",
            "Juanacatlan",
            "Chapultepec",
            "Sevilla",
            "Insurgentes",
            "Cuauhtemoc",
            "Balderas",
            "Salto_del_Agua",
            "Isabel_la_Catolica",
            "Pino_Suarez",
            "Merced",
            "Candelaria",
            "San_Lazaro",
            "Moctezuma",
            "Balbuena",
            "Blvd_Puerto_Aereo",
            "Gomez_Farias",
            "Zaragoza",
            "Pantitlan",
        ],
        "Connections": [
            ("Observatorio", "Tacubaya", 1262),
            ("Tacubaya", "Juanacatlan", 1158),
            ("Juanacatlan", "Chapultepec", 973),
            ("Chapultepec", "Sevilla", 501),
            ("Sevilla", "Insurgentes", 645),
            ("Insurgentes", "Cuauhtemoc", 793),
            ("Cuauhtemoc", "Balderas", 409),
            ("Balderas", "Salto_del_Agua", 458),
            ("Salto_del_Agua", "Isabel_la_Catolica", 445),
            ("Isabel_la_Catolica", "Pino_Suarez", 382),
            ("Pino_Suarez", "Merced", 745),
            ("Merced", "Candelaria", 698),
            ("Candelaria", "San_Lazaro", 866),
            ("San_Lazaro", "Moctezuma", 478),
            ("Moctezuma", "Balbuena", 703),
            ("Balbuena", "Blvd_Puerto_Aereo", 595),
            ("Blvd_Puerto_Aereo", "Gomez_Farias", 611),
            ("Gomez_Farias", "Zaragoza", 762),
            ("Zaragoza", "Pantitlan", 1,320),
        ],
    },
    "Linea2": {
        "Stations": [
            "Cuatro_Caminos",
            "Panteones",
            "Tacuba",
            "Cuitlahuac",
            "Popotla",
            "Colegio_Militar",
            "Normal",
            "San_Cosme",
            "Revolucion",
            "Hidalgo",
            "Bellas_Artes",
            "Allende",
            "Zocalo",
            "Pino_Suarez",
            "San_Antonio_Abada",
            "Chabacano",
            "Viaducto",
            "Xola",
            "Villa_de_Cortes",
            "Nativitas",
            "Portales",
            "Ermita",
            "General_Anaya",
            "Tasquena",
        ],
        "Connections": [
            ("Cuatro_Caminos", "Panteones", 1639),
            ("Panteones", "Tacuba", 1416),
            ("Tacuba", "Cuitlahuac", 637),
            ("Cuitlahuac", "Popotla", 620),
            ("Popotla", "Colegio_Militar", 462),
            ("Colegio_Militar", "Normal", 516),
            ("Normal", "San_Cosme", 657),
            ("San_Cosme", "Revolucion", 537),
            ("Revolucion", "Hidalgo", 587),
            ("Hidalgo", "Bellas_Artes", 447),
            ("Bellas_Artes", "Allende", 387),
            ("Allende", "Zocalo", 602),
            ("Zocalo", "Pino_Suarez", 745),
            ("Pino_Suarez", "San_Antonio_Abada", 817),
            ("San_Antonio_Abada", "Chabacano", 642),
            ("Chabacano", "Viaducto", 774),
            ("Viaducto", "Xola", 490),
            ("Xola", "Villa_de_Cortes", 698),
            ("Villa_de_Cortes", "Nativitas", 750),
            ("Nativitas", "Portales", 924),
            ("Portales", "Ermita", 748),
            ("Ermita", "General_Anaya", 838),
            ("General_Anaya", "Tasquena", 1330),
        ],
    },
    "Linea3": {
        "Stations": [
            "Indios_Verdes",
            "Deportivo_18_de_Marzo",
            "Potrero",
            "La_Raza",
            "Tlatelolco",
            "Guerrero",
            "Hidalgo",
            "Juarez",
            "Balderas",
            "Niños_Heroes",
            "Hospital_General",
            "Centro_Medico",
            "Etiopia",
            "Eugenia",
            "Division_del_Norte",
            "Zapata",
            "Coyoacan",
            "Viveros",
            "Miguel_Angel_de_Quevedo",
            "Copilco",
            "Universidad",
        ],
        "Connections": [
            ("Indios_Verdes", "Deportivo_18_de_Marzo", 1166),
            ("Deportivo_18_de_Marzo", "Potrero", 966),
            ("Potrero", "La_Raza", 1106),
            ("La_Raza", "Tlatelolco", 1445),
            ("Tlatelolco", "Guerrero", 1042),
            ("Guerrero", "Hidalgo", 702),
            ("Hidalgo", "Juarez", 251),
            ("Juarez", "Balderas", 659),
            ("Balderas", "Niños_Heroes", 665),
            ("Niños_Heroes", "Hospital_General", 559),
            ("Hospital_General", "Centro_Medico", 653),
            ("Centro_Medico", "Etiopia", 1119),
            ("Etiopia", "Eugenia", 950),
            ("Eugenia", "Division_del_Norte", 715),
            ("Division_del_Norte", "Zapata", 794),
            ("Zapata", "Coyoacan", 1153),
            ("Coyoacan", "Viveros", 908),
            ("Viveros", "Miguel_Angel_de_Quevedo", 824),
            ("Miguel_Angel_de_Quevedo", "Copilco", 1295),
            ("Copilco", "Universidad", 1306),
        ],
    },
    "Linea4": {
        "Stations": [
            "Martín_Carrera",
            "Talismán",
            "Bondojito",
            "Consulado",
            "Canal_del_Norte",
            "Morelos",
            "Candelaria",
            "Fray_Servando",
            "Jamaica",
            "Santa_Anita",
        ],
        "Connections": [
            ("Martín_Carrera", "Talismán", 1129),
            ("Talismán", "Bondojito", 959),
            ("Bondojito", "Consulado", 645),
            ("Consulado", "Canal_del_Norte", 884),
            ("Canal_del_Norte", "Morelos", 910),
            ("Morelos", "Candelaria", 1062),
            ("Candelaria", "Fray_Servando", 633),
            ("Fray_Servando", "Jamaica", 1033),
            ("Jamaica", "Santa_Anita", 758),
        ],
    },
    "Linea5": {
        "Stations": [
            "Pantitlan",
            "Hangares",
            "Terminal_Aerea",
            "Oceanía",
            "Aragón",
            "Eduardo_Molina",
            "Consulado",
            "Valle_Gómez",
            "Misterios",
            "La_Raza",
            "Autobuses_del_Norte",
            "Instituto_del_Petróleo",
            "Politécnico",
        ],
        "Connections": [
            ("Pantitlan", "Hangares", 1644),
            ("Hangares", "Terminal_Aerea", 1153),
            ("Terminal_Aerea", "Oceanía", 1174),
            ("Oceanía", "Aragón", 1219),
            ("Aragón", "Eduardo_Molina", 860),
            ("Eduardo_Molina", "Consulado", 815),
            ("Consulado", "Valle_Gómez", 679),
            ("Valle_Gómez", "Misterios", 969),
            ("Misterios", "La_Raza", 892),
            ("La_Raza", "Autobuses_del_Norte", 975),
            ("Autobuses_del_Norte", "Instituto_del_Petróleo", 1067),
            ("Instituto_del_Petróleo", "Politécnico", 1188),
        ],
    },
    "Linea6": {
        "Stations": [
            "El_Rosario",
            "Tezozomoc",
            "Azcapotzalco",
            "Ferreria",
            "Norte_45",
            "Vallejo",
            "Instituto_del_Petróleo",
            "Lindavista",
            "Deportivo_18_de_Marzo",
            "La_Villa-Basílica",
            "Martín_Carrera",
        ],
        "Connections": [
            ("El_Rosario", "Tezozomoc", 1257),
            ("Tezozomoc", "Azcapotzalco", 973),
            ("Azcapotzalco", "Ferreria", 1173),
            ("Ferreria", "Norte_45", 1072),
            ("Norte_45", "Vallejo", 660),
            ("Vallejo", "Instituto_del_Petróleo", 755),
            ("Instituto_del_Petróleo", "Lindavista", 1258),
            ("Lindavista", "Deportivo_18_de_Marzo", 1075),
            ("Deportivo_18_de_Marzo", "La_Villa-Basílica", 570),
            ("La_Villa-Basílica", "Martín_Carrera", 1141),
        ],
    },
    "Linea7": {
        "Stations": [
            "El_Rosario",
            "Aquiles_Serdan",
            "Camarones",
            "Refineria",
            "Tacuba",
            "San_Joaquin",
            "Polanco",
            "Auditorio",
            "Constituyentes",
            "Tacubaya",
            "San_Pedro_de_los_Pinos",
            "San_Antonio",
            "Mixcoac",
            "Barranca_del_Muerto",
        ],
        "Connections": [
            ("El_Rosario", "Aquiles_Serdan", 1615),
            ("Aquiles_Serdan", "Camarones", 1402),
            ("Camarones", "Refineria", 952),
            ("Refineria", "Tacuba", 1295),
            ("Tacuba", "San_Joaquin", 1433),
            ("San_Joaquin", "Polanco", 1163),
            ("Polanco", "Auditorio", 812),
            ("Auditorio", "Constituyentes", 1430),
            ("Constituyentes", "Tacubaya", 1005),
            ("Tacubaya", "San_Pedro_de_los_Pinos", 1084),
            ("San_Pedro_de_los_Pinos", "San_Antonio", 606),
            ("San_Antonio", "Mixcoac", 788),
            ("Mixcoac", "Barranca_del_Muerto", 1476),
        ],
    },
    "Linea8": {
        "Stations": [
            "Garibaldi",
            "Bellas_Artes",
            "San_Juan_de_Letran",
            "Salto_del_Agua",
            "Doctores",
            "Obrera",
            "Chabacano",
            "La_Viga",
            "Santa_Anita",
            "Coyuya",
            "Iztacalco",
            "Apatlaco",
            "Aculco",
            "Escuadron_201",
            "Atlalilco",
            "Iztapalapa",
            "Cerro_de_la_Estrella",
            "UAM-I",
            "Constitucion_de_1917",
        ],
        "Connections": [
            ("Garibaldi", "Bellas_Artes", 634),
            ("Bellas_Artes", "San_Juan_de_Letran", 456),
            ("San_Juan_de_Letran", "Salto_del_Agua", 292),
            ("Salto_del_Agua", "Doctores", 564),
            ("Doctores", "Obrera", 761),
            ("Obrera", "Chabacano", 1143),
            ("Chabacano", "La_Viga", 843),
            ("La_Viga", "Santa_Anita", 633),
            ("Santa_Anita", "Coyuya", 968),
            ("Coyuya", "Iztacalco", 993),
            ("Iztacalco", "Apatlaco", 910),
            ("Apatlaco", "Aculco", 534),
            ("Aculco", "Escuadron_201", 789),
            ("Escuadron_201", "Atlalilco", 1738),
            ("Atlalilco", "Iztapalapa", 732),
            ("Iztapalapa", "Cerro_de_la_Estrella", 717),
            ("Cerro_de_la_Estrella", "UAM-I", 1135),
            ("UAM-I", "Constitucion_de_1917", 1137),
        ],
    },
    "Linea9": {
        "Stations": [
            "Pantitlan",
            "Puebla",
            "Ciudad_Deportiva",
            "Velodromo",
            "Mixiuhca",
            "Jamaica",
            "Chabacano",
            "Lazaro_Cardenas",
            "Centro_Medico",
            "Chilpancingo",
            "Patriotismo",
            "Tacubaya",
        ],
        "Connections": [
            ("Pantitlan", "Puebla", 1380),
            ("Puebla", "Ciudad_Deportiva", 800),
            ("Ciudad_Deportiva", "Velodromo", 1110),
            ("Velodromo", "Mixiuhca", 821),
            ("Mixiuhca", "Jamaica", 942),
            ("Jamaica", "Chabacano", 1031),
            ("Chabacano", "Lazaro_Cardenas", 1000),
            ("Lazaro_Cardenas", "Centro_Medico", 1059),
            ("Centro_Medico", "Chilpancingo", 1152),
            ("Chilpancingo", "Patriotismo", 955),
            ("Patriotismo", "Tacubaya", 1133),
        ],
    },
    "LineaA": {
        "Stations": [
            "Pantitlan",
            "Agricola_Oriente",
            "Canal_de_San_Juan",
            "Tepalcates",
            "Guelatao",
            "Peñon_Viejo",
            "Acatitla",
            "Santa_Marta",
            "Los_Reyes",
            "La_Paz",
        ],
        "Connections": [
            ("Pantitlan", "Agricola_Oriente", 1409),
            ("Agricola_Oriente", "Canal_de_San_Juan", 1093),
            ("Canal_de_San_Juan", "Tepalcates", 1456),
            ("Tepalcates", "Guelatao", 1161),
            ("Guelatao", "Peñon_Viejo", 2206),
            ("Peñon_Viejo", "Acatitla", 1379),
            ("Acatitla", "Santa_Marta", 1100),
            ("Santa_Marta", "Los_Reyes", 1783),
            ("Los_Reyes", "La_Paz", 1956),
        ],
    },
    "LineaB": {
        "Stations": [
            "Buenavista",
            "Guerrero",
            "Garibaldi",
            "Lagunilla",
            "Tepito",
            "Morelos",
            "San_Lazaro",
            "Flores_Magon",
            "Romero_Rubio",
            "Oceanía",
            "Deportivo_Oceanía",
            "Bosque_de_Aragón",
            "Villa_de_Aragón",
            "Nezahualcoyotl",
            "Impulsora",
            "Rio_de_los_Remidios",
            "Muzquiz",
            "Ecatepec",
            "Olimpica",
            "Plaza_Aragón",
            "Ciudad_Azteca",
        ],
        "Connections": [
            ("Buenavista", "Guerrero", 521),
            ("Guerrero", "Garibaldi", 757),
            ("Garibaldi", "Lagunilla", 474),
            ("Lagunilla", "Tepito", 611),
            ("Tepito", "Morelos", 498),
            ("Morelos", "San_Lazaro", 1296),
            ("San_Lazaro", "Flores_Magon", 907),
            ("Flores_Magon", "Romero_Rubio", 908),
            ("Romero_Rubio", "Oceanía", 809),
            ("Oceanía", "Deportivo_Oceanía", 863),
            ("Deportivo_Oceanía", "Bosque_de_Aragón", 1165),
            ("Bosque_de_Aragón", "Villa_de_Aragón", 784),
            ("Villa_de_Aragón", "Nezahualcoyotl", 1335),
            ("Nezahualcoyotl", "Impulsora", 1393),
            ("Impulsora", "Rio_de_los_Remidios", 436),
            ("Rio_de_los_Remidios", "Muzquiz", 1155),
            ("Muzquiz", "Ecatepec", 1485),
            ("Ecatepec", "Olimpica", 596),
            ("Olimpica", "Plaza_Aragón", 709),
            ("Plaza_Aragón", "Ciudad_Azteca", 574),
        ],
    },
    "Linea12": {
        "Stations": [
            "Mixcoac",
            "Insurgentes_Sur",
            "20_de_Noviembre",
            "Zapata",
            "Parque_de_los_Venados",
            "Eje_Central",
            "Ermita",
            "Mexicaltzingo",
            "Atlalilco",
            "Culhuacán",
            "San_Andrés_Tomatlán",
            "Lomas_Estrella",
            "Calle_11",
            "Periférico_Oriente",
            "Tezonco",
            "Olivos",
            "Nopalera",
            "Zapotitlán",
            "Tlaltenco",
            "Tláhuac",
        ],
        "Connections": [
            ("Mixcoac", "Insurgentes_Sur", 651),
            ("Insurgentes_Sur", "20_de_Noviembre", 725),
            ("20_de_Noviembre", "Zapata", 450),
            ("Zapata", "Parque_de_los_Venados", 1280),
            ("Parque_de_los_Venados", "Eje_Central", 1280),
            ("Eje_Central", "Ermita", 895),
            ("Ermita", "Mexicaltzingo", 1805),
            ("Mexicaltzingo", "Atlalilco", 1922),
            ("Atlalilco", "Culhuacán", 1671),
            ("Culhuacán", "San_Andrés_Tomatlán", 990),
            ("San_Andrés_Tomatlán", "Lomas_Estrella", 1060),
            ("Lomas_Estrella", "Calle_11", 906),
            ("Calle_11", "Periférico_Oriente", 1111),
            ("Periférico_Oriente", "Tezonco", 1545),
            ("Tezonco", "Olivos", 490),
            ("Olivos", "Nopalera", 1360),
            ("Nopalera", "Zapotitlán", 1276),
            ("Zapotitlán", "Tlaltenco", 1115),
            ("Tlaltenco", "Tláhuac", 1298),
        ],
    },
}


def listar_estaciones():
    global Mexico_city_metro_structure
    all_stations = set()
    for line in Mexico_city_metro_structure.keys():
        for station in Mexico_city_metro_structure[line]["Stations"]:
            all_stations.add(station)
    return list(all_stations)


def main():
    global Mexico_city_metro
    parser = argparse.ArgumentParser(
        description="Selecciona dos estaciones de cualquier línea del metro."
    )
    parser.add_argument("-e1", "--estacion1", type=str, help="Primera estación")
    parser.add_argument("-e2", "--estacion2", type=str, help="Segunda estación")
    # add show lines option
    parser.add_argument(
        "-li", "--lines", action="store_true", help="Muestra las líneas del metro"
    )
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 2.0")
    # add show stations option for a specific line
    parser.add_argument(
        "-s", "--stations", type=str, help="Muestra las estaciones de una línea"
    )

    args = parser.parse_args()

    if args.lines:
        print("Líneas del metro:")
        for line in Mexico_city_metro_structure.keys():
            print(line)
        return
    elif args.stations:
        print(f"Estaciones de la línea {args.stations}:")
        for station in Mexico_city_metro_structure[args.stations]["Stations"]:
            print(station)
        return

    if args.estacion1 in listar_estaciones() and args.estacion2 in listar_estaciones():
        print(f"El camino más optimo a seguir de {args.estacion1} a {args.estacion2} es:.")
        print(Mexico_city_metro.dijkstra(args.estacion1, args.estacion2))
    else:
        print(
            "Error: Una o ambas estaciones no existen en el metro o estan nombradas incorrectamente."
        )


if __name__ == "__main__":
    
    for line, data in Mexico_city_metro_structure.items():
        for station in data["Stations"]:
            Mexico_city_metro.add_node(station, line)
        for connection in data["Connections"]:
            Mexico_city_metro
            Mexico_city_metro.add_connection(
                connection[0], connection[1], connection[2]
            )
    main()
