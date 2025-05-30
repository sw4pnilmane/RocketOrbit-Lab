#https://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy
#https://www.nar.org/standards-and-testing-committee/nar-certified-motors/
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import subprocess

from subprocess import *

G=6.67408e-11
M=5.972e24
r=6371e3
def vc(h):
	return np.sqrt(G*M/(r+h))


#function to find drag
def Drag(vel,frontal_area):
	drag_coef = float(ent_drag_coef.get())
	air_density = 1.225
	D = 0.5*air_density*(vel**2)*drag_coef*frontal_area
	#print('D',D)
	return D

#function to findinstataneous accelaration
def AccelerationWithDrag(thrust,vel,frontal_area,weight_at_start,prop_w_loss):
	g=9.81
	if vel >= 0:
		acc = ((thrust - Drag(vel,frontal_area))/(weight_at_start-prop_w_loss))-g
		#print('acc',acc)
	else:
		acc = -g
		#print('acc',acc)
	return acc

#Function for time and thrust data for rockets
def CreateMotorData(motor):
	
        if motor == "A":
                ev=2700

        if motor == "B":
                ev=3047#7800

        if motor == "C":
                ev=24000 #36700

        if motor == "D":
                ev=129000
        
        alph=(float(ent_prop_weight.get())/100000)
        alph1=[]
        #print('alph')
        #print(alph)
        for i in range(1,101):
                alph1.append(i*alph)
        #print('alph1')
        #print(alph1)
        proplost=[]
        for i in range(len(alph1)):
                #proplost.append(float(ent_prop_weight.get())/1000-alph1[i])
                #proplost.append(float(fweight)/1000-alph1[i])
                proplost.append(float(alph1[i]))
        #print('proplost')
        #print(proplost)
        time = list(range(len(alph1)))
        thrust=[]
        for i in range(1,101):
                thrust.append(ev*(alph))
                
        #print('thrust')
        #print(thrust)
        
	#thrust_data = [i.split("    ") for i in data.split(",")]
	#print(ent_prop_weight.get())
        #time = []
        #for i in range(0,101):
        #        time.append(i)

        return time, thrust
        #print('time')
        #print(time)

	#thrust = [1*float(thrust_data[i][1]) for i in range(0,len(thrust_data))]
                

#Function to plot time to thrust graph
def PlotMotorData(time,thrust):
	plt.plot(time, thrust)
	plt.title("Burn characteristics of motor")
	plt.ylabel("Thrust (nm^-1s")
	plt.xlabel("Time since start of burn (s)")
	plt.grid(True)
	ax.set_facecolor("lightblue")
	plt.show()

#Function which calculates the remaining propellent in the rocket
def Proploss(fweight):
        #P=[]
        #pls=propellant_weight/len(thrust)
        alph=(float(fweight)/100000)
        alph1=[]
        #print('alph')
        #print(alph)
        for i in range(1,101):
                alph1.append(i*alph)
        #print('alph1')
        #print(alph1)
        proplost=[]
        for i in range(len(alph1)):
                #proplost.append(float(fweight)/1000-alph1[i])
                proplost.append(float(alph1[i]))
        #print(proplost)
        #print("proplost",proplost)
        return proplost

#Function which creates burn data
def CreateBurnData(time,thrust,propellant_weight,liftoff_weight,frontal_area):
	velocity = []
	acceleration = []
	drag = []
	altitude = []
	prop_loss=Proploss(propellant_weight*1000)
	v = 0
	t_old = 0
	s = 0
	
	
	for i,t in enumerate(time):
		acc = AccelerationWithDrag(thrust[i],v,frontal_area,liftoff_weight,prop_loss[i])
		if acc < 0: acc = 0
		acceleration.append(acc)
		t_diff = t-t_old
		v = v + (acc*t_diff)
		velocity.append(v)
		s = s+ v*t_diff
		altitude.append(s)
		t_old = t
	#print(velocity, acceleration, altitude, v, s, t)
	#print("velocity",velocity)
	#print("acceleration",acceleration)
	#print("altitude",altitude)
	return velocity, acceleration, altitude, v, s, t
        #sprint("velocity, acceleration, altitude")
        
        #print('velocity, acceleration, altitude, v, s, t')
     

