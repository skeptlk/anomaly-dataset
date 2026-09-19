# anomaly-dataset DVC
Engine defect flight data dataset for anomaly detection

## Scheme: 

| Feature | Смысл |
|---|---|
| `aircraft_id` | Identifier of an aircraft |
| `engine_position` | 1 or 2 (left or right position) |
| `engine_id` | Id of enigne |
| `type` | Anomaly type `egt_indication` or `fan_vibration` |
| `flight_phase` | `TAKEOFF` or `CRUISE` |
| `flight_datetime` | Report recorded time |
| `failure_value` | only `1` for now |

## Usage: ...
