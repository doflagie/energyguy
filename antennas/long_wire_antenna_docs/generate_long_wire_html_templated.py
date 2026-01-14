from datetime import date
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent

SITE_TITLE = "EnergyGuy LLC"
TAGLINE = "Amateur Radio • Electronics • Engineering"
CSS_PATH = "../HTML/css/style.css"
HOME_PATH = "../HTML/index.html"

DOCS = {
    "theory_long_wire_antenna.html": (
        "Theory of Long Wire Antennas",
        [
            "A long wire antenna is a straight conductor longer than about half a wavelength.",
            "As length increases, the current distribution forms multiple standing-wave lobes.",
            "The radiation pattern narrows in the plane of the wire and develops multiple main lobes.",
            "End effects increase the physical length compared to ideal free-space calculations.",
            "Height above ground and soil conductivity strongly affect impedance and pattern.",
            "End-fed long wires typically present high feed impedance at the end.",
            "Feed impedance varies substantially with frequency and wire length.",
            "Counterpoise or earth connection is required for end-fed systems.",
            "Balanced feed can be used with center-fed or off-center-fed long wires.",
            "For portable HF, random-length wires are common with tuners.",
            "Efficiency is driven by conductor loss and ground loss.",
            "Modeling is recommended because formulas are approximate.",
        ],
    ),
    "calculations_long_wire_design.html": (
        "Design Calculations for Long Wire Antenna",
        [
            "Define target band(s) and choose a practical wire length.",
            "Start length Lm = 150 / f(MHz) meters for a half-wave estimate.",
            "Apply velocity factor: L = Lm * VF (typical VF 0.95 for bare wire).",
            "For long wire, choose L = n * (lambda / 2) where n >= 1.",
            "Estimate feed impedance with modeling or published tables.",
            "Choose feed method: end-fed with transformer or balanced line.",
            "Select matching: 9:1 unun for random wire, 49:1 for EFHW.",
            "Avoid feeding at a current null for stable performance.",
            "Estimate counterpoise length at 0.05 to 0.25 lambda.",
            "Check mechanical sag and tension for the chosen span.",
        ],
    ),
    "eznec_nec_modeling.html": (
        "Creating EZNEC / NEC Model Files",
        [
            "Define geometry: wire endpoints, diameter, and segmentation count.",
            "Use at least 20 segments per half-wave; keep segment length <= 0.05 lambda.",
            "Specify ground type: free space, perfect ground, or real ground.",
            "Add excitation: voltage source at the feed segment (end or center).",
            "Set frequency sweep and output requests (gain, impedance, current).",
            "Run the model and inspect current distribution for anomalies.",
            "Adjust segmentation if currents show sharp discontinuities.",
            "Save the file in .EZ or .NEC format with comments for revisions.",
        ],
    ),
    "winding_tables.html": (
        "Calculating Winding Tables",
        [
            "Winding tables are used for loading coils or transformer windings.",
            "Select target inductance L and coil form dimensions.",
            "For air-core solenoid: L(uH) = (r^2 * N^2) / (9r + 10l).",
            "Solve for turns N and calculate turn spacing for uniform winding.",
            "For ferrite cores, use AL: L(nH) = AL * N^2.",
            "Create a table of N vs L for common tap points.",
            "Include wire gauge, diameter, and maximum current rating.",
            "Validate inductance with an LCR meter when possible.",
        ],
    ),
    "element_lengths.html": (
        "Calculating Exact Element Lengths",
        [
            "Compute wavelength: lambda(m) = 300 / f(MHz).",
            "Start with half-wave length: L0 = lambda / 2.",
            "Apply velocity factor (VF) and end effect: L = L0 * VF * K.",
            "Typical K ranges 0.95 to 0.98 depending on diameter and height.",
            "For long wires, choose L = n * (lambda/2) and refine by model.",
            "Trim in small steps and re-measure SWR to final value.",
        ],
    ),
    "feed_point_locations.html": (
        "Calculating Exact Feed Point Locations",
        [
            "End-fed long wires have high impedance; center feed is low impedance.",
            "For off-center feed, choose a ratio that yields 200 to 3000 ohms.",
            "Use current distribution: feed where current is not at a null.",
            "For L = 1/2 lambda, center feed is typical; for 1 lambda, avoid center.",
            "Model impedance vs position and choose a point for your transformer.",
            "Verify with VNA or tuner measurements in the final installation.",
        ],
    ),
    "matching_methods.html": (
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
    "construction_methods.html": (
        "Construction Methods",
        [
            "Choose copper-clad steel or stranded copper wire for strength.",
            "Use UV-resistant insulators and rope for outdoor durability.",
            "Solder or crimp ring lugs to prevent wire fatigue at connections.",
            "Weatherproof the feed point with heat shrink and silicone sealant.",
            "Provide strain relief so the feed line does not carry mechanical load.",
        ],
    ),
    "aiming_methods.html": (
        "Aiming Methods",
        [
            "Long wires radiate strongest off the wire ends when length > 1 lambda.",
            "Orient the wire so the main lobes point toward the target area.",
            "Use modeling to find lobe angles at your operating frequency.",
            "For short wires (< 0.5 lambda), broadside radiation is dominant.",
            "Confirm direction with on-air reports or beacons.",
        ],
    ),
    "deployment_techniques.html": (
        "Deployment Techniques",
        [
            "Survey the site for clear spans, trees, and safe anchor points.",
            "Keep the wire away from power lines and public access areas.",
            "Use a throw line or mast to elevate the far end.",
            "Tension gently to reduce sag while avoiding overstress.",
            "Route feed line downward to reduce RF on the line.",
        ],
    ),
    "tuning_methods.html": (
        "Tuning Methods",
        [
            "Measure SWR and impedance with a VNA at the feed point.",
            "Trim the wire in small increments to move resonance upward.",
            "Add length or use a loading coil to move resonance downward.",
            "Adjust matching transformer taps or tuner settings as needed.",
            "Re-check after rain or temperature changes.",
        ],
    ),
    "orientation_techniques.html": (
        "Orientation Techniques",
        [
            "Place the wire as high as practical to reduce ground loss.",
            "Avoid routing parallel to metal structures that detune the antenna.",
            "Keep the feed line at right angles for several meters if possible.",
            "Use a consistent compass bearing for repeatable deployments.",
        ],
    ),
    "assembly_procedures.html": (
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

NAV_ITEMS = [
    ("Long Wire Docs Index", "index.html"),
    ("Theory", "theory_long_wire_antenna.html"),
    ("Design Calculations", "calculations_long_wire_design.html"),
    ("EZNEC / NEC Modeling", "eznec_nec_modeling.html"),
    ("Winding Tables", "winding_tables.html"),
    ("Element Lengths", "element_lengths.html"),
    ("Feed Point Locations", "feed_point_locations.html"),
    ("Matching Methods", "matching_methods.html"),
    ("Construction Methods", "construction_methods.html"),
    ("Aiming Methods", "aiming_methods.html"),
    ("Deployment Techniques", "deployment_techniques.html"),
    ("Tuning Methods", "tuning_methods.html"),
    ("Orientation Techniques", "orientation_techniques.html"),
    ("Assembly Procedures", "assembly_procedures.html"),
]


def render_nav() -> str:
    items = "\n".join(f"                    <li><a href=\"{href}\">{label}</a></li>" for label, href in NAV_ITEMS)
    return f"""
            <nav>
                <h3>Main Navigation</h3>
                <ul>
                    <li><a href=\"{HOME_PATH}\">Home</a></li>
                </ul>

                <h3>Long Wire Documents</h3>
                <ul>
{items}
                </ul>
            </nav>
"""


def render_page(title: str, body_list: list[str]) -> str:
    items = "\n".join(f"                    <li>{line}</li>" for line in body_list)
    return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <meta name=\"description\" content=\"EnergyGuy LLC - Long Wire Antenna Documentation\">
    <meta name=\"keywords\" content=\"amateur radio, antenna, long wire, NEC, EZNEC, ham radio\">
    <meta name=\"author\" content=\"Mervyn Martin\">
    <title>{title}</title>
    <link rel=\"stylesheet\" href=\"{CSS_PATH}\">
</head>
<body>
    <div class=\"container\">
        <header>
            <div class=\"banner\">
                <div>
                    <h1>{SITE_TITLE}</h1>
                    <p class=\"tagline\">{TAGLINE}</p>
                </div>
            </div>
        </header>

        <div class=\"main-wrapper\">
{render_nav()}
            <main>
                <h1>{title}</h1>
                <p>Date: {date.today().isoformat()}</p>
                <ul>
{items}
                </ul>
            </main>
        </div>

        <footer>
            <div class=\"address-block\">
                <h3>EnergyGuy LLC</h3>
                <p>Mervyn Martin, Proprietor</p>
                <p>Merced, California 95340</p>
            </div>
        </footer>
    </div>
</body>
</html>
"""


def write_pages():
    for filename, (title, lines) in DOCS.items():
        (OUT_DIR / filename).write_text(render_page(title, lines))

    # Index page
    index_items = "\n".join(
        f"                    <li><a href=\"{href}\">{label}</a></li>" for label, href in NAV_ITEMS[1:]
    )
    index_html = render_page(
        "Long Wire Antenna Documents",
        ["Use the links below to open each long wire antenna guide."]
    )
    # Inject list of links into the index main content
    marker = "<ul>\n"
    if marker in index_html:
        parts = index_html.split(marker)
        index_html = parts[0] + marker + index_items + "\n                </ul>\n" + "\n".join(parts[1].split("</ul>", 1)[1:])
    (OUT_DIR / "index.html").write_text(index_html)


if __name__ == "__main__":
    write_pages()
