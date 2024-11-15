# PythonProject
Test Repository: PythonProject

Notizen:

MCTS - Monte Carlo Tree Search Algo...

ToDo:
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
        max_height
        leafs:(List,Array,Map?)
        
    Instanzattribute:
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
-   MCTS_generate_Move (Root: Node)
    	-   Hier wird per Monte Carlo Tree Search der nächste Move (in unserem Beispiel: Node) ausgewählt, den der aktuelle Agent machen soll. Der gewählte Node dient dann als neuer Root, auf dem die Methode aufgerufen wird.
            -   in mcts in agent_mcts in agents (path)
-   Node
    - set_value
        - Berechnet den value des nodes. Ist nötig, um später zu entscheiden, wo weiter simuliert wird. 


Plan
-   Allgemeiner Ablauf
    
    -   Berrechne jeden möglichen Zug vom gewählten node bis ca. tiefe 4 (umso besser hier umso besser gegen die anderen algos der leute)

        - Bestimme bei welchen node du weiter simulieren willst
            - Dafür brauchst du die berrechnung aus dem Monte carlo selection part also Winrate + exploit wurzel oder so (siehe Folien woche 3 oder https://medium.com/@quasimik/monte-carlo-tree-search-applied-to-letterpress-34f41c86e238) 
            - alle leafs anschauen und dann mit der berrechnung entscheiden welchen du verwendest  
   
    -   wähle den mit der besten heuristik (value) als move
        
        - dieser ist dann die neue root, alle siblings / parents verworfen
        - value ist diese schlaue berechnung des nächsten zugs (winrate+c*exploitatio)
    
    -   Zug des gegners abwarten und darauf basierend die noch validen nodes als neue testmenge festsetzen




