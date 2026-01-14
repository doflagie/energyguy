# Motorized Tuning Systems

Date: 2026-01-13

## Theory

- Motor drives variable L or C for remote tuning of antennas or tuners.
- Feedback sensors enable repeatable tuning positions.
- Mechanical backlash and travel limits affect precision.

## Design Calculations

- Compute gear ratio for desired tuning resolution.
- Estimate torque based on shaft friction and capacitor load.
- Select motor voltage and current for duty cycle.

## EZNEC / NEC Modeling

- NEC models the tuned L/C values rather than the motor mechanics.
- Create per-band NEC files for each tuned setting.

## Winding Tables

- If motor drives an inductor, use turns vs position tables.

## 3D Printed Parts

- Motor mount, coupler, limit switch brackets, and sealed housing.
