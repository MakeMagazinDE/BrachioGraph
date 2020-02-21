from brachiograph import BrachioGraph

bg = BrachioGraph(
    inner_arm=8,           # Oberarmlaenge cm        
    outer_arm=8,           # Unterarmlaenge cm
    bounds=(-8, 4, 4, 13), # Koordinaten Zeichenbereich
    servo_1_degree_ms=-10, # Bewegung Schulterservo
    servo_2_degree_ms=10,  # Bewegung Ellenbogenservo
    servo_1_centre=1500,    # Mittelstellung Schulter
    servo_2_centre=1500,    # Mittelstellung Ellenbogen
    pw_down=1850,          # Position Stift unten
    pw_up=1500,            # Position Stift angehoben 
)
