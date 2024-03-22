import sys


def normalize(polyomino):
    """Normalize a polyomino to a canonical form based on its coordinates."""
    min_x = min(x for x, y in polyomino)
    min_y = min(y for x, y in polyomino)
    normalized = sorted([(x - min_x, y - min_y) for x, y in polyomino])
    return tuple(normalized)


def add_square(polyomino):
    """Generate all unique polyominoes by adding a square to the given polyomino."""
    adjacent_squares = [
        (x + dx, y + dy)
        for x, y in polyomino
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ]
    new_polyominoes = [
        polyomino + [(x, y)]
        for x, y in set(adjacent_squares)
        if (x, y) not in polyomino
    ]
    return [normalize(p) for p in new_polyominoes]


def generate_polyominoes(n):
    """Generate all unique polyominoes of size n."""
    if n == 1:
        return [((0, 0),)]
    previous_polyominoes = generate_polyominoes(n - 1)
    new_polyominoes = set()
    for poly in previous_polyominoes:
        poly_list = list(poly)
        for new_poly in add_square(poly_list):
            new_polyominoes.add(new_poly)
    return list(new_polyominoes)


def rotate90(polyomino):
    """Rotate polyomino 90 degrees clockwise."""
    return normalize([(-y, x) for x, y in polyomino])


def get_rotations(polyomino):
    """Get all rotations of a polyomino."""
    rotations = [polyomino]
    for _ in range(3):
        rotations.append(rotate90(rotations[-1]))
    return [normalize(rotation) for rotation in rotations]


def unique_rotations(polyominoes):
    """Filter polyominoes to unique ones up to rotation."""
    unique = set()
    for polyomino in polyominoes:
        rotations = get_rotations(polyomino)
        representative = min(rotations)
        unique.add(representative)
    return list(unique)


def print_polyomino(polyomino):
    """Print a polyomino using ASCII art."""
    min_x = min(x for x, y in polyomino)
    max_x = max(x for x, y in polyomino)
    min_y = min(y for x, y in polyomino)
    max_y = max(y for x, y in polyomino)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in polyomino:
                print("■", end=" ")
            else:
                print(" ", end=" ")
        print()


if __name__ == "__main__":
    # Convert the first command-line argument to an integer
    n = (
        int(sys.argv[1]) if len(sys.argv) > 1 else 4
    )  # Default to 4 if no argument provided

    all_polyominoes = generate_polyominoes(n)
    unique_polyominoes = unique_rotations(all_polyominoes)

    print("Number of unique polyominoes up to rotation:", len(unique_polyominoes))
    for i, poly in enumerate(unique_polyominoes[:], start=1):
        print("Unique Polyomino {}:".format(i))
        print_polyomino(poly)
        print()
