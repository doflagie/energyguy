# Remote Element Switching Systems

Date: 2026-01-13

## Theory

- Relays or PIN diodes switch antenna segments, traps, or matching networks.
- Control lines must be RF-isolated to avoid coupling and noise.
- Contact resistance and isolation drive loss and power limits.

## Design Calculations

- Size relays for RF current and voltage at the feed point.
- Compute control line filtering to block RF.

## EZNEC / NEC Modeling

- Create separate NEC models for each switch state.
- Replace inactive elements with open circuits or loads.

## Winding Tables

- Not coil-based; use relay datasheets and wiring lengths.

## 3D Printed Parts

- Relay box, gasketed lid, and cable glands.
