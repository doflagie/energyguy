# Automatic Direction Finding

Date: 2026-01-13

## Theory

- ADF uses loop or phased antennas to determine bearing via nulls or phase.
- A sense antenna resolves the 180-degree ambiguity.
- Signal strength and multipath dominate bearing accuracy.

## Design Calculations

- Loop area and turns set sensitivity and bandwidth.
- Phase error translates directly to bearing error.

## EZNEC / NEC Modeling

- Model loop + sense in NEC and compute pattern nulls.
- Add phasing line lengths to match the ADF hardware.

## Winding Tables

- Small loop turns can be calculated from target inductance and size.

## 3D Printed Parts

- Loop frame, rotation mount, and enclosure for phase circuitry.
