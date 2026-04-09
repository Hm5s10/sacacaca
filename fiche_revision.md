# Fiche de révision — MAP (Maths, Algo, Programmation C)

> **Convention** : 🔵 Définition | 🟢 Comment démontrer | 🔴 Contre-exemple type | 💡 Piège classique

---

# PARTIE 1 — ALGÈBRE

---

## 1.1 Loi de composition interne (LCI)

🔵 **Définition**
Une fonction ★ : E × E → E est une **loi de composition interne** sur E si et seulement si :
∀ x, y ∈ E, x ★ y ∈ E (le résultat reste dans E — on dit que E est **stable** par ★).

🟢 **Comment démontrer que ★ est une LCI sur E**
1. Prendre deux éléments quelconques x, y ∈ E (les définir explicitement).
2. Calculer x ★ y.
3. Montrer que le résultat appartient bien à E.

**Exemple :** + est-elle une LCI sur 2Z (les entiers pairs) ?
Soient x = 2a et y = 2b avec a,b ∈ Z. Alors x + y = 2(a+b) ∈ 2Z. ✓

🔴 **Contre-exemple type**
La soustraction n'est pas une LCI sur N : 3 − 5 = −2 ∉ N.
La concaténation · n'est pas une LCI sur les mots de Fibonacci F : "01" · "10" = "0110" ∉ F (contient "11").

💡 **Piège** : ne pas confondre LCI (résultat dans E) et LCE (loi de composition externe, résultat éventuellement hors de E).

---

## 1.2 Propriétés algébriques

🔵 **Associativité**
★ est associative si ∀ x, y, z ∈ E : (x ★ y) ★ z = x ★ (y ★ z).

🟢 **Comment démontrer**
Prendre x, y, z quelconques, calculer les deux membres et vérifier l'égalité.
Pour la **non-associativité**, un seul contre-exemple suffit.

🔴 **Contre-exemple** : la soustraction : (5−3)−1 = 1 ≠ 5−(3−1) = 3.

🔵 **Commutativité**
★ est commutative si ∀ x, y ∈ E : x ★ y = y ★ x.

🔴 **Contre-exemple** : la concaténation : "ab" · "c" = "abc" ≠ "c" · "ab" = "cab".

🔵 **Élément neutre**
e est neutre pour ★ si ∀ x ∈ E : e ★ x = x ★ e = x.

🟢 **Comment trouver l'élément neutre**
Poser e ★ x = x, résoudre pour e. Vérifier aussi x ★ e = x.
**L'élément neutre est unique** (preuve : si e et e' sont neutres, e = e ★ e' = e').

🔵 **Symétrique (inverse)**
x' est le symétrique de x si x ★ x' = x' ★ x = e.

🟢 **Comment trouver le symétrique**
Poser x ★ x' = e, résoudre. Vérifier que x' ∈ E.

🔴 **Contre-exemple d'existence** : dans (N, +), 3 n'a pas de symétrique car −3 ∉ N.

---

## 1.3 Monoïde

🔵 **Définition**
(E, ★) est un **monoïde** si :
1. ★ est une LCI sur E.
2. ★ est **associative**.
3. Il existe un **élément neutre** e ∈ E.

🟢 **Plan de démonstration standard**
1. LCI : montrer que E est stable par ★.
2. Associativité : calculer (x★y)★z = x★(y★z).
3. Neutre : exhiber e, vérifier e★x = x★e = x pour tout x.

**Exemple : (Σ\*, ·) est un monoïde**
- LCI : concaténer deux mots donne un mot. ✓
- Associativité : (u·v)·w = u·(v·w) = uvw. ✓
- Neutre : ε (mot vide), ε·u = u·ε = u. ✓

🔴 **Ce qui empêche d'être un monoïde**
- Pas de neutre : (N\*, ×) n'a pas de neutre si 1 ∉ N\* — attention, ici 1 ∈ N\* donc c'est bon, mais (2Z, ×) n'a pas de neutre car 1 ∉ 2Z.
- Pas associatif : tout exemple de non-associativité.

---

## 1.4 Groupe

