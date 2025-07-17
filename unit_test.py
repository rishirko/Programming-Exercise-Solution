import unittest
from conveyor import WorkerStation, Simulation

class TestWorkerStation(unittest.TestCase):
    def test_pick_components_and_assemble(self):
        ws = WorkerStation(position=0)

        action, item = ws.interact('A')
        self.assertEqual(action, 'pick')
        self.assertIsNone(item)
        self.assertIn('A', ws.components_in_hand)

        action, item = ws.interact('B')
        self.assertEqual(action, 'pick')
        self.assertIsNone(item)
        self.assertEqual(ws.assembly_time_remaining, 4)
        self.assertEqual(ws.components_in_hand, [])

        for _ in range(4):
            ws.advance_time()
        self.assertTrue(ws.has_product)

        action, item = ws.interact(None)
        self.assertEqual(action, 'place')
        self.assertEqual(item, 'P')
        self.assertFalse(ws.has_product)

    def test_station_idle_when_assembling(self):
        ws = WorkerStation(position=0)
        ws.assembly_time_remaining = 2
        action, item = ws.interact('A')
        self.assertEqual(action, 'none')
        self.assertIsNone(item)


class TestSimulation(unittest.TestCase):
    def test_simulation_outputs_consistent_with_seed(self):
        sim = Simulation(steps=50, seed=123)
        finished, lost_A, lost_B = sim.run()

        sim2 = Simulation(steps=50, seed=123)
        finished2, lost_A2, lost_B2 = sim2.run()

        self.assertEqual(finished, finished2)
        self.assertEqual(lost_A, lost_A2)
        self.assertEqual(lost_B, lost_B2)

    def test_belt_length_unchanged(self):
        sim = Simulation(steps=10, belt_length=7, station_positions=[2, 4, 6], seed=123)
        initial_len = len(sim.belt)
        sim.run()
        final_len = len(sim.belt)
        self.assertEqual(initial_len, final_len)


if __name__ == "__main__":
    unittest.main(verbosity=2)