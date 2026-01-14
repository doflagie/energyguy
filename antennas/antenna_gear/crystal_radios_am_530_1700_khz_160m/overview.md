# Crystal Radios (AM 530-1700 kHz, 160M)

Date: 2026-01-13

## Theory

- A tuned LC circuit selects the station; a diode detects audio.
- High-Q coils and low-loss caps improve selectivity.

## Design Calculations

- L and C set the tuning range: f = 1 / (2 * pi * sqrt(L * C)).
- Coil inductance determines band coverage.

## EZNEC / NEC Modeling

- Model loop or wire antenna in NEC for impedance estimates.

## Winding Tables

- Compute turns to hit the target L on a chosen coil form.

## 3D Printed Parts

- Coil form, tuning capacitor mount, and dial scale.
