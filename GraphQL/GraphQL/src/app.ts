import express from "express";
import mongoose from "mongoose";
import {graphqlHTTP} from "express-graphql";
import {buildSchema} from "graphql";
// import {schema} from "./schema";
import bodyParser, { BodyParser } from "body-parser";

const app = express();
const connectionString = `mongodb://${process.env.MONGO_INITDB_ROOT_USERNAME}:${process.env.MONGO_INITDB_ROOT_PASSWORD}@${process.env.MONGODB_SERVICE_SERVICE_HOST}:${process.env.MONGODB_SERVICE_SERVICE_PORT}/${process.env.MONGO_INITDB_DATABASE}/retryWrites=true&w=majority`;
// console.log(`CONNECTION_STRING:\T${connectionString}`);

mongoose.connect(connectionString)
    .then(()=>console.log("GQL-EXPRESS CONNECTED TO MONGO"))
    .catch(err => console.log(err));

const root = {
    hello: () => {
        return "Hello!!!!"
    }
}

app.use(bodyParser.json());
// app.use("/graphql", graphqlHTTP({
//     graphiql: true,
//     schema,
//     rootValue: root
// }));

app.listen(5000, ()=> {
    console.log("Running GQL at localhost:5000/graphql.");
});
