# Tunable Loading Coil

Date: 2026-01-13

## Theory

- A loading coil adds inductive reactance to electrically lengthen short antennas.
- It raises radiation resistance and allows resonance on low bands.
- Coil Q and placement control loss and bandwidth.

## Design Calculations

- Determine antenna capacitive reactance at the target frequency.
- Choose L so X_L = |X_C| to resonate the system.
- Check current at the coil to size wire and spacing.

## EZNEC / NEC Modeling

- Place a series inductive load at the coil position in NEC.
- Sweep frequency to validate resonance and current distribution.

## Winding Tables

- Use Wheeler formula for the coil geometry.
- Create turns vs inductance tables for tap points.

## 3D Printed Parts

- Coil form, tap ladder, and weatherproof cover.
