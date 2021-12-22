const { MongoClient } = require('mongodb');

config = {
  host: "localhost:27017",
  db: "Dofus",
  options: "?maxPoolSize=20"
}

const url = `mongodb://${config.host}/${config.db}${config.options}`;

const client = new MongoClient(url);

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