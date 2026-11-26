    path = [
        "[default]Tank_Level",
        "[default]Auto_Mode",
        "[default]High_Level",
        "[default]Inlet_Valve_Command",
        "[default]Pump_Command",
        "[default]Auto_Fill_State"
    ]

    values = system.tag.readBlocking(path)

    level = values[0].value
    auto = values[1].value
    high_level = values[2].value
    inlet_command = values[3].value
    pump_command = values[4].value
    auto_fill = values[5].value

    # High-level hysteresis
    if level >= 90:
        high_level = True
    elif level <= 80:
        high_level = False

    # AUTO state machine
    if auto:
        if level <= 20:
            auto_fill = True

        elif level >= 90:
            auto_fill = False

        if auto_fill:
            inlet_command = True
            pump_command = False

        else:
            inlet_command = False
            pump_command = True

    # Simulated interlocks
    inlet_running = inlet_command and not high_level
    pump_running = pump_command and level > 20

    # Simulate tank movement
    if inlet_running:
        level = level + 1

    if pump_running:
        level = level - 1

    level = max(0, min(100, level))

    # Write results
    system.tag.writeBlocking(
        [
            "[default]Inlet_Valve_Command",
            "[default]Pump_Command",
            "[default]Auto_Fill_State",
            "[default]High_Level",
            "[default]Tank_Level"
        ],
        [
            inlet_command,
            pump_command,
            auto_fill,
            high_level,
            level
        ]
    )