#Function to plot burn data
def PlotBurnData(time,velocity):
   plt.figure(figsize=(8, 5))
   plt.plot(time, velocity, label='Velocity ($ms^{-1}$)')
   # plt.plot(time, acceleration, label='Acceleration ($ms^{-2}$)')
   # plt.plot(time, altitude, label='Altitude (m)')
   plt.title("Initial Burn Flight Characteristics")
   plt.ylabel("Value")
   plt.xlabel("Time (s)")
   plt.grid(True)
   plt.legend()
   
   # Save the plot
   plt.savefig("burn_flight_characteristics.png", dpi=300, bbox_inches='tight')

   # Show the plot
   plt.show()
   
def PlotBurnData2(time, altitude):
    # Create the plot
    plt.figure(figsize=(8, 5))
    # plt.plot(time, velocity, label='Velocity ($ms^{-1}$)')
    # plt.plot(time, acceleration, label='Acceleration ($ms^{-2}$)')
    plt.plot(time, altitude, label='Altitude (m)', color='orange')
    
    plt.title("Initial Burn Flight Characteristics")
    plt.ylabel("Altitude (m)")
    plt.xlabel("Time (s)")
    plt.grid(True)
    plt.legend()
    plt.savefig("burn_altitude_plot.png", dpi=300, bbox_inches='tight')
    plt.show()
    
def PlotBurnData3(time, acceleration):
    plt.figure(figsize=(8, 5))
    # plt.plot(time, velocity, label='Velocity ($ms^{-1}$)')
    # plt.plot(time, acceleration, label='Acceleration ($ms^{-2}$)')
    plt.plot(time, acceleration, label='Acceleration (m/s²)', color='green')

    plt.title("Initial Burn Flight Characteristics")
    plt.ylabel("Acceleration (m/s²)")
    plt.xlabel("Time (s)")
    plt.grid(True)
    plt.legend()
    plt.savefig("burn_acceleration_plot.png", dpi=300, bbox_inches='tight')
    plt.show()
    
    
#Function which creates coast data
def CreateCoastData(v,s,t,propellant_weight,liftoff_weight,frontal_area):
	coast_acceleration = []
	coast_altitude = []
	coast_velocity = []
	iterator = []
	second_count = t
	#acc,v,s are calculated for all 0.1 seconds till altitude is ground
	while s >0:
		acc = AccelerationWithDrag(0,v,frontal_area,liftoff_weight,0)
		coast_acceleration.append(acc)
		v = v + (acc*0.1)
		coast_velocity.append(v)
		s = s+ v*0.1
		coast_altitude.append(s)
		second_count += 0.1
		iterator.append(second_count)
	return coast_acceleration, coast_velocity, coast_altitude, iterator

#Function to plot flight profile
def PlotBurnToLandAlt(iterator, time, coast_altitude, altitude):
    plt.figure(figsize=(8, 5))
    plt.plot(time + iterator, altitude + coast_altitude, label='Altitude (m)', color='blue')
    plt.title("Profile of Flight")
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.grid(True)
    plt.legend()
    plt.savefig("burn_to_landing_altitude_plot.png", dpi=300, bbox_inches='tight')
    plt.show()

#Function to calculate altitude
def CalcAlt():
	liftoff_weight = float(ent_dry_weight.get())/1000 + float(ent_prop_weight.get())/1000
	propellant_weight = float(ent_prop_weight.get())/1000
	#convert diameter to frontal area using the circle equation pi r sqrd
	frontal_area = ((float(ent_diameter.get())/200)**2)*3.14159
	motor = motor_var.get()

	time,thrust = CreateMotorData(motor)
	velocity, acceleration,altitude, v,s,t = CreateBurnData(time,thrust,propellant_weight,liftoff_weight,frontal_area)

	coast_acceleration, coast_velocity, coast_altitude, iterator = CreateCoastData(v,s,t,propellant_weight,liftoff_weight,frontal_area)
	

	lbl_result['text'] = f"{max(coast_altitude):.3f}meter" #altitude is max of coast alt till 3 decimals
	vcrit=vc(max(coast_altitude))
	f = open('fil.txt', 'a')
	f.write(str(max(coast_altitude)))
	f.write("\n")
	f.write(str(vcrit))
	Popen('python SatelliteOrbit.py')
	#f.clear()
	f.close()
	#return vcrit

	
	
