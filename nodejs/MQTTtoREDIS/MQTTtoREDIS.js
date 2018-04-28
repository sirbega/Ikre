var mqtt = require('mqtt'),url = require('url')
   var client = mqtt.createClient("mqtt://m23.cloudmqtt.com",
   {
       username: "ghvmkrdi",
       password: "sBnqoAfqU-Nt"
   });

   client.on('connect',function()
   {
       client.publish("Hello",function()
       {
           client.end();
       })
   })
