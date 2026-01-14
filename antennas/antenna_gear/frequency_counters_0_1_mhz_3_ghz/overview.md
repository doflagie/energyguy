# Frequency Counters (0.1 MHz - 3 GHz)

Date: 2026-01-13

## Theory

- Counters measure cycles during a gate interval.
- Prescalers extend the range into GHz bands.

## Design Calculations

- Resolution = 1 / gate_time.
- Prescaler divides frequency before counting.

## EZNEC / NEC Modeling

- Not modeled in NEC; connect via buffer to avoid loading.

## Winding Tables

- Not coil-based.

## 3D Printed Parts

- Display window, keypad mount, and shielded front end box.
