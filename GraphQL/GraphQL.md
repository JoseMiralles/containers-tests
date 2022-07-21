# Resolver Functions

Functions that resolve a part of a GQL query to an object.

GQL
```
query {
    User(id: "awefwaefa") {
        name
        friends(first: 5) {
            name
            age
        }
    }
}
```

Resolvers
```
User(id: String!): User         // Nullable, and returns a User object
name(user: User!): String!      // Non-nullable, and returns a string
age(user: User!): Int!
friends(first: Int, user: User!): [User!]!
```

<br>

# Inline Fragments

Allows to fetch some data based on type.

Example: Fetch the house property only if the character being fetched is a house.

Interface and types:
```
interface Character {
    id: ID!
    name: STring!
}
type Muggle implements Character {
    id: ID!
    name: String!
}
type Wizard implements Character {
    id: ID!
    name: String!
    house: [House]!
}
```
- Only wizards have a house property.

Query:
```
query FindCharacter {
    character(id: 117) {
        name
        ... on Wizard {
            house
        }
    }
}
```

<br>

# Nested Queries

example:

```
query findLuke {
    person(id: "awefwaef") {
        name,
        species {
            name,
            classification,
            population,
            homeWorlds {
                name,
                population
            }
        }
    }
}
```

<br>

# Variables and Directives

```
query findPerson($id: ID, $withSpecies: Boolean!) {
    person(id: $id) {
        name,
        eyeColor,
        species @include(if: $withSpecies) {
            name
        }
    }
}
```

Query variables
```
{
    "id": "awefwea",
    "withSpecies": true
}
```

## @skip

@skip does the oposite of @include.

<br>

# Aliases and Fragments

These are necessary if fetching multiple items of the same type, example:

```
{
    tattoine: planet(id: "awef") {
        name,
        ...
    },
    alderraan: planet(id: "afwaef") {
        name,
        ...
    }
}
```

To avoid having to write multiple planet queries, use a fragment:

```
query ComparePlanets($withTerrains: Boolean!){
    tattoine: planet(id: "awef") {
        ...FindPlanet
    },
    alderraan: planet(id: "afwaef") {
        ...FindPlanet
    }
}

fragment FindPlanet on Planet {
    name,
    diameter,
    gravity,
    terrains @include(if: $withTerrains)
    ...
}
```

<br>

# Mutations

These are create, update, and destroy operations.

Syntax:
```
mutation {
    mutationName(key1: "value1", ...) {
        key1,
        association {
            id,
            name
        }
    }
}
```

<br>

# Object & Scalar Types

In GraphQL, there are two different kinds of types.

1. Scalar types represent concrete units of data. The GraphQL spec has five predefined scalars: as String, Int, Float, Boolean, and ID.

2. Object types have fields that express the properties of that type and are composable. Examples of object types are a User or Post, and all the resources your project may have.

<br>

# Circular References

This is when one type refers to another type which in turn refers back to the first type. This would be an issue since one type will be undeclared when the other is evaluated.

To fix this, assign `fields` to an arrow function.

```
const User = new GraphQLObjectType({
  name: 'User',
  fields: () => ({      // <<<<<<<<<<<<<<<<<<<<<
    id   : { type: GraphQLString },
    email: { type: GraphQLString },
    items: {
      type: new GraphQLList(Item),
      resolve: () => { /* resolve function to get user's items */ }
    },
  })
})
const Item = new GraphQLObjectType({
  name: "Item",
  fields: () => ({      // <<<<<<<<<<<<<<<<<<<<<
    id:        { type: GraphQLString },
    name:      { type: GraphQLString },
    user: {
      type: User,
      resolve: () => { /* resolve function to get user of item */ }
    },
  })
})
```

<br>

# Introspection

GraphQL allows clients to ask a server for information about its schema. GraphQL calls this introspection.

### __schema query, tells the client what it can fetch.
```
query {
  __schema {
    types {
      name
    }
  }
}
```


