islands = range(4)  # A = 0, B = 1, C = 2, D = 3
forward, reverse = range(2)  # forward = 0, reverse = 1
search_directions = [forward, reverse]
search_directions_text = ["forward", "reverse"]
invalid_island = -1

og_bridges = [[0,2,1,0], [2,0,1,2], [1,1,0,1], [0,2,1,0]]
new_bridges = [[0,2,2,0], [2,0,1,3], [2,1,0,1], [0,3,1,0]]

class Eular:
    def __init__(self, bridges, islands):
        self.bridges = [bridge[:] for bridge in bridges]
        self.bridges_original = [bridge[:] for bridge in self.bridges]
        self.islands = islands[:]
        self.direction = forward

    def reset_bridges(self):
        self.bridges = [bridge[:] for bridge in self.bridges_original]

    def generate_path(self, starting_island, order=forward):  # attempt to find eularian cycle
        if order != self.direction:
            self.islands = self.islands[::-1]
            self.direction = order
        current_island = starting_island
        last_island = invalid_island
        while current_island != last_island:  # loop until stuck
            last_island = current_island
            for island in self.islands:
                if self.bridges[current_island][island] > 0:
                    self.bridges[current_island][island] -= 1
                    self.bridges[island][current_island] -= 1
                    print("Going from ", chr(current_island+65), " to ", chr(island+65))
                    current_island = island  # move to next islands
                    break
        return current_island

    def bridges_left(self):
        for island in self.bridges:
            for bridge in island:
                if bridge > 0:
                    return True
        return False

def main():
    final_island = invalid_island
    Algorithm = Eular(new_bridges, islands)
    for starting_island in range(4):
        print("\nStarting Island = ", chr(starting_island+65))
        for search_direction in search_directions:
            final_island = Algorithm.generate_path(starting_island, search_direction)
            if Algorithm.bridges_left():
                print("\n" + search_directions_text[search_direction] + " bias path-finding failed.\n")
                Algorithm.reset_bridges()
            else: break
        if Algorithm.bridges_left():
            print("No Eulerian cycle found.\n")
        else:
            if final_island == starting_island:
                print("Eularian cycle found!")
            else:
                print("All bridges used, but not back at starting island.\n")
            print("Final Island = ", chr(final_island+65))
            print("Remaining Bridges = ", Algorithm.bridges)
        Algorithm.reset_bridges()

if __name__ == '__main__': main()

