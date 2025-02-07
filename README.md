# Simulateur-BFS-DFS
Visualisation interactive des parcours en largeur (BFS) et en profondeur (DFS) implémentée en Python et HTML, permettant d'explorer et d'analyser l'exécution de ces algorithmes sur des graphes.

# Fonctionnalités
- Simulation des parcours BFS et DFS sur un graphe.
- Visualisation des contenus de la pile et file lors du parcours ainsi que les sommets visités à chaque itération.

# Structure du Projet
- index.html : Fichier contenant l'interface utilisateur.
- server.py : Contient le backend du projet, utilisant Flask pour servir l'API et gérer les requêtes pour l'exécution des algorithmes.
- Pays.json : Fichier de données JSON contenant les nœuds et les liens du graphe représentant les relations de frontières entre certains pays d'Afrique du Nord.

# Prérequis
- Navigateur internet.
- Python version 3.x.
- Les packages : flask_cors & flask.

# Note
- Pour exécuter le projet, saisissez la commande `python -m http.server` dans votre terminal.
- Ouvrez l'URL `http://localhost:8000` dans votre navigateur internet.
- Ouvrez un deuxième terminal en même temps et saisissez la commande `python server.py` pour lancer le backend du projet.