#function to call plotting of burn plot
def BurnPlotClick():
        #converting all units to SI
	liftoff_weight = float(ent_dry_weight.get())/1000
	propellant_weight = float(ent_prop_weight.get())/1000
	frontal_area = ((float(ent_diameter.get())/200)**2)*3.14159
	motor = motor_var.get()


	time,thrust = CreateMotorData(motor)
	velocity, acceleration,altitude, v,s,t = CreateBurnData(time,thrust,propellant_weight,liftoff_weight,frontal_area)

	PlotBurnData(time,velocity)
	PlotBurnData2(time,altitude)
	PlotBurnData3(time,acceleration)

#function which calls plotting fo flight profile
def FlightProfileClick():
	liftoff_weight = float(ent_dry_weight.get())/1000
	propellant_weight = float(ent_prop_weight.get())/1000
	frontal_area = ((float(ent_diameter.get())/200)**2)*3.14159
	motor = motor_var.get()

	time,thrust = CreateMotorData(motor)
	velocity, acceleration,altitude, v,s,t = CreateBurnData(time,thrust,propellant_weight,liftoff_weight,frontal_area)

	coast_acceleration, coast_velocity, coast_altitude, iterator = CreateCoastData(v,s,t,propellant_weight,liftoff_weight,frontal_area)

	PlotBurnToLandAlt(iterator,time,coast_altitude,altitude)

