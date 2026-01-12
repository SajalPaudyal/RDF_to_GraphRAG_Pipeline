# Protégé introduction and Basics 

This is what we want to create in protégé for creating an OWL ontology.

Thing
  ├── Book
  ├── Genre
  ├── Language
  └── Person
       └── Author


## Step 1: Verify the base IRI
Before starting to create any class we need to set a base IRI.

our IRI is 
```text
http://www.semanticweb.org/sajalpaudyal/ontologies/2026/lemonde100
```

## Creating a Class

owl:Thing is the **root** of the ontology. Every single class we create should eventually track back to owl:Thing. 

**Top level class - Book**

This is the class that sits under owl:Thing

- Go to *Entities* tab -> *Classes* 
- In the class hierarchy on the left, click on owl:Thing and click **Add Class** button under the toolbar.
- A new class will appear in a box, and rename class to *Books*.

We will then have 

owl:Thing
  └── Book

Similarly create other three classes **Genre, Language,** and **Person**.

## Creating a SubClass

Now we create the hierarchy where Author ill be the subClass under Person.

- Click on *Person* under the *owl:Thing* *Entities* -> *Classes* 
- Click **Add Subclass** which appears on the tab bar similar to *Add Class*
- On the popup that appears rename the new subclass to *Author*.