🔵 **Définition**
(E, ★) est un **groupe** si :
1. C'est un monoïde (LCI + associatif + neutre).
2. Tout élément admet un **symétrique** dans E.

(E, ★) est un **groupe abélien** si de plus ★ est commutative.

🟢 **Plan de démonstration**
1. Montrer que c'est un monoïde (voir ci-dessus).
2. Prendre x ∈ E quelconque, exhiber son symétrique x' ∈ E, vérifier x★x' = x'★x = e.

**Exemple : (Z, +) est un groupe**
- Monoïde : LCI ✓, associatif ✓, neutre 0 ✓.
- Symétrique de x : −x ∈ Z ✓.

🔴 **Ce qui empêche d'être un groupe**
(N, +) n'est pas un groupe : 3 n'a pas de symétrique dans N (−3 ∉ N).
(Z, ×) n'est pas un groupe : 2 n'a pas de symétrique (1/2 ∉ Z).

💡 **Piège** : bien vérifier que le symétrique reste dans E (pas juste qu'il existe dans un ensemble plus grand).

---

## 1.5 Monoïde libre

🔵 **Définition**
Le **monoïde libre** engendré par un alphabet Σ est (Σ\*, ·), où Σ\* est l'ensemble de tous les mots finis sur Σ. C'est le monoïde le plus général qu'on peut former avec Σ : il n'y a aucune relation supplémentaire entre les lettres.

🔵 **Base d'un monoïde libre**
Un ensemble B est une **base** (= ensemble générateur libre) de M si :
- Tout élément de M s'écrit de manière **unique** comme produit d'éléments de B.

🟢 **Comment montrer qu'un ensemble est une base**
Montrer l'existence et l'unicité de la décomposition.

🔴 **Contre-exemple** : {4, 5} engendre P\* = {4,5,8,9,10,12,13,...} ⊂ N. Mais ce n'est pas une base car 20 = 4+4+4+4+4 = 4+4+4+8 = ... (décompositions non uniques).

---

## 1.6 Morphisme de monoïde / de groupe

🔵 **Définition — Morphisme de monoïde**
f : (E, ★) → (F, ●) est un **morphisme de monoïde** si :
1. ∀ x, y ∈ E : f(x ★ y) = f(x) ● f(y). (compatible avec la loi)
2. f(e_E) = e_F. (envoie le neutre sur le neutre)

🔵 **Morphisme de groupe**
Même condition 1 seulement (la condition 2 est automatique pour les groupes).

🟢 **Plan de démonstration**
1. Prendre x, y ∈ E quelconques.
2. Calculer f(x ★ y).
3. Calculer f(x) ● f(y).
4. Vérifier l'égalité.
5. Vérifier f(e_E) = e_F (pour les monoïdes).

**Exemple : f : (2Z,+) → (3Z,+), f(x) = 3x/2**
- f est bien définie : si x ∈ 2Z, x = 2k, f(x) = 3k ∈ 3Z. ✓
- f(x+y) = 3(x+y)/2 = 3x/2 + 3y/2 = f(x) + f(y). ✓
- f(0) = 0. ✓ → morphisme de groupe.

🔴 **Contre-exemple de morphisme** : f : (R,+) → (R,×), f(x) = x² + 1.
f(x+y) = (x+y)² + 1 ≠ (x²+1)(y²+1) en général. Pas un morphisme.

---

## 1.7 Injection, Surjection, Bijection

🔵 **Définitions**
- f est **injective** : ∀ x, y, f(x) = f(y) ⟹ x = y. (pas deux antécédents pour une même image)
- f est **surjective** : ∀ y ∈ F, ∃ x ∈ E, f(x) = y. (tout élément de F a un antécédent)
- f est **bijective** : injective ET surjective.

🟢 **Comment démontrer l'injectivité**
Méthode directe : supposer f(x) = f(y), puis montrer x = y.
Méthode contraposée : supposer x ≠ y, montrer f(x) ≠ f(y).

🟢 **Comment démontrer la surjectivité**
Prendre y ∈ F quelconque. Résoudre f(x) = y pour trouver x ∈ E. Vérifier que cet x appartient bien à E.

🔴 **Contre-exemple d'injectivité** : f : Z → N, f(x) = x². Pas injective : f(2) = f(−2) = 4.
🔴 **Contre-exemple de surjectivité** : f : N → N, f(x) = 2x. Pas surjective : 3 n'a pas d'antécédent.

🔵 **Isomorphisme**
Un morphisme bijectif est un **isomorphisme**. Si E = F, c'est un **automorphisme**.

🟢 **Plan pour montrer qu'un morphisme est un isomorphisme**
1. Montrer que c'est un morphisme (voir 1.6).
2. Montrer l'injectivité.
3. Montrer la surjectivité.

---

## 1.8 Permutations

🔵 **Définition**
Une **permutation** de taille n est une bijection σ : {1,...,n} → {1,...,n}.
On note Sn l'ensemble des permutations de taille n.

Notation matricielle : σ = ( 1 2 3 / σ(1) σ(2) σ(3) ).

🔵 **Composition de permutations**
(π ∘ μ)(i) = π(μ(i)) — on applique d'abord μ, puis π.

🟢 **Comment montrer que (Sn, ∘) est un groupe**
1. LCI : composée de deux bijections est une bijection. ✓
2. Associativité : composition de fonctions est toujours associative. ✓
3. Neutre : identité id(i) = i. ✓
4. Symétrique : toute bijection est inversible, et l'inverse d'une permutation est une permutation. ✓

🔵 **Matrice de permutation**
permat(σ) = matrice M où M[i][j] = 1 si σ(i) = j, 0 sinon.
Chaque ligne et colonne contient exactement un 1.

---

# PARTIE 2 — RELATIONS

---

## 2.1 Relation binaire

🔵 **Définition**
Une **relation** R sur E est un sous-ensemble de E × E. On note xRy pour (x,y) ∈ R.

---

## 2.2 Relation d'équivalence

🔵 **Définition**
R est une **relation d'équivalence** sur E si elle est :
1. **Réflexive** : ∀ x ∈ E, xRx.
2. **Symétrique** : ∀ x, y ∈ E, xRy ⟹ yRx.
3. **Transitive** : ∀ x, y, z ∈ E, xRy et yRz ⟹ xRz.

🟢 **Plan de démonstration**
Vérifier les trois propriétés séparément, une par une, avec des éléments quelconques.

**Exemple : "être codé sur le même nombre de bits" sur N\{0}**
Rappel : nb_bits(n) = ⌊log₂(n)⌋ + 1.
- Réflexive : nb_bits(n) = nb_bits(n). ✓
- Symétrique : si nb_bits(x) = nb_bits(y), alors nb_bits(y) = nb_bits(x). ✓
- Transitive : si nb_bits(x)=nb_bits(y) et nb_bits(y)=nb_bits(z), alors nb_bits(x)=nb_bits(z). ✓

🔴 **Contre-exemple type (non-transitive)** : "être voisins directs" sur une liste n'est pas transitive.
🔴 **Contre-exemple (non-symétrique)** : < sur Z.

---

## 2.3 Relation d'ordre

🔵 **Définition**
R est une **relation d'ordre** sur E si elle est :
1. **Réflexive** : ∀ x, xRx.
2. **Antisymétrique** : ∀ x, y, xRy et yRx ⟹ x = y.
3. **Transitive** : ∀ x, y, z, xRy et yRz ⟹ xRz.

**Ordre partiel** : il peut exister x, y non comparables (ni xRy ni yRx).
**Ordre total** : ∀ x, y, xRy ou yRx (tous les éléments sont comparables).

🟢 **Plan de démonstration (ordre)**
1. **Réflexivité** : prendre x quelconque, montrer xRx.
2. **Antisymétrie** : supposer xRy ET yRx, montrer x = y.
3. **Transitivité** : supposer xRy ET yRz, montrer xRz.

**Exemple classique : h(t₁) < h(t₂) ou t₁ = t₂ sur les arbres**
- Réflexive : t = t, donc t ⪯ t. ✓
- Antisymétrique : t₁ ⪯ t₂ et t₂ ⪯ t₁ signifie h(t₁)<h(t₂) ou t₁=t₂, ET h(t₂)<h(t₁) ou t₂=t₁. La seule possibilité cohérente est t₁ = t₂. ✓
- Transitive : si h(t₁)<h(t₂) et h(t₂)<h(t₃), alors h(t₁)<h(t₃). ✓

🔴 **Contre-exemple d'antisymétrie** : "avoir le même nombre de lettres ou plus" n'est pas antisymétrique : "ab" R "ba" et "ba" R "ab" mais "ab" ≠ "ba".

💡 **Différence relation d'ordre / équivalence** : l'ordre est **antisymétrique**, l'équivalence est **symétrique**.

---

## 2.4 Diagramme de Hasse

🔵 **Définition**
Représentation graphique d'un ordre partiel où :
- Les éléments sont des nœuds.
- On trace un arc de x vers y (y au-dessus) si x ⪯ y et il n'existe pas z tel que x ⪯ z ⪯ y (couvrance directe).
- On ne trace pas les arcs "évidents" par transitivité ou réflexivité.

🟢 **Comment le construire**
1. Lister toutes les paires (x, y) avec x ⪯ y.
2. Éliminer les paires déduites par transitivité (si x⪯y et y⪯z, ne pas tracer x→z directement).
3. Placer les éléments minimaux en bas, maximaux en haut.

---

# PARTIE 3 — APPLICATIONS ET FONCTIONS

---

## 3.1 Application vs Relation

🔵 **Application**
f : E → F est une **application** si tout élément de E a **exactement un** image dans F.
= f est bien définie (définie partout, et résultat unique).

🟢 **Comment vérifier qu'une fonction C est une application**
1. Est-elle définie pour toutes les entrées valides ? (pas de cas non traités)
2. Retourne-t-elle toujours une valeur unique ? (pas d'indéterminisme)

**Exemple : hauteur d'un arbre**
h est une application de T vers Z car tout arbre a une hauteur unique bien définie (−1, 0, ou max récursif).

---

# PARTIE 4 — ALGORITHMIQUE ET COMPLEXITÉ

---

## 4.1 Complexité en temps

🔵 **Définition**
La **complexité en temps** est le nombre d'opérations élémentaires effectuées en fonction de la taille de l'entrée n.

🔵 **Notations**
- O(f(n)) : borne supérieure (pire des cas ou ordre de grandeur).
- Ω(f(n)) : borne inférieure (meilleur des cas).
- Θ(f(n)) : borne exacte (les deux à la fois).

🟢 **Comment calculer la complexité**
- **Boucle simple** de 0 à n : O(n).
- **Boucles imbriquées** : multiplier les bornes → O(n²) pour deux boucles de 0 à n.
- **Récursion** : écrire l'équation de récurrence, la résoudre.
  - T(n) = T(n−1) + O(1) → O(n).
  - T(n) = T(n/2) + O(1) → O(log n) (Master Theorem).
  - T(n) = 2T(n/2) + O(n) → O(n log n).

**Exemple : recherche naïve de motif**
Texte de longueur n, motif de longueur m.
- Boucle externe : n−m+1 itérations.
- Boucle interne : jusqu'à m comparaisons.
→ O((n−m+1)·m) = O(n·m) dans le pire des cas.

---

## 4.2 Complexité en espace

🔵 **Définition**
Quantité de **mémoire supplémentaire** utilisée (hors entrée).

🟢 **Comment calculer**
- Variables locales : O(1) chacune.
- Tableau de taille n : O(n).
- Récursion de profondeur p : O(p) (pile d'appel).
- Itératif avec quelques variables : O(1).

**Exemple : itérateur Fibonacci**
next() utilise 3 variables (a, b, tmp) → O(1) en temps ET espace.
Afficher tous les F(n) pour 1 ≤ n ≤ max : O(max) en temps, O(1) en espace.

---

## 4.3 Itérateurs en C

🔵 **Définition**
Un **itérateur** est une structure qui permet de parcourir une séquence sans la stocker entièrement. Il expose typiquement :
- `init(...)` : initialise l'état.
- `has_next(...)` : retourne 1 s'il reste des éléments.
- `next(...)` : retourne le prochain élément et avance l'état.

🟢 **Structure type en C**

```c
typedef struct {
    long long a, b;  /* état courant */
    int n, max;
} IterFib;

void init(IterFib *it, int max) {
    it->a = 0; it->b = 1; it->n = 1; it->max = max;
}

int has_next(IterFib *it) {
    return it->n <= it->max;
}

long long next(IterFib *it) {
    long long val = it->b;
    long long tmp = it->a + it->b;
    it->a = it->b;
    it->b = tmp;
    it->n++;
    return val;
}
```

💡 **Piège** : next() doit être O(1) en temps ET espace. Ne jamais recalculer depuis le début.

---

## 4.4 Trace de pile d'appel

🔵 **Définition**
La **pile d'appel** est la structure LIFO qui stocke les frames d'exécution de chaque appel de fonction. Chaque frame contient les paramètres et variables locales.

🟢 **Comment faire une trace**

Pour chaque appel :
1. Empiler : noter tous les paramètres et variables locales.
2. Évaluer : exécuter le corps de la fonction.
3. Si appel récursif : empiler un nouveau frame, exécuter, dépiler, continuer.
4. Dépiler : noter la valeur de retour.

**Format recommandé :**
```
APPEL cherche(texte, motif, i=0, j=0, n=6, m=2, occ=0)
  texte[0+0]='0' == motif[0]='0' → vrai
  APPEL cherche(..., i=0, j=1, ..., occ=0)
    texte[0+1]='1' == motif[1]='1' → vrai
    APPEL cherche(..., i=0, j=2, ..., occ=0)
      j==m → APPEL cherche(..., i=0, j=0, ..., occ=1)
      ...
    RETOUR ...
  RETOUR ...
RETOUR 2
```

💡 **Pièges fréquents**
- Les pointeurs : `*p1 = valeur` modifie la variable pointée, pas le pointeur.
- Les tableaux passés en paramètre sont passés par **référence** implicite en C.
- Bien distinguer les variables locales (dans le frame) et les variables globales/partagées.

---

## 4.5 Récursif ↔ Itératif

🟢 **Transformer récursif → itératif**

**Récursion terminale** (le résultat est retourné directement sans opération après l'appel récursif) :
→ Remplacer par une boucle while, les paramètres deviennent des variables.

```c
/* Récursif terminal */
int cherche_rec(char *t, char *m, int i, int j, int n, int mp, int occ) {
    if (i >= n) return occ;
    if (j == mp) return cherche_rec(t, m, i, 0, n, mp, occ+1);
    if (t[i+j] == m[j]) return cherche_rec(t, m, i, j+1, n, mp, occ);
    return cherche_rec(t, m, i+1, 0, n, mp, occ);
}

/* Version itérative */
int cherche_iter(char *t, char *m, int n, int mp) {
    int i = 0, j = 0, occ = 0;
    while (i < n) {
        if (j == mp) { occ++; j = 0; }
        else if (t[i+j] == m[j]) { j++; }
        else { i++; j = 0; }
    }
    return occ;
}
```

**Récursion non terminale** : utiliser une pile explicite.

💡 **Avantage de l'itératif** : complexité espace O(1) vs O(profondeur) pour le récursif.

---

## 4.6 Arbres en C

🔵 **Arbre binaire**

```c
typedef struct noeud {
    int valeur;
    struct noeud *gauche;
    struct noeud *droit;
} Noeud;

typedef Noeud* Arbre;
```

🔵 **Arbre ternaire**

```c
typedef struct noeud_ter {
    int valeur;
    struct noeud_ter *gauche;
    struct noeud_ter *milieu;
    struct noeud_ter *droit;
} NoeudTer;

typedef NoeudTer* ArbreTer;
```

🔵 **Hauteur (avec contrat)**

```c
/*
 * Précondition : t est un arbre ternaire valide (NULL ou pointeur valide)
 * Postcondition : retourne -1 si t est vide, 0 si feuille,
 *                 max(h(gauche), h(milieu), h(droit)) + 1 sinon
 */
int hauteur(ArbreTer t) {
    if (t == NULL) return -1;
    if (t->gauche == NULL && t->milieu == NULL && t->droit == NULL)
        return 0;
    int hg = hauteur(t->gauche);
    int hm = hauteur(t->milieu);
    int hd = hauteur(t->droit);
    int max = hg > hm ? hg : hm;
    return (max > hd ? max : hd) + 1;
}
```

---

## 4.7 Recherche de motif naïve

🔵 **Principe**
Tester le motif à chaque position possible du texte.

```c
int naif(char *texte, char *motif, int n, int m) {
    int occ = 0;
    for (int i = 0; i <= n - m; i++) {
        int j = 0;
        while (j < m && texte[i+j] == motif[j]) j++;
        if (j == m) occ++;
    }
    return occ;
}
```

- Complexité temps : O(n·m) pire des cas.
- Complexité espace : O(1) (pas de mémoire supplémentaire).

---

# PARTIE 5 — CHAÎNES DE MARKOV (bonus)

---

🔵 **Définition**
Une **chaîne de Markov** (Xₜ) est un processus stochastique tel que le futur ne dépend du passé qu'à travers le présent : P(Xₜ₊₁ = j | Xₜ = i, Xₜ₋₁, ...) = P(Xₜ₊₁ = j | Xₜ = i).

🔵 **Matrice de transition**
P = matrice où P[i][j] = probabilité de passer de l'état i à l'état j.
Propriété : chaque ligne somme à 1.

🔵 **Distribution à l'instant t**
πₜ = π₀ · Pᵗ (vecteur ligne × matrice).

🔵 **Irréductibilité**
La chaîne est **irréductible** si on peut aller de tout état à tout état (graphe fortement connexe).

🔵 **Apériodicité**
Un état i est **apériodique** si son PGCD de retour vaut 1 (pas de cycle obligatoire de période fixe).

🟢 **Conclusion ergodique**
Si la chaîne est irréductible ET apériodique → il existe une **distribution stationnaire** π unique telle que π = π·P, et πₜ → π quelle que soit la distribution initiale.

---

# PARTIE 6 — AIDE-MÉMOIRE RAPIDE

---

## Hiérarchie des structures algébriques

```
Magma
  └─ Loi interne
Semi-groupe
  └─ + Associativité
Monoïde
  └─ + Élément neutre
Groupe
  └─ + Symétrique pour tout élément
Groupe abélien
  └─ + Commutativité
```

## Hiérarchie des applications

```
Application : tout élément de E a exactement une image
  └─ Injective : images distinctes (pas de collision)
  └─ Surjective : tout élément de F est atteint
  └─ Bijective = injective + surjective
       └─ Morphisme bijectif = Isomorphisme
       └─ Isomorphisme E→E = Automorphisme
```

## Complexités usuelles

| Structure | Temps | Espace |
|---|---|---|
| Boucle simple | O(n) | O(1) |
| Boucles imbriquées (×2) | O(n²) | O(1) |
| Récursion terminale profondeur n | O(n) | O(n) pile |
| Itérateur next() | O(1) | O(1) |
| Recherche motif naïve | O(n·m) | O(1) |
| Hauteur arbre (récursif) | O(n nœuds) | O(h hauteur) |

## Checklist démonstration morphisme isomorphisme

- [ ] f est bien définie (le résultat est dans le bon ensemble)
- [ ] f(x ★ y) = f(x) ● f(y) pour tous x, y
- [ ] f(neutre_E) = neutre_F
- [ ] f est injective (f(x)=f(y) ⟹ x=y)
- [ ] f est surjective (∀y ∈ F, ∃x ∈ E, f(x)=y)

## Checklist relation d'ordre

- [ ] Réflexive : x ⪯ x
- [ ] Antisymétrique : x⪯y et y⪯x ⟹ x=y
- [ ] Transitive : x⪯y et y⪯z ⟹ x⪯z

## Checklist relation d'équivalence

- [ ] Réflexive : xRx
- [ ] Symétrique : xRy ⟹ yRx
- [ ] Transitive : xRy et yRz ⟹ xRz
