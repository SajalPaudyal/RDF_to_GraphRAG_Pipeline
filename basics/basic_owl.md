# OWL (Web Ontology Language)

## Introduction

OWL is a language to define "Rules" and "Relationships" between concepts, allowing computers to understand what things are and how they relate to each other, beyond just listing facts.

### Connection with RDF

**RDF (the Data)**: It describes specific things

- Example: "Harry Potter" is a "Book". It has "450 pages".

**OWL (the Rules)**: Describes the categories and logic

- Example: "All books are documents". "If a book is a part of a series, it is called SeriesBook". "A book cannot be an Author" etc.

If we use just RDF we will have a pile of data without understanding their relationships. OWL gives computer the brain to interpret the data and allows us to define

1. **Classes (Categories)**: Defining "Novel" vs "Textbook"
2. **Sub-classes (Hierarchy)**: Stating that "Crime novel" is a "Novel", which is a type of "Book".
3. **Properties(Relationships)**: Defining _written by_ actually means "the book is linked to an Author".
4. **Restrictions (Logic)**: A author must be a "Person" not a "Book".

#### Comparing with SQL

**SQL (Closed World)**: If asked, "Is Mount Everest in France?" and the database does not have a row clearly saying Mount Everest is in Nepal, the answer will be "NO".
**OWL (Closed World)**: If asked the same question and the Knowledge Graph does not explicitly say "Mount Everest is in Nepal" OR "Mount Everest is not in France", we cannot infer that it isn't hence the answer would be "don't know".

This implies the major difference, to say something is false, _it must be explicitly assertive or it must derive a contradiction._

### The Trinity of OWL

1. **Individuals (Instances)** - The actual data (ex. Ernest Hemingway, Apple Inc., Paris, etc.)
2. **Classes (Concepts)** - The categories or types of individuals (ex. Person, Author, Company, City, etc.)
3. **Properties (Relationships)** - How the individuals relate (ex. worksFor, locatedIn, isAuthorOf, etc.)

## The building blocks of OWL

We use the Turtle (.ttl) syntax to define OWL ontologies which is standard for professional ontologist.

1. **Classes and Hierarchies**

It defines taxonomies.

```turtle
:person a owl:Class.
:employee a owl:Class;
    rdfs:subClassOf :person.
```

The above syntax defines the rule of class and subclass relationship. Where a class `employee` is a subclass of class `person`.

2. **Properties (Object vs Data)**

- ObjectProperty: Links two individuals
  _Albert -> **Knows** -> Marie_

- DataProperty: Links an individual to a literal value
  _Albert -> **hasAge** -> "30"_

this relation can be depicted as follows:

```turtle
:knows a owl:ObjectProperty.
:hasAge a owl:DataProperty;
    rdfs:range xsd:integer;
```

3. **Domain and Range**
   They are basic constraints on properties but in owl they act as implications.

- **Domain** - If (X hasAge Y) exists, it infers that X is a person.
- **Range** - If \*(X hasAge Y) exists, it infers Y is an integer.

```turtle
:hasAge rdfs:domain :Person;
        rdfs:range  xsd:integer.
```

### Property Characteristics

Here the property shifts from `labels` to `behaviors`

1. **Functional Properties**
   `Functional` means <ins>one</ins>. An individual can have at most <ins>one</ins> value of this property. For example National Identity Number (in Nepal) or Social Security Number (SSN).

```turtle
:hasSSN a owl:FunctionalProperty.
```

2. **Inverse Functional Property**
   It means `a unique identifier`, where if the functional property of two content/individuals is same, it must be the same individual.

For example: If the SSN for one data Author, and the SSN for another data Person is the same then the Person and the Author is the same individual.

3. **Inverse Properties**
   It defines a two way relationship between data. For example, if X is parentOf Y, then Y is the childOf X.

```turtle
:parentOf a owl:ObjectProperty;
    owl:InverseOf :childOf.
```

4. **Symmetric Properties**
   If A relates to B then B relates to A.

example: Spouse/Siblings

```turtle
:spouse a owl:SymmetricProperties.
```

5. **Transitive Properties**

If A -> B and B -> C then A -> C.

example: partOf, locatedIn, ancestorOf etc.

```turtle
:locatedIn owl:TransitiveProperty.
```

example: If Baneshwor is located in Kathmandu, and Kathmandu is located in Nepal, then Baneshwor is located in Nepal.

### Advanced Expression - Restriction (one of the most important part of OWL)

This is how classes are defined dynamically based on their relationships, rather than just naming them.

1. **Existential Quantification _(someValuesFrom)_**
   A parent is a person who has some child. Meaning that Person hasChild (at least 1)

```turtle

:parent a owl:Class;
    owl:equivalentClass[
        owl:intersectionOf(
            :person
            [
                a owl:Restriction;
                owl:on Property :hasChild;
                owl:someValuesFrom :person
            ]
        )
    ]

```

2. **Universal Quantification _(allValuesFrom)_**

This defines class that relates to a specific type.

- The `only` rule: A vegetarian is a person who `only` eats plants, or `nothing`.

_In open world assumption, we do not know what someone ate for breakfast, lunch, dinner, etc. and hence we cannot assert they are vegetarian._

3. **Cardinality Restrictions**

```turtle
owl:maxCardinality 1
```

At most one similar function.

```turtle
owl:maxCardinality 2
```

At most two similar function.

```turtle
owl:qualifiedCardinality
```

Exactly 3 of type X.

Example: _A monogamist person is the one who has only one spouse._

```turtle
:monogamistPerson a owl:Class;
    rdfs: subClassOf[
        a owl:Restriction;
        owl:onProperty :hasSpouse;
        owl:maxCardinality 1
    ]
```

### Reasoning

1. **Consistency checking**

- Does the ontology contain logical contradiction?

For example: - Class_A is disjoint from Class_B - John is in Class_A - John is in Class_B

    result: Inconsistent ontology, the reasoner will throw an error.

2. **Classification**
   If classes are defined by logic, the reasoner automatically organizes them.

For example:

    - Input: We define `Bachelor` as `Man` who is `Not Married`.
    - Action: We add `Jean` as `Man` and `Not Married`.
    - Inference: The reasoner *automatically classifies* `Jean` as a `Bachelor`.

### Same As and Equivalent

**Same As**
Two individuals are actually the same thing: ex. `JFK` owl:sameAs `John_F_Kennedy`.

**Equivalent To**
Two individuals have exact same members ex. `Humans` owl:equivalentClass `HomoSapiens`.

### Property Chains

The newer version of Owl-2 allows us to infer the relations based on `path`.

If A is a part of B, and B is the part of C, then A is the part of C. We have seen this property previously when we defined transitivity.

But this sort of relations are much more complex in real world problems, which needs chains to define them.

example

    - A hasBrother B
    - B hasFather C

    the relation should infer A hasFather C.

    similarly,
    - A hasFather B
    - B hasBrother C

    the relation like below should be defined that follows the chain, of father and brother making the relation `hasUncle` valid.

```turtle
    :hasUncle a owl:objectProperty;
        owl:propertyChainAxiom(:hasFather :hasBrother )
```

    The property hasUncle is implied to the chain of hasFather, and then hasBrother.


This is the basics of OWL, and we will be using these logics in creating the pipeline. 