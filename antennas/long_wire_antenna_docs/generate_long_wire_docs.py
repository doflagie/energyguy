import math
from datetime import date
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent


def pdf_escape(text: str) -> str:
    return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')


def make_pdf(path: Path, width: float, height: float, content: str) -> None:
    header = "%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
    objects = []
    objects.append("<< /Type /Catalog /Pages 2 0 R >>")
    objects.append("<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
    objects.append(
        "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {w} {h}] "
        "/Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>".format(
            w=width, h=height
        )
    )
    objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    objects.append(f"<< /Length {len(content.encode('utf-8'))} >>\nstream\n{content}\nendstream")

    offsets = [0]
    body = header
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(body))
        body += f"{i} 0 obj\n{obj}\nendobj\n"
    xref_start = len(body)
    body += "xref\n0 {count}\n".format(count=len(offsets))
    body += "0000000000 65535 f \n"
    for off in offsets[1:]:
        body += f"{off:010d} 00000 n \n"
    body += "trailer\n<< /Size {size} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".format(
        size=len(offsets), xref=xref_start
    )

    path.write_bytes(body.encode('utf-8'))


def text_cmd(x: float, y: float, size: float, text: str) -> str:
    return f"BT /F1 {size} Tf {x:.2f} {y:.2f} Td ({pdf_escape(text)}) Tj ET\n"


def make_text_pdf(path: Path, title: str, lines: list[str]):
    w, h = 595, 842
    x = 50
    y = h - 60
    content = ""
    content += text_cmd(x, y, 16, title)
    y -= 30
    content += text_cmd(x, y, 10, f"Date: {date.today().isoformat()}")
    y -= 24
    for line in lines:
        if y < 60:
            break
        content += text_cmd(x, y, 11, line)
        y -= 16
    make_pdf(path, w, h, content)


