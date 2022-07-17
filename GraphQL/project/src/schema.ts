import {GraphQLObjectType, GraphQLString, GraphQLInt, GraphQLSchema} from "graphql";

const users = [
    {id: "12312fawfwa", name: "Jose Miralles", favoriteNumber: 3},
    {id: "afefaw23f", name: "Luchentio", favoriteNumber: 4},
];

const mounts = [
    {id: "awfewfa", userId: "12312fawfwa", name: "Odie"},
    {id: "fwefwafwafwe", userId: "afefaw23f", name: "Honda Civic"},
]

const MountType = new GraphQLObjectType({
    name: "MountType",
    fields: {
        id: { type: GraphQLString },
        userId: { type: GraphQLString },
        name: { type: GraphQLString }
    }
});

const UserType = new GraphQLObjectType({
    name: "UserType",
    fields: {
        id: { type: GraphQLString },
        name: { type: GraphQLString },
        favoriteNumber: { type: GraphQLInt },
        mount: {
            type: MountType,
            args: {userId: {type: GraphQLString}},
            resolve: (parentValue, args) => {
                return mounts.find(m => m.userId === parentValue.id)
            }
        }
    }
});

const RootQuery = new GraphQLObjectType({
    name: "RootQueryType",
    fields: {
        user: {
            type: UserType,
            args: {id: {type: GraphQLString}},
            resolve: (parentValue, args) => {
                return users.find(u => u.id === args.id);
            }
        }
    }
});

const schema = new GraphQLSchema({ query: RootQuery });

export default schema;
