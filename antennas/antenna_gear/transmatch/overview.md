# Transmatch

Date: 2026-01-13

## Theory

- A transmatch is an impedance matching network (L, T, or Pi) between radio and antenna.
- It transforms complex impedances while controlling circulating currents.
- Component Q and layout strongly affect loss and power handling.

## Design Calculations

- Select a target match ratio and choose an L-network topology.
- Compute reactances for the chosen Q and load resistance.
- Convert reactances to L and C values at the operating frequency.

## EZNEC / NEC Modeling

- Model as series and shunt reactances at the feed point in NEC.
- Represent variable caps/inductors as tuned values per band.

## Winding Tables

- If using a roller inductor, map turns/position to inductance.
- Use measured inductance per turn to build the table.

## 3D Printed Parts

- Knobs, shaft couplers, insulated standoffs, and enclosure panels.
