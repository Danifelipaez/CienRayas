"""
Servicio de consulta a la API Open-Meteo para obtener datos meteorológicos.
Implementación minimalista sin autenticación, usa solo httpx como librería externa.
"""

from typing import Dict, Optional
import httpx

from ..core.config import CIÉNAGA_LAT, CIÉNAGA_LON, OPEN_METEO_BASE_URL


def fetch_weather() -> Optional[Dict]:
    """
    Consulta la API de Open-Meteo para las coordenadas de la Ciénaga Grande.
    
    Extrae variables requeridas del momento actual:
    - weathercode: Código WMO del tipo de clima
    - windspeed_10m: Velocidad del viento a 10m en km/h
    - precipitation: Precipitación en mm
    - temperature_2m: Temperatura a 2m en °C
    
    Returns:
        Dict con las 4 variables del clima, o None si la consulta falla.
        En caso de falla, retorna dict seguro (viento=0, lluvia=0) para evitar crashes.
    """
    try:
        # Parámetros de consulta a Open-Meteo v1/forecast
        params = {
            "latitude": CIÉNAGA_LAT,
            "longitude": CIÉNAGA_LON,
            "current": "temperature_2m,weathercode,windspeed_10m,precipitation",
            "timezone": "auto"  # UTC automático
        }
        
        # Realizar solicitud HTTP GET
        with httpx.Client() as client:
            response = client.get(OPEN_METEO_BASE_URL, params=params, timeout=10.0)
            response.raise_for_status()  # Lanzar excepción si status != 2xx
        
        data = response.json()
        
        # Extraer datos del bloque "current" (datos actuales)
        if "current" not in data:
            return _safe_weather_dict()
        
        current = data["current"]
        
        # Construir dict limpio con valores requeridos
        weather_dict = {
            "weathercode": current.get("weathercode", 0),
            "windspeed_10m": current.get("windspeed_10m", 0),
            "precipitation": current.get("precipitation", 0),
            "temperature_2m": current.get("temperature_2m", 25),
        }
        
        return weather_dict
    
    except httpx.RequestError as e:
        # Error de conexión, timeout, etc.
        print(f"Error conectando a Open-Meteo: {e}")
        return _safe_weather_dict()
    
    except (KeyError, ValueError) as e:
        # Error parseando JSON o accediendo a keys
        print(f"Error parseando respuesta de Open-Meteo: {e}")
        return _safe_weather_dict()
    
    except Exception as e:
        # Cualquier otro error inesperado
        print(f"Error inesperado en fetch_weather(): {e}")
        return _safe_weather_dict()


def _safe_weather_dict() -> Dict:
    """
    Retorna un dict meteorológico "seguro" con valores por defecto.
    Usado cuando la API falla o no está disponible.
    Valores conservadores: viento bajo, sin lluvia → condición "verde".
    """
    return {
        "weathercode": 0,
        "windspeed_10m": 0,
        "precipitation": 0,
        "temperature_2m": 25,
    }
