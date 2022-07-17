import express from "express";
import {graphqlHTTP} from "express-graphql";
import {buildSchema} from "graphql";

const app = express();

const schema = buildSchema(`
type Query {
    hello: String
}
`);

const root = {
    hello: () => {
        return "Hello!!!!"
    }
}

app.use("/graphql", graphqlHTTP({
    graphiql: true,
    schema,
    rootValue: root
}));

app.listen(5000, ()=> {
    console.log("Running GQL at localhost:5000/graphql.");
});