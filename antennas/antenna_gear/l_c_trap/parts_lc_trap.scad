// L/C trap parts for 200x200x200 printers
// Units: mm

$fn = 64;

module coil_form(body_len=70, body_d=28, flange_d=50, flange_t=3, hole_d=4) {
    difference() {
        union() {
            cylinder(h=body_len, r=body_d / 2);
            translate([0, 0, 0]) cylinder(h=flange_t, r=flange_d / 2);
            translate([0, 0, body_len - flange_t]) cylinder(h=flange_t, r=flange_d / 2);
        }
        // Center hole
        translate([0, 0, -1]) cylinder(h=body_len + 2, r=hole_d / 2);
        // Vent holes
        for (z = [10:10:body_len - 10]) {
            translate([body_d / 2 - 3, 0, z]) rotate([0, 90, 0]) cylinder(h=6, r=2);
        }
    }
}

module end_cap(cap_d=60, cap_t=4, hole_r=2.2, bolt_circle=42) {
    difference() {
        cylinder(h=cap_t, r=cap_d / 2);
        for (a = [0:90:270]) {
            translate([
                (bolt_circle / 2) * cos(a),
                (bolt_circle / 2) * sin(a),
                -1
            ]) cylinder(h=cap_t + 2, r=hole_r);
        }
    }
}

module trap_enclosure(body_x=120, body_y=60, body_z=40, wall=3) {
    difference() {
        cube([body_x, body_y, body_z], center=false);
        translate([wall, wall, wall])
            cube([body_x - 2 * wall, body_y - 2 * wall, body_z - 2 * wall], center=false);
    }
}

// Preview layout
translate([-70, 0, 0]) coil_form();
translate([20, 0, 0]) end_cap();
translate([-60, 70, 0]) trap_enclosure();
