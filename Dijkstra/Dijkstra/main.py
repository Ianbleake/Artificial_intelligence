from Elements.graph import Graph
from Elements.node import Node

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
            ("Observatorio", "Tacubaya", 1),
            ("Tacubaya", "Juanacatlan", 1),
            ("Juanacatlan", "Chapultepec", 1),
            ("Chapultepec", "Sevilla", 1),
            ("Sevilla", "Insurgentes", 1),
            ("Insurgentes", "Cuauhtemoc", 1),
            ("Cuauhtemoc", "Balderas", 1),
            ("Balderas", "Salto_del_Agua", 1),
            ("Salto_del_Agua", "Isabel_la_Catolica", 1),
            ("Isabel_la_Catolica", "Pino_Suarez", 1),
            ("Pino_Suarez", "Merced", 1),
            ("Merced", "Candelaria", 1),
            ("Candelaria", "San_Lazaro", 1),
            ("San_Lazaro", "Moctezuma", 1),
            ("Moctezuma", "Balbuena", 1),
            ("Balbuena", "Blvd_Puerto_Aereo", 1),
            ("Blvd_Puerto_Aereo", "Gomez_Farias", 1),
            ("Gomez_Farias", "Zaragoza", 1),
            ("Zaragoza", "Pantitlan", 1),
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
            ("Cuatro_Caminos", "Panteones", 1),
            ("Panteones", "Tacuba", 1),
            ("Tacuba", "Cuitlahuac", 1),
            ("Cuitlahuac", "Popotla", 1),
            ("Popotla", "Colegio_Militar", 1),
            ("Colegio_Militar", "Normal", 1),
            ("Normal", "San_Cosme", 1),
            ("San_Cosme", "Revolucion", 1),
            ("Revolucion", "Hidalgo", 1),
            ("Hidalgo", "Bellas_Artes", 1),
            ("Bellas_Artes", "Allende", 1),
            ("Allende", "Zocalo", 1),
            ("Zocalo", "Pino_Suarez", 1),
            ("Pino_Suarez", "San_Antonio_Abada", 1),
            ("San_Antonio_Abada", "Chabacano", 1),
            ("Chabacano", "Viaducto", 1),
            ("Viaducto", "Xola", 1),
            ("Xola", "Villa_de_Cortes", 1),
            ("Villa_de_Cortes", "Nativitas", 1),
            ("Nativitas", "Portales", 1),
            ("Portales", "Ermita", 1),
            ("Ermita", "General_Anaya", 1),
            ("General_Anaya", "Tasquena", 1),
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
            ("Indios_Verdes", "Deportivo_18_de_Marzo", 1),
            ("Deportivo_18_de_Marzo", "Potrero", 1),
            ("Potrero", "La_Raza", 1),
            ("La_Raza", "Tlatelolco", 1),
            ("Tlatelolco", "Guerrero", 1),
            ("Guerrero", "Hidalgo", 1),
            ("Hidalgo", "Juarez", 1),
            ("Juarez", "Balderas", 1),
            ("Balderas", "Niños_Heroes", 1),
            ("Niños_Heroes", "Hospital_General", 1),
            ("Hospital_General", "Centro_Medico", 1),
            ("Centro_Medico", "Etiopia", 1),
            ("Etiopia", "Eugenia", 1),
            ("Eugenia", "Division_del_Norte", 1),
            ("Division_del_Norte", "Zapata", 1),
            ("Zapata", "Coyoacan", 1),
            ("Coyoacan", "Viveros", 1),
            ("Viveros", "Miguel_Angel_de_Quevedo", 1),
            ("Miguel_Angel_de_Quevedo", "Copilco", 1),
            ("Copilco", "Universidad", 1),
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
            ("Martín_Carrera", "Talismán", 1),
            ("Talismán", "Bondojito", 1),
            ("Bondojito", "Consulado", 1),
            ("Consulado", "Canal_del_Norte", 1),
            ("Canal_del_Norte", "Morelos", 1),
            ("Morelos", "Candelaria", 1),
            ("Candelaria", "Fray_Servando", 1),
            ("Fray_Servando", "Jamaica", 1),
            ("Jamaica", "Santa_Anita", 1),
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
            ("Pantitlan", "Hangares", 1),
            ("Hangares", "Terminal_Aerea", 1),
            ("Terminal_Aerea", "Oceanía", 1),
            ("Oceanía", "Aragón", 1),
            ("Aragón", "Eduardo_Molina", 1),
            ("Eduardo_Molina", "Consulado", 1),
            ("Consulado", "Valle_Gómez", 1),
            ("Valle_Gómez", "Misterios", 1),
            ("Misterios", "La_Raza", 1),
            ("La_Raza", "Autobuses_del_Norte", 1),
            ("Autobuses_del_Norte", "Instituto_del_Petróleo", 1),
            ("Instituto_del_Petróleo", "Politécnico", 1),
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
            ("El_Rosario", "Tezozomoc", 1),
            ("Tezozomoc", "Azcapotzalco", 1),
            ("Azcapotzalco", "Ferreria", 1),
            ("Ferreria", "Norte_45", 1),
            ("Norte_45", "Vallejo", 1),
            ("Vallejo", "Instituto_del_Petróleo", 1),
            ("Instituto_del_Petróleo", "Lindavista", 1),
            ("Lindavista", "Deportivo_18_de_Marzo", 1),
            ("Deportivo_18_de_Marzo", "La_Villa-Basílica", 1),
            ("La_Villa-Basílica", "Martín_Carrera", 1),
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
            ("El_Rosario", "Aquiles_Serdan", 1),
            ("Aquiles_Serdan", "Camarones", 1),
            ("Camarones", "Refineria", 1),
            ("Refineria", "Tacuba", 1),
            ("Tacuba", "San_Joaquin", 1),
            ("San_Joaquin", "Polanco", 1),
            ("Polanco", "Auditorio", 1),
            ("Auditorio", "Constituyentes", 1),
            ("Constituyentes", "Tacubaya", 1),
            ("Tacubaya", "San_Pedro_de_los_Pinos", 1),
            ("San_Pedro_de_los_Pinos", "San_Antonio", 1),
            ("San_Antonio", "Mixcoac", 1),
            ("Mixcoac", "Barranca_del_Muerto", 1),
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
            ("Garibaldi", "Bellas_Artes", 1),
            ("Bellas_Artes", "San_Juan_de_Letran", 1),
            ("San_Juan_de_Letran", "Salto_del_Agua", 1),
            ("Salto_del_Agua", "Doctores", 1),
            ("Doctores", "Obrera", 1),
            ("Obrera", "Chabacano", 1),
            ("Chabacano", "La_Viga", 1),
            ("La_Viga", "Santa_Anita", 1),
            ("Santa_Anita", "Coyuya", 1),
            ("Coyuya", "Iztacalco", 1),
            ("Iztacalco", "Apatlaco", 1),
            ("Apatlaco", "Aculco", 1),
            ("Aculco", "Escuadron_201", 1),
            ("Escuadron_201", "Atlalilco", 1),
            ("Atlalilco", "Iztapalapa", 1),
            ("Iztapalapa", "Cerro_de_la_Estrella", 1),
            ("Cerro_de_la_Estrella", "UAM-I", 1),
            ("UAM-I", "Constitucion_de_1917", 1),
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
            ("Pantitlan", "Puebla", 1),
            ("Puebla", "Ciudad_Deportiva", 1),
            ("Ciudad_Deportiva", "Velodromo", 1),
            ("Velodromo", "Mixiuhca", 1),
            ("Mixiuhca", "Jamaica", 1),
            ("Jamaica", "Chabacano", 1),
            ("Chabacano", "Lazaro_Cardenas", 1),
            ("Lazaro_Cardenas", "Centro_Medico", 1),
            ("Centro_Medico", "Chilpancingo", 1),
            ("Chilpancingo", "Patriotismo", 1),
            ("Patriotismo", "Tacubaya", 1),
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
            ("Pantitlan", "Agricola_Oriente", 1),
            ("Agricola_Oriente", "Canal_de_San_Juan", 1),
            ("Canal_de_San_Juan", "Tepalcates", 1),
            ("Tepalcates", "Guelatao", 1),
            ("Guelatao", "Peñon_Viejo", 1),
            ("Peñon_Viejo", "Acatitla", 1),
            ("Acatitla", "Santa_Marta", 1),
            ("Santa_Marta", "Los_Reyes", 1),
            ("Los_Reyes", "La_Paz", 1),
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
            ("Buenavista", "Guerrero", 1),
            ("Guerrero", "Garibaldi", 1),
            ("Garibaldi", "Lagunilla", 1),
            ("Lagunilla", "Tepito", 1),
            ("Tepito", "Morelos", 1),
            ("Morelos", "San_Lazaro", 1),
            ("San_Lazaro", "Flores_Magon", 1),
            ("Flores_Magon", "Romero_Rubio", 1),
            ("Romero_Rubio", "Oceanía", 1),
            ("Oceanía", "Deportivo_Oceanía", 1),
            ("Deportivo_Oceanía", "Bosque_de_Aragón", 1),
            ("Bosque_de_Aragón", "Villa_de_Aragón", 1),
            ("Villa_de_Aragón", "Nezahualcoyotl", 1),
            ("Nezahualcoyotl", "Impulsora", 1),
            ("Impulsora", "Rio_de_los_Remidios", 1),
            ("Rio_de_los_Remidios", "Muzquiz", 1),
            ("Muzquiz", "Ecatepec", 1),
            ("Ecatepec", "Olimpica", 1),
            ("Olimpica", "Plaza_Aragón", 1),
            ("Plaza_Aragón", "Ciudad_Azteca", 1),
            
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
            ("Mixcoac", "Insurgentes_Sur", 1),
            ("Insurgentes_Sur", "20_de_Noviembre", 1),
            ("20_de_Noviembre", "Zapata", 1),
            ("Zapata", "Parque_de_los_Venados", 1),
            ("Parque_de_los_Venados", "Eje_Central", 1),
            ("Eje_Central", "Ermita", 1),
            ("Ermita", "Mexicaltzingo", 1),
            ("Mexicaltzingo", "Atlalilco", 1),
            ("Atlalilco", "Culhuacán", 1),
            ("Culhuacán", "San_Andrés_Tomatlán", 1),
            ("San_Andrés_Tomatlán", "Lomas_Estrella", 1),
            ("Lomas_Estrella", "Calle_11", 1),
            ("Calle_11", "Periférico_Oriente", 1),
            ("Periférico_Oriente", "Tezonco", 1),
            ("Tezonco", "Olivos", 1),
            ("Olivos", "Nopalera", 1),
            ("Nopalera", "Zapotitlán", 1),
            ("Zapotitlán", "Tlaltenco", 1),
            ("Tlaltenco", "Tláhuac", 1),
        ],
    },
}

if __name__ == "__main__":
    Mexico_city_metro = Graph()

    for line, data in Mexico_city_metro_structure.items():
        for station in data["Stations"]:
            Mexico_city_metro.add_node(station, line)
        for connection in data["Connections"]:
            Mexico_city_metro
            Mexico_city_metro.add_connection(connection[0], connection[1], connection[2])

    print(Mexico_city_metro.dijkstra("Cuatro_Caminos", "San_cosme"))
