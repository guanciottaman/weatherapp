from dataclasses import dataclass


@dataclass
class English:
    lang_code = 'en'
    title = 'Weather'
    search = 'Search'
    search_entry = 'Search for a city...'
    error = 'Error'
    error_message = 'City not found. \nTry again'


@dataclass
class Italian:
    lang_code = 'it'
    title = 'Meteo'
    search = 'Cerca'
    search_entry = 'Cerca una città...'
    error = 'Errore'
    error_message = 'Città non trovata. \nProva ancora'


@dataclass
class French:
    lang_code = 'fr'
    title = 'Météo'
    search = 'Recherche'
    search_entry = 'Recherche une ville...'
    error = 'Erreur'
    error_message = 'Ville introuvable. \nRéessayez'


@dataclass
class German:
    lang_code = 'de'
    title = 'Wettervorhersage'
    search = 'Suche'
    search_entry = 'Suche nach einer Stadt...'
    error = 'Fehler'
    error_message = 'Stadt nicht gefunden. \nVersuchen Sie es noch einmal'


@dataclass
class Spanish:
    lang_code = 'es'
    title = 'Pronóstico del tiempo'
    search = 'Busca'
    search_entry = 'Busca una ciudad'
    error = 'Error'
