n=int(input())
arr = [input() for s in range(n)]
poly= {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}
total=sum(poly[key] for key in arr)
print(total)