def main():
    docs = {
        "theory_long_wire_antenna.pdf": (
            "Theory of Long Wire Antennas",
            [
                "A long wire antenna is a straight conductor longer than about 1/2 wavelength.",
                "As length increases, current distribution forms multiple standing-wave lobes.",
                "The radiation pattern narrows in the plane of the wire with multiple main lobes.",
                "End effects raise the resonant length above the ideal free-space length.",
                "Height above ground and ground conductivity affect impedance and pattern.",
                "End-fed long wires usually present high feed impedance at the end.",
                "Feed impedance varies strongly with frequency and wire length.",
                "Counterpoise or earth connection is needed for end-fed systems.",
                "With balanced feed, the wire may be center-fed or off-center-fed.",
                "For portable HF, random-length wires are common with tuners.",
                "Antenna efficiency depends on conductor loss and ground loss.",
                "Modeling is useful because simple formulas are only approximate.",
            ],
        ),
        "calculations_long_wire_design.pdf": (
            "Design Calculations for Long Wire Antenna",
            [
                "Define target band(s) and choose a practical wire length.",
                "Start length Lm = 150 / f(MHz) meters for half-wave estimate.",
                "Apply velocity factor: L = Lm * VF (typical VF 0.95 for bare wire).",
                "For long wire, pick L = n * (lambda / 2) where n >= 1.",
                "Estimate feed impedance with modeling or tables for L/lambda.",
                "Choose feed method: end-fed with transformer or balanced line.",
                "Select matching: 9:1 unun for random wire, 49:1 for EFHW.",
                "Check current maxima to avoid feeding at a current null.",
                "Estimate required counterpoise length ~0.05 to 0.25 lambda.",
                "Verify mechanical sag and tension for the chosen span.",
            ],
        ),
        "eznec_nec_modeling.pdf": (
            "Creating EZNEC / NEC Model Files",
            [
                "Define geometry: wire endpoints, diameter, and segmentation count.",
                "Use at least 20 segments per half-wave; keep segment length <= 0.05 lambda.",
                "Specify ground type: free space, perfect ground, or real ground.",
                "Add excitation: voltage source at feed segment (end or center).",
                "Set frequency sweep and output requests (gain, impedance, current).",
                "Run the model and inspect current distribution for irregularities.",
                "Adjust segmentation if currents show sharp discontinuities.",
                "Save the file in .EZ or .NEC format with comments for revisions.",
            ],
        ),
        "winding_tables.pdf": (
            "Calculating Winding Tables",
            [
                "Winding tables are used for loading coils or transformer windings.",
                "Select target inductance L and core form dimensions.",
                "For air-core solenoid: L(uH) = (r^2 * N^2) / (9r + 10l).",
                "Solve for turns N and calculate turn spacing for uniform winding.",
                "If using ferrite, use AL value: L(nH) = AL * N^2.",
                "Create a table of N vs L for common tap points (e.g., 10, 20, 30 turns).",
                "Include wire gauge, diameter, and maximum current rating.",
                "Validate inductance with an LCR meter when possible.",
            ],
        ),
        "element_lengths.pdf": (
            "Calculating Exact Element Lengths",
            [
                "Compute wavelength: lambda(m) = 300 / f(MHz).",
                "Start with half-wave length: L0 = lambda / 2.",
                "Apply velocity factor (VF) and end effect: L = L0 * VF * K.",
                "Typical K ranges 0.95 to 0.98 depending on diameter and height.",
                "For long wires, choose L = n * (lambda/2) and adjust per model.",
                "Use modeling to refine length for the desired resonance or pattern.",
                "Trim in small steps and re-measure SWR to final value.",
            ],
        ),
        "feed_point_locations.pdf": (
            "Calculating Exact Feed Point Locations",
            [
                "End-fed long wires have high impedance; center feed is low impedance.",
                "For off-center feed, choose a ratio that yields 200-3000 ohms.",
                "Use current distribution: feed where current is not at a null.",
                "For L = 1/2 lambda, center feed is typical; for 1 lambda, avoid center.",
                "Model impedance vs position and choose a point for your transformer.",
                "Verify with VNA or tuner measurements in the final installation.",
            ],
        ),
        "matching_methods.pdf": (
            "Calculating Matching Methods",
            [
                "Measure or model feed impedance at the operating frequency.",
                "For end-fed random wire, start with 9:1 unun (3000 to 50 ohms).",
                "For EFHW, use 49:1 or 64:1 transformer depending on impedance.",
                "For balanced feed, use a 1:1 current balun and open-wire line.",
                "Tune residual reactance with an antenna tuner or L-network.",
                "Check transformer voltage/current ratings to prevent overheating.",
            ],
        ),
        "construction_methods.pdf": (
            "Construction Methods",
            [
                "Choose copper-clad steel or stranded copper wire for strength.",
                "Use UV-resistant insulators and rope for outdoor durability.",
                "Solder or crimp ring lugs to prevent wire fatigue at connections.",
                "Weatherproof the feed point with heat shrink and silicone sealant.",
                "Provide strain relief so the feed line does not carry mechanical load.",
            ],
        ),
        "aiming_methods.pdf": (
            "Aiming Methods",
            [
                "Long wires radiate strongest off the wire ends when length > 1 lambda.",
                "Orient the wire so the main lobes point toward the target area.",
                "Use modeling to find lobe angles at your operating frequency.",
                "For short wires (< 0.5 lambda), broadside radiation is dominant.",
                "Confirm direction with on-air reports or beacons.",
            ],
        ),
        "deployment_techniques.pdf": (
            "Deployment Techniques",
            [
                "Survey the site for clear spans, trees, and safe anchor points.",
                "Keep the wire away from power lines and public access areas.",
                "Use a throw line or mast to elevate the far end.",
                "Tension gently to reduce sag while avoiding overstress.",
                "Route feed line downward to reduce RF on the line.",
            ],
        ),
        "tuning_methods.pdf": (
            "Tuning Methods",
            [
                "Measure SWR and impedance with a VNA at the feed point.",
                "Trim the wire in small increments to move resonance upward.",
                "Add length or use a loading coil to move resonance downward.",
                "Adjust matching transformer taps or tuner settings as needed.",
                "Re-check after rain or temperature changes.",
            ],
        ),
        "orientation_techniques.pdf": (
            "Orientation Techniques",
            [
                "Place the wire as high as practical to reduce ground loss.",
                "Avoid routing parallel to metal structures that detune the antenna.",
                "Keep the feed line at right angles for several meters if possible.",
                "Use a consistent compass bearing for repeatable deployments.",
            ],
        ),
        "assembly_procedures.pdf": (
            "Assembly Procedures",
            [
                "Cut wire to calculated length and add extra for end terminations.",
                "Install end insulators and tie-off points with figure-eight knots.",
                "Attach feed point insulator and strain relief.",
                "Connect matching transformer or balun and verify continuity.",
                "Label the feed line and store the antenna coiled without kinks.",
            ],
        ),
    }

    for filename, (title, lines) in docs.items():
        make_text_pdf(OUT_DIR / filename, title, lines)


if __name__ == "__main__":
    main()
