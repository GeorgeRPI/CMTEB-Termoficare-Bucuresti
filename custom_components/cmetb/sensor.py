import requests
from bs4 import BeautifulSoup
import logging
from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN, CONF_SECTOR, CONF_NUME_PUNCT

_LOGGER = logging.getLogger(__name__)

class CmtebSensor(SensorEntity):
    """Representation of a CMTEB sensor."""

    def __init__(self, hass, config):
        self._hass = hass
        self._sector = config[CONF_SECTOR]
        self._nume_punct = config[CONF_NUME_PUNCT]
        self._state = None
        self._attributes = {}
        
        # Nume unic pentru sensor
        self._name = f"Termoficare {self._sector} - {self._nume_punct}"

    async def async_update(self):
        """Update sensor data."""
        try:
            # Folosește executor thread pentru requests sincrone
            date = await self._hass.async_add_executor_job(
                self._extrage_date_cmteb
            )
            
            self._state = date.get('stare', 'Necunoscut')
            self._attributes = {
                'sector': self._sector.replace('_', ' ').title(),
                'nume_punct': self._nume_punct,
                'afectat': date.get('afectat', 'Necunoscut'),
                'termen_finalizare': date.get('termen', 'Necunoscut'),
                'culoare': date.get('culoare', '#CCCCCC'),
                'ultima_actualizare': date.get('actualizare')
            }
            
        except Exception as e:
            _LOGGER.error("Eroare la extragerea datelor pentru %s: %s", self._name, e)
            self._state = "Eroare"
            self._attributes = {'eroare': str(e)}

    def _extrage_date_cmteb(self):
        """Extrage datele de pe site-ul CMTEB."""
        url = "https://www.cmteb.ro/harta_stare_sistem_termoficare_bucuresti.php"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # AICI implementezi logica reală de parsare
        # Folosește self._sector și self._nume_punct pentru a găsi datele corecte
        
        return self._cauta_date_dupa_sector_nume(soup, self._sector, self._nume_punct)

    def _cauta_date_dupa_sector_nume(self, soup, sector, nume_punct):
        """Caută datele pentru sector și nume punct specific."""
        # IMPLEMENTARE REALĂ: 
        # Această funcție trebuie să parseze HTML-ul și să găsească
        # datele pentru combinatia sector + nume_punct
        
        # Exemplu temporar:
        date_exemplu = {
            'stare': 'Functionare normala',
            'afectat': 'Nimic',
            'termen': None,
            'culoare': '#00FF00',
            'actualizare': '2024-01-01 12:00:00'
        }
        
        return date_exemplu

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    @property
    def icon(self):
        """Iconiță în funcție de stare."""
        if self._state == "Functionare normala":
            return "mdi:check-circle"
        elif "Deficienta" in str(self._state):
            return "mdi:alert-circle"
        elif "Oprire" in str(self._state):
            return "mdi:close-circle"
        else:
            return "mdi:thermometer"
