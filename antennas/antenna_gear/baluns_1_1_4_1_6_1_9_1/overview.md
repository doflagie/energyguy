# Baluns (1:1, 4:1, 6:1, 9:1)

Date: 2026-01-13

## Theory

- Baluns transform impedance and suppress common-mode currents.
- Current baluns prioritize isolation; voltage baluns prioritize ratio.
- Core mix and winding style set bandwidth and power handling.

## Design Calculations

- Impedance ratio = turns_ratio^2 for transformer baluns.
- Choking impedance target: 1k to 5k ohms across the band.

## EZNEC / NEC Modeling

- Model as transformer with series loss resistance.
- Add common-mode choke impedance at the feed point.

## Winding Tables

- Bifilar or trifilar turns are computed from desired L and AL.
- Build turns tables for each ratio and core size.

## 3D Printed Parts

- Core clamps, strain relief, wire guides, and enclosure.
