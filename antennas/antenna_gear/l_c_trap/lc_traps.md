# L/C Traps for Antennas

Date: 2026-01-13

## Theory

L/C traps are resonant circuits (inductor + capacitor) inserted in-line with an antenna element. At their resonant frequency, the trap presents a high impedance and effectively isolates the outer portion of the element. Below resonance, the trap behaves inductively and allows the element to act electrically longer. Above resonance, the trap behaves capacitively and the element can function as a shorter section.

Key ideas:
- At resonance: high impedance, current is reduced past the trap.
- Below resonance: inductive, adds electrical length.
- Above resonance: capacitive, reduces electrical length.
- Trap losses (coil resistance, dielectric loss) reduce efficiency, so Q matters.

## Design Calculations

Resonant frequency:
- f = 1 / (2 * pi * sqrt(L * C))

Given target frequency f and chosen capacitor C:
- L = 1 / ((2 * pi * f)^2 * C)

Given target f and chosen inductance L:
- C = 1 / ((2 * pi * f)^2 * L)

Trap impedance at resonance is limited by Q:
- Q = (2 * pi * f * L) / R
- Z_trap_approx = Q * (2 * pi * f * L)

Choose a capacitor with low ESR and adequate voltage rating. Coil wire size and spacing impact loss and power handling.

## EZNEC / NEC Modeling

Basic approach:
- Model a segmented antenna element with a series RLC load (trap) at the trap position.
- Use a series load with L and C values.
- If using NEC-2, include a small series resistance to represent coil losses.

Typical steps:
1) Define the antenna wire geometry (endpoints, diameter, height).
2) Choose a segment at the trap location.
3) Apply a series RLC load to that segment.
4) Sweep frequency to verify trap resonance and current distribution.
5) Tune L or C for the target resonance in the model.

## Winding Tables

Wheeler single-layer air-core solenoid (inches):
- L(uH) = (r^2 * N^2) / (9r + 10l)

Where:
- r = coil radius (in)
- l = coil length (in)
- N = turns

Steps to build a winding table:
1) Decide coil form diameter and length.
2) Pick wire diameter and turn spacing.
3) Compute L for each turn count N.
4) Build a table of N vs L for tap points.

Ferrite core (AL method):
- L(nH) = AL * N^2
- N = sqrt(L(nH) / AL)

Use measured AL where possible.

## 3D Printed Parts

OpenSCAD parts provided:
- Coil form with flanges and vent holes.
- End cap with screw holes for enclosure assembly.
- Compact trap enclosure sized for 200x200x200 build volume.

Files:
- parts_lc_trap.scad
