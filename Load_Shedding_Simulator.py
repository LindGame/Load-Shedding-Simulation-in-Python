#Load Shedding System Simulator - Lindizwe Gamedze

import time
import random

class PowerZone:
    def __init__(self, name, demand, priority):
        self.name = name             # Area Name (e.g., Hospital, Residential)
        self.demand = demand         # Power consumption in Megawatts (MW)
        self.priority = priority     # 1: Critical, 2: Essential, 3: Non-Essential
        self.is_active = True        # Current Status of Power
        

    def __repr__(self):
        status = "ON" if self.is_active else "OFF"
        return f"[{self.name:<18}] Demand: {self.demand:>3}MW | Priority: {self.priority} | Status: {status}"

class IntelligentGrid:
    def __init__(self, total_capacity):
        self.total_capacity = total_capacity
        self.zones = []

    def add_zone(self, zone):
        """Adds a new power zone to the grid management system."""
        self.zones.append(zone)

    def calculate_current_demand(self):
        """Calculates total demand from all currently active zones."""
        return sum(zone.demand for zone in self.zones if zone.is_active)

    def manage_load(self):
        """Main optimization algorithm. Compares supply vs demand and handles load shedding/restoration."""
        print(f"\n--- Checking Grid Status (Available Supply: {self.total_capacity}MW) ---")

        current_demand = self.calculate_current_demand()

        # Scenario A: Demand exceeds supply -> Need to shed load
        if current_demand > self.total_capacity:
            print(f"CRITICAL: Demand ({current_demand}MW) Exceeds Capacity! Initiating targeted shedding...")
            
            # Sort zones: target lower priority (higher numbers) first
            self.zones.sort(key=lambda x: x.priority, reverse=True)

            for zone in self.zones:
                if zone.is_active and zone.priority > 1: # Protects critical priority 1 zones
                    print(f"SHEDDING LOAD: Deactivating {zone.name} (-{zone.demand}MW)...")
                    zone.is_active = False
                    current_demand -= zone.demand

                if current_demand <= self.total_capacity:
                    print(f"Grid Stabilized successfully at {current_demand}MW.")
                    break
            
            if current_demand > self.total_capacity:
                print("WARNING: Demand still exceeds capacity despite shedding non-essential zones!")

        # Scenario B: Supply exceeds demand -> Check if we can restore power to dark zones
        elif current_demand < self.total_capacity:
            self.restore_load()
            
        else:
            print(f"Grid Perfectly Stable. Current Load: {current_demand}MW. No action required.")

    def restore_load(self):
        """Attempts to bring inactive zones back online if there is excess grid capacity."""
        # Sort zones to restore highest priority (lower numbers) first
        self.zones.sort(key=lambda x: x.priority)

        for zone in self.zones:
            if not zone.is_active:
                potential_demand = self.calculate_current_demand() + zone.demand
                if potential_demand <= self.total_capacity:
                    print(f"RESTORING POWER: Reactivating {zone.name} (+{zone.demand}MW)...")
                    zone.is_active = True
                else:
                    # If we can't afford to turn this zone back on, don't try lower priority ones yet
                    break
                

#          --             --- Simulation Execution ---          --

# 1. Initializing the Grid
smart_grid = IntelligentGrid(total_capacity=500)

# 2. Adding various zones with different demands and priorities
smart_grid.add_zone(PowerZone("City Hospital", 150, 1))        # Critical
smart_grid.add_zone(PowerZone("Industrial Site/Zone", 250, 2))  # Essential
smart_grid.add_zone(PowerZone("Shopping Mall", 100, 3))        # Non-Essential
smart_grid.add_zone(PowerZone("Residential Block", 80, 2))     # Essential
smart_grid.add_zone(PowerZone("Stadium Lights", 50, 3))        # Non-Essential

def run_simulation(grid):
    print("Starting Intelligent Load Management System Simulation...")
    print("Press Ctrl+C to stop the simulation.")
    try:
        while True:
            # Simulating a fluctuating supply (e.g., Solar/Wind variations)
            grid.total_capacity = random.randint(380, 550)

            # Running the grid management brain
            grid.manage_load()

            # Showing current status of all zones (sorted cleanly  by name for readability)
            print("\nCurrent Grid Readout:")
            grid.zones.sort(key=lambda x: x.name)
            for zone in grid.zones:
                print(f"  {zone}")

            print("\nREMEMBER - Press Ctrl+C to stop the simulation.")
            print("\n" + "="*50)
            time.sleep(5) #a five second pause before the next cycle displays (for slow readers)

    except KeyboardInterrupt:
        print("\n_____________SYSTEM SIMULATION STOPPED BY OPERATOR._____________")#or some butter fingers

# Execute!
run_simulation(smart_grid)
## Remember to press Ctrl C to stop the simulation
## Ctrl C  - Remember!


#### Notes For Future Improvements

# 1. Add Time of Day Pricing/Demmand - makes the simulation a bit more realistic
# 2. Add Renewable Energy Mix - gets the simulation in tune with modern grids because everyone is going solar and stuff or sth
# 3. someting something something...

































































# not that bad, eh?
# too basic? ( ¬_¬ )


