"""
Generador de boletines meteorológicos personalizados para pescadores artesanales.
Convierte datos climáticos en avisos colociales en español costeño colombiano.
"""

from typing import Dict


def generate_bulletin_message(weather_data: Dict) -> str:
    """
    Genera un mensaje de boletín meteorológico personalizado basado en condiciones climáticas.
    
    Args:
        weather_data: Dict con keys: windspeed_10m (km/h), precipitation (mm), temperature_2m (°C), weathercode (int)
    
    Returns:
        String con máximo 2 oraciones en español costeño, sin términos técnicos.
    """
    windspeed = weather_data.get("windspeed_10m", 0)
    precipitation = weather_data.get("precipitation", 0)
    temperature = weather_data.get("temperature_2m", 25)
    
    # Determinar características del viento
    if windspeed < 10:
        viento_desc = "está manso"
        viento_eval = "bueno"
    elif windspeed < 20:
        viento_desc = "está moderao"
        viento_eval = "moderado"
    elif windspeed < 40:
        viento_desc = "está fuerte"
        viento_eval = "fuerte"
    else:
        viento_desc = "está muy fuerte"
        viento_eval = "muy fuerte"
    
    # Determinar lluvia
    lluvia_present = "hay lluvia" if precipitation >= 0.5 else "no hay lluvia"
    
    # Determinar seguridad general
    if windspeed < 20 and precipitation < 1:
        # Verde: seguro
        if temperature > 28:
            return f"Hoy el tiempo está tranquilo por la Ciénaga, pueden salir sin problema. " \
                   f"El viento {viento_desc} y {lluvia_present}, está un chin calentao pero es día pa' pescar."
        else:
            return f"Hoy el tiempo está tranquilo por la Ciénaga, pueden salir sin problema. " \
                   f"El viento {viento_desc} y {lluvia_present}."
    
    elif windspeed < 40 or precipitation < 5:
        # Amarillo: precaución
        if precipitation >= 1:
            return f"Cuidao hoy, hay riesgo con lluvia y el viento está apretao. " \
                   f"Si salen, vayan con ojo y preparen los trastos bien."
        else:
            return f"Cuidao hoy, el viento está {viento_eval}. " \
                   f"Si salen, vayan con cuidao y no se alejen mucho."
    
    else:
        # Rojo: peligroso
        return f"Hoy no es día, hermano. El viento fuerte y lluvia no dejan. " \
               f"Mejor esperen a que amainen las aguas."


def determine_condition(windspeed_kmh: float, precipitation_mm: float) -> str:
    """
    Determina la condición de seguridad basada en umbrales meteorológicos.
    
    Args:
        windspeed_kmh: Velocidad del viento en km/h
        precipitation_mm: Precipitación en mm
    
    Returns:
        "verde" (seguro), "amarillo" (precaución) o "rojo" (peligro)
    """
    # Usar umbrales del módulo config (inyectados por caller o aquí definidos)
    VIENTO_AMARILLO = 20
    VIENTO_ROJO = 40
    PRECIP_AMARILLO = 1
    PRECIP_ROJO = 5
    
    # Rojo: viento > 40 km/h o precipitación > 5 mm
    if windspeed_kmh > VIENTO_ROJO or precipitation_mm > PRECIP_ROJO:
        return "rojo"
    
    # Amarillo: viento 20-40 km/h o precipitación 1-5 mm
    if windspeed_kmh >= VIENTO_AMARILLO or precipitation_mm >= PRECIP_AMARILLO:
        return "amarillo"
    
    # Verde: viento < 20 km/h y precipitación < 1 mm
    return "verde"
