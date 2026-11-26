# Ignition Water Tank Control

Water tank control simulation built with Ignition Perspective
and Python/Jython scripting.

## Features
- Manual inlet valve and pump control
- Automatic filling and draining between 20% and 90%
- High level inlet protection
- Low level pump protection
- Live tank level and simulated equipment status

## Simulation approach
Memory tags represent tank level and control commands.
Expression tags provide simulated equipment status.
A Gateway timer script updates the simulated water level.
No physical PLC, sensors, or actuators are connected.

## Files

- [Ignition project export](ignition/water_tank_control.zip)
- [Tag configurations](ignition/tank_tags.json)
- [Gateway timer script](scripts/tank_level_simulation.py)


## Requirements
Ignition with the Perspective module.
The simulation script runs inside Ignition.