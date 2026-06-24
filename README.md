# Load-Shedding-Simulation-in-Python
An OOP Python simulation of a smart grid automation system using priority-based algorithms to manage real-time load shedding and power restoration.

# Intelligent Load Shedding System Simulation

An object-oriented Python simulation designed to model smart grid power distribution, automation, and automated load shedding algorithms. This project demonstrates how modern electrical grids can dynamically balance fluctuating power supply (such as intermittent renewable energy) against consumer demand while strictly protecting critical infrastructure.

## Core Features

* **Dynamic Supply Fluctuations:** Simulates real-world grid volatility (e.g., solar/wind dropouts) by dynamically adjusting total generation capacity.
* **Priority-Based Shedding Logic:** Categorizes power zones into Grid Priorities (Critical, Essential, Non-Essential) to ensure hospitals and emergency services never lose power during a shortage.
* **Automated Load Restoration:** Proactively detects when grid capacity recovers and automatically restores power to dark zones sequentially based on priority.
* **Object-Oriented Architecture:** Built entirely using clean, extensible Python OOP principles (`PowerZone` and `IntelligentGrid` classes).

## System Architecture & Logic Flow

1. **Grid Monitoring:** Continuous evaluation of real-time supply vs. aggregate demand.
2. **Shedding Sequence:** If $Demand > Supply$, the system iteratively deactivates non-essential zones (Priority 3, then Priority 2) until the grid stabilizes.
3. **Restoration Sequence:** If $Supply > Demand$, the system checks if it can safely bring inactive zones back online without re-tripping the grid.

## Future Roadmap

* **Time-of-Day Pricing/Demand Curves:** Integrating peaking patterns (e.g., residential spikes during evening hours).
* **Renewables Integration:** Breaking total capacity into discrete Base-Load, Solar, and Wind generation inputs influenced by weather metrics.
