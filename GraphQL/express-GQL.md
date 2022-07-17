Install `express` and `express-graphql`.

```
const express = require('express');
const app = express();
// note the capitalization!
const expressGraphQL = require('express-graphql');

// This adds an additional step to see if the incoming request is intended for the graphql route.
// If it is -  that request is handed off to GraphQL. GraphQL will take care of the request
// before handing the response back to Express.
app.use('/graphql', expressGraphQL({
  // this allows us to use the GraphiQL tool to make queries against our development environment
  graphiql: true,
}));

app.listen(5000, () => {
  console.log('Running a GraphQL API server at localhost:5000/graphql');
});
```