if __name__ == '__main__':
    m = tk.Tk()
    m.title("🚀 Rocket Flight Characteristic Calculator")
    m.configure(bg='#0b0f2b')
    m.geometry("800x520")
    m.resizable(False, False)

    # --- Main Container to Center Content ---
    main_container = tk.Frame(m, bg='#0b0f2b')
    main_container.pack(expand=True)

    # --- Section Titles ---
    tk.Label(main_container, text="🛰 Rocket Modelling", font=('Helvetica', 13, 'bold'),
             bg='#0b0f2b', fg='#6dd5ed').grid(row=0, column=0, columnspan=2, pady=(10, 8))

    # Frames
    frm_entry = tk.Frame(master=main_container, bg='#0b0f2b', padx=20, pady=20)
    frm_btn = tk.Frame(master=main_container, bg='#0b0f2b', padx=20, pady=20)
    frm_sat = tk.Frame(master=main_container, bg='#0b0f2b', padx=20, pady=20)

    # Rocket Input Section
    motor_var = tk.StringVar(m)
    motor_choices = {'A', 'B', 'C', 'D'}
    motor_var.set('A')

    tk.Label(frm_entry, text="🚀 Choose an engine", font=('Helvetica', 11, 'bold'),
             bg='#0b0f2b', fg='#6dd5ed').grid(row=1, column=0, sticky='w', pady=5)
    popupMenu = tk.OptionMenu(frm_entry, motor_var, *motor_choices)
    popupMenu.config(
        bg='#1a1a40', fg='white', font=('Helvetica', 10),
        activebackground='#3f51b5', activeforeground='white',
        highlightthickness=0
    )
    popupMenu["menu"].config(bg="#3f51b5", fg="white")
    popupMenu.grid(row=1, column=1, sticky='ew', pady=5)

    def change_dropdown(*args):
        print(motor_var.get())
    motor_var.trace('w', change_dropdown)

    fields = [
        ("🚀 Rocket Weight", "g", 'ent_dry_weight'),
        ("📏 Rocket Diameter", "cm", 'ent_diameter'),
        ("⛽ Fuel Weight", "g", 'ent_prop_weight'),
        ("🌪 Drag Coe.", "", 'ent_drag_coef')
    ]

    entries = {}
    for i, (label_text, unit, var_name) in enumerate(fields, start=2):
        tk.Label(frm_entry, text=label_text, font=('Helvetica', 11),
                 bg='#0b0f2b', fg='#e0e0e0').grid(row=i, column=0, sticky='w', pady=6)
        entry = tk.Entry(frm_entry, width=12, bg='#1a1a40', fg='white',
                         insertbackground="white", highlightbackground='#6dd5ed', highlightcolor='#6dd5ed')
        entry.grid(row=i, column=1, sticky='ew', pady=6)
        tk.Label(frm_entry, text=unit, bg='#0b0f2b', fg='#6dd5ed').grid(row=i, column=2, sticky='w')
        entries[var_name] = entry

    ent_dry_weight = entries['ent_dry_weight']
    ent_diameter = entries['ent_diameter']
    ent_prop_weight = entries['ent_prop_weight']
    ent_drag_coef = entries['ent_drag_coef']

    btn_style = {
        "bg": '#1a1a40',
        "fg": '#ffffff',
        "activebackground": '#3f51b5',
        "activeforeground": '#ffffff',
        "font": ('Helvetica', 11, 'bold'),
        "width": 22,
        "padx": 5,
        "pady": 5
    }

    # Rocket Buttons
    btn_altitude = tk.Button(frm_btn, text="🧮 Estimate Altitude", command=CalcAlt, **btn_style)
    lbl_result = tk.Label(frm_btn, text="🌌 Altitude: ?", bg='#0b0f2b', fg='#ffccff', font=('Helvetica', 12, 'bold'))
    btn_burn_plot = tk.Button(frm_btn, text="🔥 Create Burn Plot", command=BurnPlotClick, **btn_style)
    btn_profile_plot = tk.Button(frm_btn, text="📈 Create Flight Profile", command=FlightProfileClick, **btn_style)

    btn_altitude.grid(row=1, column=0, sticky='ew', pady=6, columnspan=2)
    lbl_result.grid(row=2, column=0, columnspan=2, pady=10)
    btn_burn_plot.grid(row=3, column=0, columnspan=2, sticky='ew', pady=6)
    btn_profile_plot.grid(row=4, column=0, columnspan=2, sticky='ew', pady=6)

    # --- Satellite Section Title ---
    tk.Label(main_container, text="🛰 Satellite Simulation", font=('Helvetica', 13, 'bold'),
             bg='#0b0f2b', fg='#6dd5ed').grid(row=2, column=0, columnspan=2, pady=(10, 0))

    # Satellite Input
    tk.Label(frm_sat, text="🪐 Orbital Radius", font=('Helvetica', 11),
             bg='#0b0f2b', fg='#e0e0e0').grid(row=0, column=0, sticky='w')
    sat_orb_radius = tk.Entry(frm_sat, width=15, bg='#1a1a40', fg='white',
                              insertbackground='white', highlightbackground='#6dd5ed')
    sat_orb_radius.grid(row=0, column=1, pady=6)

    tk.Label(frm_sat, text="💨 Satellite Speed", font=('Helvetica', 11),
             bg='#0b0f2b', fg='#e0e0e0').grid(row=1, column=0, sticky='w')
    sat_speed = tk.Entry(frm_sat, width=15, bg='#1a1a40', fg='white',
                         insertbackground='white', highlightbackground='#6dd5ed')
    sat_speed.grid(row=1, column=1, pady=6)

    def simulate_orbit():
        radius = sat_orb_radius.get()
        speed = sat_speed.get()
        with open("fil.txt", "w") as f:
            f.write(f"{radius}\n{speed}")
        subprocess.run(["python", "SatelliteOrbit.py"])

    sim_btn = tk.Button(frm_sat, text="🛰 Simulate Orbit", command=simulate_orbit, **btn_style)
    sim_btn.grid(row=2, column=0, columnspan=2, pady=10)

    # Layout inside main_container
    frm_entry.grid(row=1, column=0, sticky='nsew')
    frm_btn.grid(row=1, column=1, sticky='nsew')
    frm_sat.grid(row=3, column=0, columnspan=2, pady=5)

    m.mainloop()