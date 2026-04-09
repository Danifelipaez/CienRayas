# CiénaFish 🐟

> Herramienta digital para pescadores artesanales de la Ciénaga Grande de Santa Marta, Colombia.

## ¿Qué es?

CiénaFish es una app web móvil que ayuda a los pescadores artesanales de la Ciénaga Grande a tomar decisiones de pesca más informadas y seguras. Integra datos satelitales abiertos para mostrar en tiempo real las condiciones ambientales del cuerpo de agua más grande de Colombia.

La información se presenta como:
- **Mapa de zonas** con semáforo (verde / amarillo / rojo) según condiciones del día
- **Pronóstico climático** con íconos grandes, sin terminología técnica
- **Boletín en lenguaje sencillo** adaptado al vocabulario territorial de los pescadores
- **Alerta de seguridad** cuando no es recomendable salir a pescar

El proyecto se construye con los pescadores, no para ellos.

## Fuentes de datos

| Fuente | Variable | Uso |
|---|---|---|
| NASA MODIS / VIIRS | Temperatura superficial del agua | Semáforo de zonas |
| Copernicus Marine Service | Concentración de clorofila-a | Indicador de biomasa |
| Open-Meteo API | Pronóstico climático | Alerta de seguridad |

## Stack técnico

- **Backend:** Python 3.11 + FastAPI
- **Frontend:** HTML / CSS / JS vanilla · Leaflet.js + GeoJSON
- **App:** Web móvil responsive, Android-first (URL, no APK)
- **Cache:** Último pronóstico disponible para uso offline básico

## Estructura del proyecto

```
cienafish/
├── backend/          # FastAPI · servicios satelitales · lógica semáforo
├── frontend/         # Mapa Leaflet · UI · cache offline
├── data/             # GeoJSON de zonas · fuentes documentadas
├── docs/             # Documento de problema · historias de usuario · decisiones
└── iot/              # Placeholder Fase 2+ (ESP32 · sensores en campo)
```

## Equipo

| Nombre | Rol |
|---|---|
| Daniel | Project Manager · Ing. Sistemas |
| Valentina | Desarrollo y datos · Ing. Sistemas |
| Diego | Análisis territorial · Ing. Civil |
| Soe | Investigación comunitaria · Historia |
| Luis | Vínculo comunitario · Etnoeducación |

## Estado actual

- [x] Fase 1 — Identificación del problema
- [ ] Fase 2 — Stack · repositorio · primeras integraciones
- [ ] Fase 3 — Prototipo funcional con validación comunitaria

## Contexto

Seminario Aluna IA 2025 · Profesor Ricardo Pupo · Universidad del Magdalena  
Horizonte: prototipo funcional en 4–6 semanas con validación real en campo.