import {GraphQLObjectType, GraphQLString, GraphQLInt, GraphQLSchema, GraphQLNonNull} from "graphql";
import mongoose, { model, Schema } from "mongoose";

// const UserSchema = new Schema({
//     name: {
//         type: String,
//         required: true
//     },
//     email: {
//         type: String,
//         required: true
//     },
//     password: {
//         type: String,
//         required: true
//     },
//     date: {
//         type: Date,
//         default: Date.now
//     },
//     posts: [{
//         type: Schema.Types.ObjectId,
//         ref: "post"
//     }]
// });
// export const userModel = mongoose.model("user", UserSchema);

// const PostSchema = new Schema({
//     title: {
//         type: String,
//         required: true
//     },
//     author: {
//         type: Schema.Types.ObjectId,
//         ref: "user"
//     },
//     body: {
//         type: String,
//         required: true
//     },
//     date: {
//         type: Date,
//         default: Date.now
//     }
// });
// export const PostModel = mongoose.model("post", PostSchema);


// // OBJECTS

// const MountType = new GraphQLObjectType({
//     name: "MountType",
//     fields: {
//         id: { type: GraphQLString },
//         userId: { type: GraphQLString },
//         name: { type: GraphQLString }
//     }
// });

// const UserType = new GraphQLObjectType({
//     name: "UserType",
//     fields: {
//         id: { type: GraphQLString },
//         name: { type: GraphQLString },
//         favoriteNumber: { type: GraphQLInt },
//         mount: {
//             type: MountType,
//             args: {userId: {type: GraphQLString}},
//             resolve: (parentValue, args) => {
//                 return mounts.find(m => m.userId === parentValue.id)
//             }
//         }
//     }
// });

// const RootQuery = new GraphQLObjectType({
//     name: "RootQueryType",
//     fields: {
//         user: {
//             type: UserType,
//             args: {id: {type: GraphQLString}},
//             resolve: (parentValue, args) => {
//                 return users.find(u => u.id === args.id);
//             }
//         }
//     }
// });


// // MUTATIONS

// const mutation = new GraphQLObjectType({
//     name: "Mutation",
//     fields: {
//         newUser: {
//             type: UserType,
//             args: {
//                 name: { type: new GraphQLNonNull(GraphQLString) },
//                 favoriteNumber: { type: new GraphQLNonNull(GraphQLInt) }
//             },
//             resolve(parentValue, { name, favoriteNumber }) {
//                 const newUser = {
//                     id: (users.length * 10).toString(),
//                     name,
//                     favoriteNumber
//                 };
//                 users.push(newUser);
//                 return newUser;
//             }
//         }
//     }
// });

// export const schema = new GraphQLSchema({
//     query: RootQuery,
//     mutation
// });
