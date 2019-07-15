Sensors = new Mongo.Collection("sensors");
if (Meteor.isClient) {
  Meteor.subscribe("sensorsTopic");
}
if (Meteor.isServer) {
  Meteor.publish("sensorsTopic", function() {
    // only publish when logged-in users request publishing
    if (this.userId) {
      return [Sensors.find()];
    }
  });
}
