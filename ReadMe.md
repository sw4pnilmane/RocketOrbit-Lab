# 🚀 RocketOrbit-Lab

**RocketOrbit-Lab** is a simulation lab that models a rocket's complete journey from **launch to orbit**. It combines rocket thrust simulation, burn and coast phases, and satellite orbital animation — all controlled through an intuitive GUI built using Python and Tkinter.

---

## 🧠 What It Does

### 🔧 Rocket Launch Simulation
- Choose from standard motor classes (A–D)
- Input physical characteristics:
  - Rocket mass
  - Fuel weight
  - Diameter
  - Drag coefficient
- Simulates:
  - Burn phase: thrust, acceleration, and altitude
  - Coasting phase after burnout
  - Apogee (peak altitude) calculation
- Outputs:
  - Velocity, altitude, and acceleration plots
  - Full flight profile

### 🛰 Satellite Orbit Simulation
- Auto-launches after apogee calculation
- Uses RK4 numerical integration for orbital path
- Real-time animation with:
  - Radial distance
  - Velocity display
  - Crash detection if satellite falls back

---

## 🎯 Features

| Module              | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| 🚀 Rocket Engine     | Simulates launch using thrust, drag, and mass loss                          |
| 📈 Plotting          | Generates burn and trajectory graphs using Matplotlib                       |
| 🛰 Orbital Physics    | Simulates satellite orbit using Newtonian physics and RK4                   |
| 🎥 Animation         | Visualizes orbit in a Tkinter canvas                                        |
| 🔁 Data Sync         | Passes launch data to orbital sim via `fil.txt`                             |

---

