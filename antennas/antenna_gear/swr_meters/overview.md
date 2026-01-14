# SWR Meters

Date: 2026-01-13

## Theory

- SWR meters compare forward and reflected power.
- They infer mismatch from the ratio of samples.

## Design Calculations

- SWR = (1 + sqrt(Pr/Pf)) / (1 - sqrt(Pr/Pf)).
- Calibrate with a known 50-ohm load.

## EZNEC / NEC Modeling

- Not modeled in NEC; use NEC to predict expected SWR.

## Winding Tables

- Coupler transformer turns set the sample ratio.

## 3D Printed Parts

- Panel meter mount, switch cutout, and labeling plate.
