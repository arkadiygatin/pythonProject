my_list = [(3 + 5),
           2.2,
           True,
           'words',
           [2,5],
           (2, 67, 3.9),
           {5: 'five'},
           {5, 6},
           frozenset(),
           range(54),
           b'twelve',
           bytearray(b' thirteen'),
           zip(*[(14, 15), (16, 17), ('a', 'b')]),
           TypeError]

for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")
