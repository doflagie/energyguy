# L/C Resonators

Date: 2026-01-13

## Theory

- Series or parallel LC circuits create a sharp resonance used for traps and tuned circuits.
- At resonance, series LC is low impedance; parallel LC is high impedance.
- Q is limited by coil resistance and capacitor ESR, which sets bandwidth and loss.

## Design Calculations

- Resonance: f = 1 / (2 * pi * sqrt(L * C)).
- Choose C first, then solve L for the target frequency.
- Estimate Q: Q = (2 * pi * f * L) / R.

## EZNEC / NEC Modeling

- Model as a series or parallel RLC load in NEC at the trap location.
- Include a small series R to represent loss.
- Sweep frequency to verify the impedance peak or notch.

## Winding Tables

- Use Wheeler or AL formulas to compute L vs turns.
- Build a turns table to hit the target L with known wire size and spacing.

## 3D Printed Parts

- Coil form, capacitor bracket, and insulated standoffs.
- Enclosure or shield can for higher Q and stability.
