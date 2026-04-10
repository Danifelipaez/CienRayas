"""
API FastAPI mínima para CiénaFish.
Endpoint GET /bulletin que orquesta servicios de clima y boletines para pescadores artesanales.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.services.open_meteo import fetch_weather
from app.services.bulletin import generate_bulletin_message, determine_condition

# Crear instancia de la app FastAPI
app = FastAPI(
    title="CiénaFish API",
    description="Boletín meteorológico para pescadores artesanales de la Ciénaga Grande de Santa Marta",
    version="0.1.0"
)


@app.get("/bulletin")
def get_bulletin():
    """
    Endpoint para obtener boletín meteorológico personalizado.
    
    Retorna:
        {
            "condicion": "verde" | "amarillo" | "rojo",
            "mensaje": "Aviso en español costeño...",
            "datos": {
                "weathercode": int,
                "windspeed_10m": float,
                "precipitation": float,
                "temperature_2m": float
            }
        }
    """
    # Consultar clima actual de la Ciénaga Grande
    weather_data = fetch_weather()
    
    if weather_data is None:
        # Fallback: retornar error con valores seguros
        weather_data = {
            "weathercode": 0,
            "windspeed_10m": 0,
            "precipitation": 0,
            "temperature_2m": 25,
        }
    
    # Determinar condición de seguridad (verde/amarillo/rojo)
    condicion = determine_condition(
        weather_data["windspeed_10m"],
        weather_data["precipitation"]
    )
    
    # Generar mensaje personalizado
    mensaje = generate_bulletin_message(weather_data)
    
    # Retornar JSON estructurado
    return JSONResponse(
        content={
            "condicion": condicion,
            "mensaje": mensaje,
            "datos": weather_data
        },
        status_code=200
    )


@app.get("/health")
def health_check():
    """
    Endpoint de salud para verificar que la API está operativa.
    """
    return {"status": "ok", "service": "CiénaFish API"}


if __name__ == "__main__":
    # Para ejecución directa (aunque uvicorn es lo recomendado)
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
