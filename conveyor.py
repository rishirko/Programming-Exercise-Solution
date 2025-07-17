import random

class WorkerStation:
    """A station that picks A and B, assembles P in 4 steps, then places P."""
    def __init__(self, position):
        self.position = position
        self.components_in_hand = []        
        self.assembly_time_remaining = 0 
        self.has_product = False         
    def interact(self, slot_content):
        """
        Decide on one action:
        - 'place': put 'P' if ready and slot empty
        - 'pick' : take A or B if needed
        - 'none' : do nothing
        Returns (action, item_to_place_or_None).
        """
        if self.assembly_time_remaining > 0:
            return 'none', None

        if self.has_product and slot_content is None:
            self.has_product = False
            return 'place', 'P'

        needed = []
        if 'A' not in self.components_in_hand:
            needed.append('A')
        if 'B' not in self.components_in_hand:
            needed.append('B')

        if slot_content in needed:
            self.components_in_hand.append(slot_content)
            if len(self.components_in_hand) == 2:
                self.assembly_time_remaining = 4
                self.components_in_hand.clear()
            return 'pick', None

        return 'none', None

    def advance_time(self):
        """Advance assembly timer and mark product ready when done."""
        if self.assembly_time_remaining > 0:
            self.assembly_time_remaining -= 1
            if self.assembly_time_remaining == 0:
                self.has_product = True


class Simulation:
    def __init__(self, steps=100, belt_length=10, station_positions=None, seed=None):
        self.steps = steps
        self.belt = [None] * belt_length
        self.stations = []
        if station_positions is None:
            station_positions = [2, 5, 8]
        for pos in station_positions:
            self.stations.append(WorkerStation(pos))
        self.random = random.Random(seed)

        self.finished = 0
        self.lost_A = 0
        self.lost_B = 0

    def run(self):
        for _ in range(self.steps):
            out_item = self.belt.pop()
            if out_item == 'P':
                self.finished += 1
            elif out_item == 'A':
                self.lost_A += 1
            elif out_item == 'B':
                self.lost_B += 1

            new_item = self.random.choice([None, 'A', 'B'])
            self.belt.insert(0, new_item)

            for station in self.stations:
                idx = station.position
                slot = self.belt[idx]
                action, item = station.interact(slot)
                if action == 'place':
                    self.belt[idx] = item
                elif action == 'pick':
                    self.belt[idx] = None

            for station in self.stations:
                station.advance_time()

        return self.finished, self.lost_A, self.lost_B


if __name__ == '__main__':
    sim = Simulation(steps=1000, seed=45)
    finished, lost_A, lost_B = sim.run()
    print(f"Finished products: {finished}")
    print(f"Unpicked A's:      {lost_A}")
    print(f"Unpicked B's:      {lost_B}")