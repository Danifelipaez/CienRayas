"""
Configuración central para CiénaFish.
Almacena coordenadas, URLs de API y umbrales de condiciones meteorológicas.
"""

# Coordenadas de la Ciénaga Grande de Santa Marta (centroide del ecosistema)
CIÉNAGA_LAT = 10.8
CIÉNAGA_LON = -74.4

# API de Open-Meteo (sin autenticación requerida)
OPEN_METEO_BASE_URL = "https://api.open-meteo.com/v1/forecast"

# Umbrales para determinar condición de seguridad para pesca
# Verde: seguro salir a pescar
# Amarillo: precaución, condiciones moderadas
# Rojo: peligroso, no recomendado
VIENTO_AMARILLO_KMH = 20  # Límite inferior para condición amarilla
VIENTO_ROJO_KMH = 40      # Límite inferior para condición roja

PRECIP_AMARILLO_MM = 1    # Límite inferior para condición amarilla
PRECIP_ROJO_MM = 5        # Límite inferior para condición roja
