# Exemple de soumission d'activité

ÉTS - LOG430 - Architecture logicielle - Automne 2027

Étudiant(e) : Christine Yang-Dai

# Questions

(Il est obligatoire d'ajouter du code, des captures d'écran ou des sorties de terminal pour illustrer chacune de vos réponses.)

## 1. Si l'un des tests échoue à cause d'un bug, comment pytest signale-t-il l'erreur et aide-t-il à la localiser ? Rédigez un test qui provoque volontairement une erreur, puis montrez la sortie du terminal obtenue.

Un message d'échec est affiché, avec une description de l'erreur au sein de la fonction fautive. De plus, un résumé est imprimer, spécifiant le test qui a échoué de même que le fichier de test.
![Capture d'écran de la sortie du terminal](docs\rapport\question1.png)

## 2. Que fait GitHub pendant les étapes de « setup » et « checkout » ? Veuillez inclure la sortie du terminal GitHub CI dans votre réponse.

Dans l'étape setup, GitHub prépare la machine virtuelle pour l'exécution du workflow. Dans l'étape checkout, il clone le dépôt dans le runner pour l'exécution des prochaines étapes du workflow.
![Capture d'écran de l'étape setup](docs\rapport\setup.png)
![Capture d'écran de l'étape checkout](docs\rapport\checkout.png)

## 3. Quel type d'informations pouvez-vous obtenir via la commande `top` ? Veuillez donner quelques exemples. Veuillez inclure la sortie du terminal dans votre réponse.

Réponse

# Déploiement

(Le cas échéant, décrivez votre pipeline CI/CD et ce que vous avez appris dans ce laboratoire en ce qui concerne le déploiement. Il est obligatoire d'ajouter du code, des captures d'écran ou des sorties de terminal pour illustrer votre réponse.)
