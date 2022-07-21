import mongoose, { Schema } from "mongoose";

export const UserSchema = new Schema({
    name: {
        tpye: String,
        required: true
    },
    email: {
        type: String,
        required: true
    },
    password: {
        type: String,
        required: true
    },
    date: {
        type: Date,
        default: Date.now
    },
    posts: [{
        type: Schema.Types.ObjectId,
        ref: "post"
    }]
});
