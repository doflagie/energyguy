// End-fed quarter-wave feed point insulators
// All dimensions in mm. Designed for printers up to 200x200x200.

$fn = 64;

// Base insulator with two tie holes and one feed hole.
module end_fed_base_insulator(body_len=70, body_w=20, body_h=10,
                              hole_d=4, feed_d=6, edge=10) {
    difference() {
        hull() {
            translate([0, 0, 0]) cylinder(h=body_h, r=body_w/2);
            translate([body_len, 0, 0]) cylinder(h=body_h, r=body_w/2);
        }
        translate([edge, 0, body_h/2]) rotate([90, 0, 0]) cylinder(h=body_w+2, r=hole_d/2);
        translate([body_len - edge, 0, body_h/2]) rotate([90, 0, 0]) cylinder(h=body_w+2, r=hole_d/2);
        translate([body_len/2, 0, body_h/2]) rotate([90, 0, 0]) cylinder(h=body_w+2, r=feed_d/2);
    }
}

end_fed_base_insulator();
