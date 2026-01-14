// Loop antenna feed point insulators
// All dimensions in mm. Designed for printers up to 200x200x200.

$fn = 64;

// Feed point plate with two wire tie holes and two feed holes.
module loop_feed_insulator(body_len=70, body_w=22, body_h=10,
                           hole_d=4, feed_d=5, edge=10) {
    difference() {
        hull() {
            translate([0, 0, 0]) cylinder(h=body_h, r=body_w/2);
            translate([body_len, 0, 0]) cylinder(h=body_h, r=body_w/2);
        }
        translate([edge, 0, body_h/2]) rotate([90, 0, 0]) cylinder(h=body_w+2, r=hole_d/2);
        translate([body_len - edge, 0, body_h/2]) rotate([90, 0, 0]) cylinder(h=body_w+2, r=hole_d/2);
        translate([body_len/2 - 6, 0, body_h/2]) rotate([90, 0, 0]) cylinder(h=body_w+2, r=feed_d/2);
        translate([body_len/2 + 6, 0, body_h/2]) rotate([90, 0, 0]) cylinder(h=body_w+2, r=feed_d/2);
    }
}

loop_feed_insulator();
