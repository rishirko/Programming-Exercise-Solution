# Conveyor Belt Assembly Simulation

This project simulates a simple conveyor belt system with fixed stations and randomized component input, designed to mimic a basic assembly line process.

## 🛠️ Assumptions

- **Belt Length**: 10 slots  
  > Long enough for components to circulate and interact with stations, yet small enough to allow efficient array operations.

- **New Slot Input**: Randomly chosen from `[None, 'A', 'B']` with equal probability (1/3 each).

- **Station Positions**: Fixed at slots `[2, 5, 8]`  
  > Chosen to evenly distribute workload across the belt.

- **Time Step Actions**:
  - The belt moves forward by popping the last slot and inserting a new random item at the start.
  - Each station performs one action: **place**, **pick**, or **do nothing**.
  - Assembly timers at stations are decremented.
  - Stations operate on distinct slots, ensuring no collisions.
  - Workers can hold at most **two components**.
  - Assembly requires **4 complete time steps** per product.

---

## 🧪 Sample Outputs

### Case 1
**Input**: `steps = 100`  
**Output**:
  Finished products: 17
  Unpicked A's: 11
  Unpicked B's: 6


### Case 2  
**Input:** `steps = 1000`  
**Output:**
  Finished products: 220
  Unpicked A's: 57
  Unpicked B's: 72

## 🚀 Getting Started

### Prerequisites

- Python 3.0 or higher installed 
