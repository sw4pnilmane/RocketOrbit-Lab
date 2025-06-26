# 🚀 RocketOrbit-Lab

**RocketOrbit-Lab** is a simulation lab that models a rocket's complete journey from **launch to orbit**. It combines rocket thrust simulation, burn and coast phases, and satellite orbital animation — all controlled through an intuitive GUI built using Python and Tkinter.
![Screenshot 2025-06-27 032307](https://github.com/user-attachments/assets/d27f3a4a-89cd-4917-a4e5-9428bedc88b2)


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
  - Stable orbit
  - ![Screenshot 2025-06-27 032503](https://github.com/user-attachments/assets/9684127f-f6c7-4217-8c27-f40c4c5851b2)

  - Crash detection if satellite falls back
  - ![Screenshot 2025-06-27 032637](https://github.com/user-attachments/assets/c2fc0a9d-db16-4eb2-9654-6e26ea837382)


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

