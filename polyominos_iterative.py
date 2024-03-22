import sys

def normalize(polyomino):
    """Normalize a polyomino to its canonical form based on its coordinates."""
    min_x = min(x for x, y in polyomino)
    min_y = min(y for x, y in polyomino)
    return tuple(sorted((x - min_x, y - min_y) for x, y in polyomino))

def rotate90(polyomino):
    """Rotate polyomino 90 degrees clockwise."""
    return normalize([(-y, x) for x, y in polyomino])

def get_rotations(polyomino):
    """Generate all rotations of a polyomino."""
    rotations = [polyomino]
    for _ in range(3):
        rotations.append(rotate90(rotations[-1]))
    return [normalize(rotation) for rotation in rotations]

def unique_rotations(polyominoes):
    """Deduplicate polyominoes considering their rotations."""
    unique = set()
    for polyomino in polyominoes:
        rotations = get_rotations(polyomino)
        representative = min(rotations)
        unique.add(representative)
    return list(unique)

def generate_polyominoes_iter(n):
    """Generate all unique polyominoes of size n iteratively."""
    if n < 1:
        return []
    polyominoes = {((0, 0),)}  # Initialize with a single block polyomino
    for _ in range(1, n):
        new_polyominoes = set()
        for poly in polyominoes:
            for x, y in poly:
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_block = (x + dx, y + dy)
                    if new_block not in poly:
                        new_poly = poly + (new_block,)
                        normalized = normalize(new_poly)
                        new_polyominoes.add(normalized)
        polyominoes = new_polyominoes
    return unique_rotations(polyominoes)

def print_polyomino(polyomino):
    """Print a polyomino using ASCII art."""
    min_x = min(x for x, y in polyomino)
    max_x = max(x for x, y in polyomino)
    min_y = min(y for x, y in polyomino)
    max_y = max(y for x, y in polyomino)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print("■" if (x, y) in polyomino else " ", end=" ")
        print()

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 4  # Default to n=4 if no argument provided
    unique_polyominoes = generate_polyominoes_iter(n)

    print("Number of unique polyominoes up to rotation:", len(unique_polyominoes))
    for i, poly in enumerate(unique_polyominoes[:], start=1):
        print("Unique Polyomino {}:".format(i))
        print_polyomino(poly)
        print()

