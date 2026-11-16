# TestsIA — IA générative appliquée à la qualité logicielle

**Projet de formation | QA fonctionnelle · Python · Prompt engineering · LLM**

Ce dépôt rassemble des travaux pratiques réalisés dans le cadre d'une formation à l'IA générative appliquée aux activités de **Quality Assurance (QA)**. Il explore comment formuler des demandes précises à un modèle de langage, générer des cas de test, évaluer les limites des réponses et intégrer ces traitements dans des scripts Python réutilisables.

Le fil conducteur est simple : **l'IA propose, la QA vérifie**. Les résultats générés ne remplacent ni l'analyse des exigences ni la validation humaine.

## Objectifs du projet

- Concevoir des prompts structurés pour des activités de recette fonctionnelle.
- Générer des scénarios nominaux, des cas limites et des cas d'erreur.
- Améliorer les réponses grâce aux exemples (*few-shot*) et à l'auto-critique.
- Utiliser des API de modèles de langage depuis Python.
- Vérifier automatiquement le format de certaines sorties générées.
- Comprendre les risques d'hallucination, de variabilité et de biais.

## Contenu du dépôt

Les fichiers sont regroupés dans [`atelier-ia/`](atelier-ia/).

| Fichier | Sujet exploré |
| --- | --- |
| [`L2_demo.ipynb`](atelier-ia/L2_demo.ipynb) | Assistant e-commerce ZotoShop : comparer une réponse sans contexte documentaire et une réponse fondée sur une fiche produit. |
| [`L4_atelier_ia.ipynb`](atelier-ia/L4_atelier_ia.ipynb) | Premiers appels à un modèle, installation et vérification de la configuration, génération de cas de test. |
| [`L5_atelier_ia.ipynb`](atelier-ia/L5_atelier_ia.ipynb) | Framework **CREAT** : contexte, rôle, exemple, action et format attendu. |
| [`L6_patterns.ipynb`](atelier-ia/L6_patterns.ipynb) | Techniques de prompting : *zero-shot*, *few-shot*, raisonnement guidé et auto-critique. |
| [`L7_rouages.ipynb`](atelier-ia/L7_rouages.ipynb) | Fonctionnement des LLM : comptage des tokens, consommation et limite de longueur des réponses. |
| [`L8_limites.ipynb`](atelier-ia/L8_limites.ipynb) | Limites des modèles : API inventée, non-déterminisme et biais dans les données générées. |
| [`L9_modeles.ipynb`](atelier-ia/L9_modeles.ipynb) | Comparaison de modèles Anthropic selon la durée de réponse, les tokens et la complexité de la tâche. |
| [`L10_migration.ipynb`](atelier-ia/L10_migration.ipynb) | Passage du prompt conversationnel au script : génération de JSON, assertions et export CSV de cas de test. |
| [`kit_qa_starter.ipynb`](atelier-ia/kit_qa_starter.ipynb) | Trame de départ d'un kit de prompts QA réutilisable. |
| [`kit_qa_starter_OJO.ipynb`](atelier-ia/kit_qa_starter_OJO.ipynb) | Adaptation du kit au domaine de l'**assurance vie** : génération et revue de cas de test pour une souscription en back-office. |
| [`outils_ia.py`](atelier-ia/outils_ia.py) | Fonction `ask()` réutilisable, reposant sur le SDK Google Gen AI et une clé Gemini fournie par variable d'environnement. |
| [`verif.py`](atelier-ia/verif.py) | Script de vérification d'un appel à l'API Anthropic. |

## Focus métier : QA et assurance vie

Dans [`kit_qa_starter_OJO.ipynb`](atelier-ia/kit_qa_starter_OJO.ipynb), les exercices de prompting sont adaptés à un **parcours de souscription de contrat d'assurance vie** dans une application bancaire de back-office.

Le kit vise notamment à :

