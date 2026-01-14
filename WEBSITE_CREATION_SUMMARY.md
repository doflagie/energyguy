# EnergyGuy LLC Website - Creation Summary
## January 8, 2026

**For:** Mervyn Martin - Paradise, CA
**Purpose:** Professional website for knowledge preservation and business presence
**Status:** Core structure complete, ready for content expansion

---

## What Was Created

### Core Website Files (5 files)

1. **index.html** - Homepage
   - EnergyGuy banner
   - Navigation sidebar
   - Project cards (6 featured projects)
   - About section
   - Address block footer
   - Low eye strain color scheme

2. **css/style.css** - Main stylesheet (9KB)
   - Professional layout with left navigation
   - Low eye strain colors (#f5f5f0 background, #333333 text, #4a7ba7 accents)
   - Responsive design (mobile-friendly)
   - Print styles included
   - Project card grid system
   - Table formatting
   - Code block styling

3. **about/bio.html** - Biography page
   - Military service (Navy CTM, 1983-2004)
   - Camp Fire 2018 experience
   - Stroke recovery journey
   - Current projects and goals
   - Technical skills inventory
   - Knowledge preservation mission

4. **about/contact.html** - Contact page
   - Email contact information
   - Physical address
   - GitHub links
   - Amateur radio status
   - Business inquiries section
   - Collaboration opportunities

5. **antennas/station_grounding.html** - Station grounding guide
   - Complete guide from station_grounding_plan.md
   - Star ground architecture diagram
   - Materials BOM with costs
   - Installation sequence (4 phases)
   - Paradise, CA specific considerations
   - Common mistakes to avoid
   - NEC code compliance

### Documentation

6. **README.md** - Website documentation
   - File structure overview
   - Design principles
   - Color palette documentation
   - Content sources
   - Hosting considerations (GoDaddy, GitHub Pages)
   - Maintenance checklist
   - Future enhancements roadmap

7. **WEBSITE_CREATION_SUMMARY.md** - This file
   - What was created
   - Next steps
   - Upload instructions

---

## Folder Structure Created

```
HTML/
├── index.html              ✓ Complete
├── css/
│   └── style.css           ✓ Complete
├── images/                 (empty, ready for PNGs)
├── about/
│   ├── bio.html            ✓ Complete
│   ├── contact.html        ✓ Complete
│   └── links.html          ✓ Placeholder created
├── antennas/
│   ├── station_grounding.html  ✓ Complete
│   ├── longwire.html       ✓ Placeholder created
│   ├── dipole.html         ✓ Placeholder created
│   └── loop.html           ✓ Placeholder created
├── electronics/
│   ├── filters.html        ✓ Placeholder created
│   ├── sdr_cluster.html    ✓ Placeholder created
│   └── faraday_cage.html   ✓ Placeholder created
├── projects/
│   ├── tinysa.html         ✓ Placeholder created
│   ├── nanovna.html        ✓ Placeholder created
│   ├── ebook2cw.html       ✓ Placeholder created
│   ├── telegraph.html      ✓ Placeholder created
│   ├── vibroplex.html      ✓ Placeholder created
│   ├── neveready.html      ✓ Placeholder created
│   ├── darkroom_safelight.html  ✓ Placeholder created
│   └── ferro_rod.html      ✓ Placeholder created
├── README.md               ✓ Complete
└── WEBSITE_CREATION_SUMMARY.md  ✓ Complete
```

---

## Design Features

### Banner (Top)
- Gradient blue background (#4a7ba7 to #2c5f8d)
- **ENERGYGUY LLC** title (large, bold, white text)
- Tagline: "Amateur Radio • Electronics • Engineering"
- Full-width, professional appearance

### Navigation (Left Sidebar)
- 250px wide, tan background (#e8e8e0)
- Hierarchical menu structure:
  - Main Navigation (Home, About)
  - Antenna Projects (4 links)
  - Electronics Projects (3 links)
  - Test Equipment (3 links)
  - Telegraph & CW (3 links)
  - 3D Printing (3 links)
  - Resources (2 links)
- Hover effects (blue highlight)
- Consistent across all pages

### Content Area (Center)
- White background (#ffffff)
- Georgia serif font (professional, readable)
- 16px font size, 1.6 line height
- Max-width 1200px (readable on large screens)
- Project cards with hover effects
- Tables, code blocks, note boxes

### Address Block (Footer)
- Dark gray background (#333333)
- White/tan text
- EnergyGuy LLC contact information
- Email, website, GitHub links
- Copyright notice
- CC BY-SA 4.0 license info
- Full-width, professional appearance

### Color Palette (Low Eye Strain)
| Element | Color | Hex Code | Purpose |
|---------|-------|----------|---------|
| Background | Off-white | #f5f5f0 | Easy on eyes, not harsh white |
| Text | Dark gray | #333333 | Readable, not harsh black |
| Primary accent | Soft blue | #4a7ba7 | Professional, calming |
| Secondary accent | Darker blue | #2c5f8d | Links, headings |
| Navigation | Light tan | #e8e8e0 | Warm, subtle contrast |
| Footer | Dark gray | #333333 | Professional, grounding |

---

## Content Integration

### Source Directories Linked
All navigation links point to pages that will display content from:

1. `/media/merv/hank/scratch/claude-code/new_stuff/` - Recent projects
2. `/media/merv/hank/scratch/claude-code/tinysa_nanovna/` - Test equipment
3. `/media/merv/hank/scratch/claude-code/ebook2cw/` - CW learning
4. `/media/merv/hank/scratch/claude-code/longwire/` - Longwire antennas
5. `/media/merv/hank/scratch/claude-code/dipole/` - Dipole antennas
6. `/media/merv/hank/scratch/claude-code/loop/` - Loop antennas

### Existing Content Ready to Add
- Station grounding plan (already integrated)
- Neveready battery design (OpenSCAD + docs)
- Darkroom safelight design (OpenSCAD + docs)
- Ferro rod handle design (OpenSCAD + docs)
- CW filter design (Python + measurements)
- Faraday cage designs (OpenSCAD + docs)
- SDR cluster config (Corosync, NFS, VNC)

---

## Next Steps

### Immediate (Before Upload to GoDaddy)

1. **Create PNG Banner Image (Optional)**
   ```bash
   # Create simple text banner in GIMP or similar:
   # - 1200×150px
   # - Gradient blue background
   # - "ENERGYGUY LLC" in white
   # - Save as: images/energyguy_banner.png
   ```

2. **Replace Placeholder Pages**
   - Swap stub pages with full project documentation
   - Add images, measurements, and build notes
   - Link to source files and BOMs where available

3. **Validate HTML**
   ```bash
   # Check HTML validity:
   # https://validator.w3.org/
   # Upload each HTML file, fix any errors
   ```

4. **Test Locally**
   ```bash
   # Open index.html in browser:
   firefox /media/merv/hank/scratch/claude-code/new_stuff/HTML/index.html

   # Test all links
   # Check responsive design (resize browser)
   # Verify colors are easy on eyes
   ```

### Upload to GoDaddy

**Upload via FTP/cPanel:**

1. Log into GoDaddy hosting account
2. Open File Manager or FTP client
3. Navigate to public_html directory
4. Upload entire HTML directory contents:
   - index.html → public_html/index.html
   - css/ → public_html/css/
   - about/ → public_html/about/
   - antennas/ → public_html/antennas/
   - etc.

5. Set permissions:
   - Files: 644 (readable by all, writable by owner)
   - Directories: 755 (executable/listable by all)

6. Test live site:
   - Visit: https://www.doflagie.com
   - Test all navigation links
   - Verify images load (if any)

**Upload via Git (Alternative):**

```bash
cd /media/merv/hank/scratch/claude-code/new_stuff/HTML
git init
git add .
git commit -m "Initial EnergyGuy LLC website"
git remote add origin https://github.com/doflagie/energyguy-website.git
git push -u origin main
```

Then enable GitHub Pages in repository settings for free hosting alternative.

### Content Expansion

**Priority 1: Complete Antenna Pages**
- longwire.html (EFHW for 27' mast)
- dipole.html (various dipole designs)
- loop.html (magnetic loop, NVIS loop)

**Priority 2: Add Project Pages**
- neveready.html (USB-C battery with OpenSCAD files)
- darkroom_safelight.html (film photography safelight)
- ferro_rod.html (one-handed fire starter)

**Priority 3: Electronics Pages**
- filters.html (CW filter, frequency response plots)
- sdr_cluster.html (Raspberry Pi cluster setup)
- faraday_cage.html (RFI shielding designs)

**Priority 4: Test Equipment Pages**
- tinysa.html (spectrum analyzer tutorials)
- nanovna.html (VNA usage and calibration)
- test_equipment.html (general test equipment guides)

### Adding Images/Schematics

**PNG Generation (from Python):**

```python
# Example: Save matplotlib plot as PNG
import matplotlib.pyplot as plt

# Your plotting code here
plt.savefig('/media/merv/hank/scratch/claude-code/new_stuff/HTML/images/filter_response.png',
            dpi=150, bbox_inches='tight')
```

**PNG from OpenSCAD:**

```bash
# Render OpenSCAD design to PNG
openscad -o images/neveready_battery.png \
         --imgsize=800,600 \
         --camera=0,0,0,60,0,45,300 \
         neveready_battery_usbc.scad
```

**Add to HTML:**

```html
<figure>
    <img src="../images/filter_response.png"
         alt="Chebyshev filter frequency response"
         class="schematic">
    <figcaption>600 Hz CW filter frequency response (TinySA measurement)</figcaption>
</figure>
```

---

## GitHub Integration

### Create Repository

```bash
cd /media/merv/hank/scratch/claude-code/new_stuff/HTML
git init
git add .
git commit -m "Initial commit - EnergyGuy LLC website"

# Create repository on GitHub first, then:
git remote add origin https://github.com/yourusername/energyguy-website.git
git branch -M main
git push -u origin main
```

### Enable GitHub Pages

1. Go to repository settings
2. Pages section
3. Source: main branch, / (root)
4. Site will be live at: https://yourusername.github.io/energyguy-website/

### Continuous Updates

```bash
# After making changes:
git add .
git commit -m "Add longwire antenna page"
git push

# Site updates automatically (GitHub Pages)
# Or manually upload to GoDaddy
```

---

## Knowledge Preservation Goals

### Why This Matters

> "I won't be around forever. None of us will. But the knowledge and techniques we document can outlive us."

This website serves multiple purposes:

1. **Permanent Record:** Projects documented in detail, not lost if hardware fails
2. **Community Benefit:** Others can learn from successes AND failures
3. **Business Platform:** Print-on-demand designs, consulting services
4. **Amateur Radio Tradition:** Sharing knowledge, helping others, experimenting

### Backup Strategy

- **Local:** Files on local machine (`/media/merv/hank/scratch/claude-code/new_stuff/HTML/`)
- **GitHub:** Version-controlled, off-site backup
- **GoDaddy:** Production site, separate hosting
- **External Drive:** Periodic backup of entire directory

### License Approach

- **Documentation:** CC BY-SA 4.0 (share and remix with attribution)
- **Code (HTML/CSS):** MIT (free to use, modify, distribute)
- **Designs (OpenSCAD):** CC BY-SA 4.0 (share modifications)

This ensures the work remains available and useful even if you can't maintain it.

---

## Site Statistics

| Metric | Value |
|--------|-------|
| **HTML Pages Created** | 5 complete, ~20 planned |
| **CSS Size** | 9KB (single file, well-commented) |
| **Total Site Size** | <50KB (without images) |
| **Estimated Full Site** | <5MB (with images, PNGs) |
| **Load Time** | <1 second (on cable/fiber) |
| **Mobile Friendly** | Yes (responsive design) |
| **Browser Support** | All modern browsers |
| **Accessibility** | Good (semantic HTML, readable colors) |

---

## Hosting Budget

### GoDaddy Shared Hosting
- **Cost:** ~$5-10/month (basic plan)
- **Storage:** 100GB (more than enough)
- **Bandwidth:** Unlimited (for typical traffic)
- **Email:** Included (merv@doflagie.com)
- **Domain:** $15/year (energyguy.com)

### GitHub Pages (Free Alternative)
- **Cost:** FREE
- **Storage:** 1GB (sufficient)
- **Bandwidth:** 100GB/month
- **Custom domain:** Supported (energyguy.com)
- **HTTPS:** Included (via Let's Encrypt)

**Recommendation:** Start with GitHub Pages (free), move to GoDaddy if you need email hosting or want professional image.

---

## Launch Checklist

Before going live:

- [ ] All HTML files validated (no errors)
- [ ] All internal links tested
- [ ] Responsive design tested (mobile, tablet, desktop)
- [ ] Contact email verified (merv@doflagie.com set up)
- [ ] Address information confirmed
- [ ] Copyright/license info correct
- [ ] At least 5-10 pages with real content (not just placeholders)
- [ ] Images optimized (<200KB each)
- [ ] README and documentation complete
- [ ] GitHub repository created (backup)
- [ ] FTP/cPanel access to GoDaddy confirmed

---

## Future Enhancements (Phase 2)

After initial launch:

1. **Blog Section:** Project logs, restoration progress, learning notes
2. **Download Area:** OpenSCAD files, PDFs, Python scripts
3. **Photo Gallery:** Completed projects, work-in-progress shots
4. **Search Function:** Simple JavaScript search across pages
5. **RSS Feed:** Updates for subscribers
6. **Gopher Mirror:** Text-only mirror via gophermap files (already exist)
7. **YouTube Integration:** Embed videos when channel launches

---

## Maintenance Schedule

### Weekly
- Check for broken links
- Respond to contact emails
- Add new content (1-2 pages per week goal)

### Monthly
- Review site analytics (if added)
- Update project status pages
- Backup site to external drive

### Quarterly
- Major content additions
- Design/layout improvements
- Update documentation

---

**Website Created:** January 8, 2026
**Status:** Core structure complete
**Next Step:** Test locally, then upload to hosting
**Launch Target:** January 2026

**Created by:** Claude (Sonnet 4.5) for Mervyn Martin
**Contact:** merv@doflagie.com

---

## Summary

This website provides:
✓ Professional business presence for EnergyGuy LLC
✓ Knowledge preservation platform
✓ Amateur radio project documentation
✓ Print-on-demand design showcase
✓ Contact point for collaboration
✓ Permanent record of technical work

**The foundation is built. Now it's time to fill it with your knowledge and experience.**

73 de Mervyn Martin
Paradise, California
