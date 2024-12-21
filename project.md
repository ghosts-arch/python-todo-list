ajouter une tache [X]
afficher les taches [X]
marquer une tache comme faite ou non [X]
supprimer une tache [X]
stocker les taches dans une base de données [X]

colors :

- green = #90EE90

background_color = #DCE9F2

prompts :

"Je vous demande de procéder à une revue de code d'un projet complet. Veuillez analyser le code source dans son intégralité et identifiez les éléments suivants :

    Erreurs de logique : Cherchez des incohérences ou des erreurs de logique dans le code qui pourraient provoquer des comportements inattendus ou des résultats erronés.
    Performance : Identifiez des points dans le code où des optimisations de performance peuvent être réalisées (par exemple, des boucles inutiles, des calculs répétitifs, ou des ressources non gérées).
    Sécurité : Vérifiez si le code présente des failles de sécurité potentielles (par exemple, injection SQL, XSS, ou mauvaise gestion des données sensibles).
    Lisibilité et style : Analysez la lisibilité du code. Proposez des améliorations pour le rendre plus lisible, maintenable et conforme aux bonnes pratiques de style (par exemple, PEP8 pour Python, ou autre norme pertinente selon le langage utilisé).
    Gestion des erreurs : Vérifiez si le code gère correctement les erreurs et les exceptions. Proposez des améliorations pour rendre la gestion des erreurs plus robuste.
    Modularité et réutilisabilité : Examinez la structure du code pour vérifier s'il est modulaire et réutilisable. Proposez des refactorisations si certaines parties du code pourraient être extraites en fonctions ou classes plus génériques.
    Tests : Vérifiez si des tests unitaires ou d'intégration sont présents. Si non, suggérez des endroits du code où des tests devraient être ajoutés pour améliorer la couverture.
    Documentation : Analysez si le code est correctement documenté (commentaires, docstrings). Suggérez des endroits où des commentaires ou des docstrings pourraient être ajoutés pour rendre le code plus compréhensible.
    Dépréciation et compatibilité : Identifiez les fonctionnalités ou bibliothèques dépréciées dans le code et proposez des solutions pour les remplacer par des alternatives modernes.
    Conventions du framework ou de la bibliothèque : Si le projet utilise un framework ou une bibliothèque spécifique (par exemple, Django, Flask, React), vérifiez que les conventions et bonnes pratiques du framework sont respectées.

Fournissez une analyse détaillée pour chaque point et proposez des solutions ou des améliorations spécifiques."
