# Rapport du laboratoire 0

ÉTS - LOG430 - Architecture logicielle - Automne 2026

Étudiant(e) : Hugo Barou, Amélie Lemay, Martin Simon, Christine Yang-Dai

# Questions

## 1. Si l'un des tests échoue à cause d'un bug, comment pytest signale-t-il l'erreur et aide-t-il à la localiser ? Rédigez un test qui provoque volontairement une erreur, puis montrez la sortie du terminal obtenue.

Un message d'échec est affiché, avec une description de l'erreur au sein de la fonction fautive. De plus, un résumé est imprimé, spécifiant le test qui a échoué de même que le fichier de test.

Pour illustrer ceci, un nouveau test `test_add_failure` a été créé dans lequel une assertion fausse est vérifiée.

![Capture d'écran de la sortie du terminal](docs\rapport\question1.png)

## 2. Que fait GitHub pendant les étapes de « setup » et « checkout » ? Veuillez inclure la sortie du terminal GitHub CI dans votre réponse.

Dans l'étape setup, GitHub prépare la machine virtuelle pour l'exécution du workflow.

Les journaux donnent des informations sur cette machine, notamment qu'il s'agisse d'une `Ubuntu 24.04.5 LTS`, avec une image `ubuntu-24.04`, situé dans la région Azure `centralus`. Le runner, version `2.337.0`, exécute les commandes du workflow. Puis, GitHub configure les permissions du `GITHUB_TOKEN`, les secrets venant de `GitHub Actions Secrets` et l'autorisation à écrire dans le système de cache. Il prépare ensuite le répertoire du workflow et les actions nécessaires. Ici, il en trouve trois, qu'il télécharge. Finalement, il identifie le nom du job (`publish`) tel que déterminé dans ![cd.yml](.github\workflows\cd.yml)

![Capture d'écran de l'étape setup](docs\rapport\setup.png)

Dans l'étape checkout, il clone le dépôt dans le runner pour l'exécution des prochaines étapes du workflow.

D'abord, l'actions `actions/checkout@v4` utilise le `GITHUB_TOKEN` pour s'authentifier et créer le dépôt dans `/home/runner/work/log430-labo0-A26/log430-labo0-A26` Il va ensuite configurer le dépôt (initialisation et authentification).

![Capture d'écran de l'étape checkout, partie 1](docs\rapport\checkout-1.png)

Il va alors récupérer (`fetch`) le dernier commit fait sur le main (`--depth=1`). Avec `checkout`, il place les fichiers du commit dans le workspace pour y exécuter les étapes suivantes.

![Capture d'écran de l'étape checkout, partie 2](docs\rapport\checkout-2.png)

## 3. Quel type d'informations pouvez-vous obtenir via les commandes `docker stats` et `top` ? Veuillez donner quelques exemples et expliquer la différence entre ce que chacune vous montre. Veuillez inclure la sortie du terminal dans votre réponse.

La capture d'écran suivante montre le résultat de la commande `top`.

![Capture d'écran du résultat de la commande top](docs\rapport\docker-top.png)

# Déploiement

(Le cas échéant, décrivez votre pipeline CI/CD et ce que vous avez appris dans ce laboratoire en ce qui concerne le déploiement. Il est obligatoire d'ajouter du code, des captures d'écran ou des sorties de terminal pour illustrer votre réponse.)
