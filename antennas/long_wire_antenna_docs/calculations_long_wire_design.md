# Design Calculations for Long Wire Antenna

Date: 2026-01-12

- Define target band(s) and choose a practical wire length.
- Start length Lm = 150 / f(MHz) meters for a half-wave estimate.
- Apply velocity factor: L = Lm * VF (typical VF 0.95 for bare wire).
- For long wire, choose L = n * (lambda / 2) where n >= 1.
- Estimate feed impedance with modeling or published tables.
- Choose feed method: end-fed with transformer or balanced line.
- Select matching: 9:1 unun for random wire, 49:1 for EFHW.
- Avoid feeding at a current null for stable performance.
- Estimate counterpoise length at 0.05 to 0.25 lambda.
- Check mechanical sag and tension for the chosen span.
