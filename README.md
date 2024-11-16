# PythonProject
Test Repository: PythonProject

Notizen:

MCTS - Monte Carlo Tree Search Algo...

ToDo:
-   readme anpassen
-   Schreibe was du für welchen schritt verwenden möchtest
-   Ideen suchen für die verbesserung der Leistung:
    - height Attribute an den erkannt wird wie tief die suche schon ging -> wenn zu viele züge dann ist ein draw sehr wahrscheinlich -> ignoriere diesen subtree absofort
    - weit von einander entferte columns sinnloser als zusammenhängende? -> gewisse züge priorisieren über andere? (column 1 -> 6 -> 3 -> 0 -> 4 ->...., das würde dem anderem eh zu viel zeit geben sich 4 nebeneinander zu bauen und damit brauch man solche fälle nicht immer berechnen (wie viel schlechter wird der Agent dann, im austausch zu wie viel performence?))

Wichtige Klassen (Attribute), Methoden:

Klassen: 
-   Node


Attribute:
-   Node
    Klassenattribute:
        current_root (Der aktuelle Stand des Spiels)
        
    Instanzattribute:#anpassen
        parent
        child
        height
        chosen_column
        win_simulations
        total_simulations
        board
        value
        (...?)

Methoden: 
-   mcts
    - generate_move_mcts (Root: Node)
        - Hier wird per Monte Carlo Tree Search der nächste Move (in unserem Beispiel: Node) ausgewählt, den der aktuelle Agent machen  soll. Der gewählte Node dient dann als neuer Root, auf dem die Methode aufgerufen wird.
            -   in mcts in agent_mcts in agents (path)
    - simulate
        - Simuliert die nächstens paar moves (Erstmal die nächsten 4, irgendwann vielleicht mehr/weniger)
        - muss parent beim erstellen der neu simulierten node hinterlegen
        - muss simulationen und falls ein win kommt win alle parents updaten (win/total_simulations)

-   Node
    - set_value
        - Berechnet den value des nodes. Ist nötig, um später zu entscheiden, wo weiter simuliert wird.
    - update_root_by_board
        - Kriegt das aktuelle Spielbrett und setzt die entsprechende Node als neue root. Wenn es der erste move ist und noch keine Nodes erstellt wurden erstellt es eine Node und stellt diese als neue Root ein. Am ende wird die Node returned.
    
    #nicht richtig wir wollen jeden node ab root testen bis wir an ein leaf kommen un dann ein spiel simulieren folgende muss anders gehen
    - get_leaf_by_best_value    
        - Aus der leaf liste wird die Node mit dem besten value (nach UCT) ausgewählt und returned.


Plan
-   Allgemeiner Ablauf
    
    -   Berrechne jeden möglichen Zug vom gewählten node bis ca. tiefe 4 (umso besser hier umso besser gegen die anderen algos der leute)

        - Bestimme bei welchen node du weiter simulieren willst
            - Dafür brauchst du die berrechnung aus dem Monte carlo selection part also Winrate + exploit wurzel oder so (siehe Folien woche 3 oder https://medium.com/@quasimik/monte-carlo-tree-search-applied-to-letterpress-34f41c86e238) 
            - alle nodes anschauen und dann mit der berrechnung entscheiden welchen du verwendest  
   
    -   wähle den mit der besten heuristik als move (muss noch eine überlegen, wenn 2 gleich gut dann random choose one)
        
        - dieser ist dann die neue root, alle siblings / parents verworfen
        - value ist diese schlaue berechnung des nächsten zugs (winrate+c*exploitatio)
    
    -   Zug des gegners abwarten und darauf basierend die noch validen nodes als neue testmenge festsetzen




