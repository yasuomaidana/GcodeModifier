;FLAVOR:RepRap
;TIME:1.0
;Filament used:2
;Layer height: 2
;Generated with YasuosHand
G21        ;metric values
G90        ;absolute positioning
M82        ;set extruder to absolute mode
M107       ;start with the fan off
M302
M92 E1000
;G28 X0 Y0  ;move X/Y to min endstops
;G28 Z0     ;move Z to min endstops
;G1 Z15.0 F2 ;move the platform down 15mm
G92 E0                  ;zero the extruded length
G1 F2 E2              ;extrude 3mm of feed stock
G92 E0                  ;zero the extruded length again
G1 F2
M117 Printing...
M107
;it starts here
G1 F2
G1 E2
