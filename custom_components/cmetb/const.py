"""Constants for CMTEB integration."""

DOMAIN = "cmteb"
NAME = "CMTEB Termoficare Bucuresti"
VERSION = "1.0.0"
ATTRIBUTION = "Date preluate de la CMTEB București"

# Configurare
CONF_SECTOR = "sector"
CONF_NUME_PUNCT = "nume_punct"

# Lista sectoarelor și punctelor termice (de completat cu date reale)
SECTORI_PUNCTE = {
    "sector_1": [
        "Aviației",
        "Dorobanți", 
        "Floreasca",
        "Primăverii",
        "Piața Romană"
    ],
    "sector_2": [
        "Pantelimon",
        "Colentina",
        "Obor",
        "Iancului",
        "Piața Sudului"
    ],
    "sector_3": [
        "Titan",
        "Dristor",
        "Vitan",
        "Timpuri Noi",
        "Balta Albă"
    ],
    "sector_4": [
        "Berceni",
        "Tineretului", 
        "Văcărești",
        "Piața Progresul",
        "Ștefan cel Mare"
    ],
    "sector_5": [
        "Rahova",
        "Ferentari",
        "Cotroceni",
        "13 Septembrie",
        "Piața Chirii"
    ],
    "sector_6": [
        "Militari",
        "Crângași",
        "Giulești",
        "Drumul Taberei",
        "Piața Armatei"
    ]
}

# Stări posibile
STATUS_OPRIT = "Oprire ACC/INC"
STATUS_NORMAL = "Functionare normala"
STATUS_DEFECT = "Deficienta ACC/INC"

# Tipuri afectate
AFECTAT_ACC = "Apa calda (ACC)"
AFECTAT_INC = "Caldura (INC)"
AFECTAT_AMANDOUA = "ACC si INC"

# Culori
COLOR_ROSU = "#FF0000"
COLOR_VERDE = "#00FF00" 
COLOR_GALBEN = "#FFFF00"
