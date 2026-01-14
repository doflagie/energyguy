# Creating EZNEC / NEC Model Files

Date: 2026-01-12

- Define geometry: wire endpoints, diameter, and segmentation count.
- Use at least 20 segments per half-wave; keep segment length <= 0.05 lambda.
- Specify ground type: free space, perfect ground, or real ground.
- Add excitation: voltage source at the feed segment (end or center).
- Set frequency sweep and output requests (gain, impedance, current).
- Run the model and inspect current distribution for anomalies.
- Adjust segmentation if currents show sharp discontinuities.
- Save the file in .EZ or .NEC format with comments for revisions.
