# PythonProject
Test Repository: PythonProject

Notizen für mich:

MCTS - Monte Carlo Tree Search Algo...

ToDo:
-   Ideen suchen für die verbesserung der Leistung:
    - height Attribute an den erkannt wird wie tief die suche schon ging -> wenn zu viele züge dann ist ein draw sehr wahrscheinlich -> ignoriere diesen subtree absofort
    - weit von einander entferte columns sinnloser als zusammenhängende? -> gewisse züge priorisieren über andere? (column 1 -> 6 -> 3 -> 0 -> 4 ->...., das würde dem anderem eh zu viel zeit geben sich 4 nebeneinander zu bauen und damit brauch man solche fälle nicht immer berechnen (wie viel schlechter wird der Agent dann, im austausch zu wie viel performence?))
    -mittig im spielbrett mehr möglichkeiten -> diese züge bevorzugen??