var mqtt = require('mqtt');
var options = {
    port: 14388,
    host: 'mqtt://zz',
    clientId: 'vedran',
    username: 'ghvmkrdi',
    password: 'sBnqoAfqU-Nt',
    keepalive: 60,
    reconnectPeriod: 1000,
    protocolId: 'MQIsdp',
    protocolVersion: 3,
    clean: true,
    encoding: 'utf8'
};
var client = mqtt.connect('mqtt://m23.cloudmqtt.com', options);
client.on('connect', function() {
    console.log('connected');
    client.subscribe('ado', function() {
        client.on('message', function(topic, message, packet) {
            console.log("Received '" + message + "' on '" + topic + "'");
        });
    });


    client.publish('hello', 'go away', function() {
        console.log("Message is published");
        client.end();
    });
});
