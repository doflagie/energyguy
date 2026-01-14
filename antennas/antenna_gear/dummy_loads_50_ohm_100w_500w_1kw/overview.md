# Dummy Loads (50 Ohm, 100W/500W/1kW)

Date: 2026-01-13

## Theory

- Dummy loads provide a non-radiating load for transmitter testing.
- Resistors convert RF power into heat.

## Design Calculations

- Power: P = V^2 / R and I = sqrt(P / R).
- Thermal design uses resistor rating and heat sink capacity.

## EZNEC / NEC Modeling

- Not modeled in NEC; treat as a 50-ohm termination.

## Winding Tables

- Not coil-based; use resistor networks and thermal calculations.

## 3D Printed Parts

- Heat sink, oil can, or forced-air enclosure mounts.
