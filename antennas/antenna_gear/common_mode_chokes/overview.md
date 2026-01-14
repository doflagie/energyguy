# Common-Mode Chokes

Date: 2026-01-13

## Theory

- Common-mode chokes block RF on the outside of coax shield.
- High impedance across the band reduces RFI and pattern distortion.

## Design Calculations

- Target choking impedance of 1k to 5k ohms at the band center.
- Z = 2 * pi * f * L; choose turns and core mix to reach Z.

## EZNEC / NEC Modeling

- Model as a series impedance in the shield path.
- Evaluate antenna current with and without the choke.

## Winding Tables

- Use AL to compute turns for a target L.
- Document turns vs impedance across the band.

## 3D Printed Parts

- Core clamp, wire guides, and weatherproof housing.
