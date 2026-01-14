// Antenna gear parts template for 200x200x200 printers
// Units: mm

$fn = 64;

module simple_enclosure(body_x=120, body_y=80, body_z=45, wall=3) {
    difference() {
        cube([body_x, body_y, body_z], center=false);
        translate([wall, wall, wall])
            cube([body_x - 2 * wall, body_y - 2 * wall, body_z - 2 * wall], center=false);
    }
}

module mounting_plate(plate_x=120, plate_y=80, plate_t=4, hole_r=2.2) {
    difference() {
        cube([plate_x, plate_y, plate_t], center=false);
        for (x = [10, plate_x - 10])
            for (y = [10, plate_y - 10])
                translate([x, y, -1]) cylinder(h=plate_t + 2, r=hole_r);
    }
}

simple_enclosure();
translate([0, 100, 0]) mounting_plate();
