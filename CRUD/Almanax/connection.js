const { MongoClient } = require('mongodb');
//const user = "user";
//const pass = "pass";
const ip = "localhost:27017";
const db = "DofusData"
const options = "?maxPoolSize=20";

var uri = `mongodb://${ip}/${db}${options}`;

const client = new MongoClient(uri);

async function run() {
    try {
      // Connect the client to the server
      await client.connect();
      // Establish and verify connection
      //await client.db("admin").command({ ping: 1 });
      console.log("Connected successfully to server");
    } catch (err) {
      console.log(err);
    } finally {
      // Ensures that the client will close when you finish/error
      await client.close();
    }
}
run();//.catch(console.dir);