1. Générer des cas de test à partir d'une fonctionnalité de souscription.
2. Couvrir le scénario nominal, les valeurs limites et les situations d'erreur.
3. Structurer les cas avec les préconditions, étapes, résultats attendus et priorités.
4. Fournir un exemple de cas de test au format métier souhaité.
5. Soumettre une première proposition à une revue critique pour identifier les oublis et compléter la couverture.

Cette démarche illustre un usage de l'IA comme **assistant à la conception de tests**, avec une validation QA indispensable avant toute utilisation opérationnelle.

## Technologies et outils

- **Python** pour les scripts et les vérifications.
- **Jupyter Notebook** pour les exercices interactifs.
- **Google Gemini** via `google-genai` dans `outils_ia.py`.
- **Anthropic Claude** via `anthropic` dans certains notebooks et dans `verif.py`.
- **python-dotenv** pour charger des variables d'environnement.
- **Git / GitHub** pour le versionnement des travaux.

> **Important :** les notebooks reflètent plusieurs étapes de formation et n'utilisent pas tous le même fournisseur de modèle. Certains exercices nécessitent une clé Anthropic, tandis que la fonction `ask()` actuellement présente dans `outils_ia.py` utilise Gemini. Le dépôt constitue un ensemble pédagogique et non une suite de tests intégralement automatisée et validée de bout en bout.

## Installation et utilisation

### 1. Préparer un environnement Python

Depuis la racine du dépôt :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install google-genai anthropic python-dotenv notebook
```

### 2. Configurer les clés API

Créer un fichier `.env` **à la racine du dépôt** et y renseigner uniquement les clés correspondant aux exercices exécutés :

```dotenv
GEMINI_API_KEY=VOTRE_CLE_GEMINI
ANTHROPIC_API_KEY=VOTRE_CLE_ANTHROPIC
```

Le fichier `.env` et le dossier `.venv/` sont exclus du suivi Git par `.gitignore`. **Ne jamais publier de clés API ou de données confidentielles.**

### 3. Ouvrir les notebooks

```powershell
jupyter notebook
```

Ouvrir ensuite les fichiers du dossier `atelier-ia/` et exécuter les cellules nécessaires à l'exercice choisi.

> **Note d'exécution :** plusieurs notebooks importent `outils_ia` depuis leur dossier. Selon le répertoire de lancement, il peut être nécessaire d'ouvrir `atelier-ia/` comme dossier de travail ou d'ajuster le chemin d'import. Les modèles disponibles, leurs noms et les quotas API peuvent également évoluer.

## Bonnes pratiques QA mises en œuvre

- **Traçabilité :** conserver les prompts et les exemples de tests dans des fichiers versionnés.
- **Couverture :** distinguer parcours nominal, cas limites et scénarios d'erreur.
- **Contrôle des sorties :** vérifier la structure JSON et certaines propriétés des cas générés avec des assertions.
- **Relecture critique :** ne pas considérer une réponse de modèle comme une preuve de conformité.
- **Gestion des risques :** identifier les hallucinations, les biais et les variations de résultats.
- **Confidentialité :** séparer les secrets du code source.

## Limites et pistes d'amélioration

Ce dépôt documente un **parcours d'apprentissage**. Il ne démontre pas, à lui seul, une intégration CI/CD opérationnelle ni une automatisation Playwright exécutée en production.

Prochaines pistes possibles : ajouter des jeux d'essai reproductibles, définir des critères d'évaluation des cas générés, isoler les dépendances dans un fichier de configuration, renforcer les contrôles de sécurité et automatiser l'exécution de vérifications sans appel API réel.

## À propos

Projet réalisé dans une démarche de montée en compétences en **QA augmentée par l'IA**, à la croisée de la recette fonctionnelle, de l'analyse métier et des outils d'IA générative.

**Dépôt :** [oliviajohnson3/TestsIA](https://github.com/oliviajohnson3/TestsIA)
