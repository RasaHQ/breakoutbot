## happy test path
* greet: hello
  - utter_greet
* help: can i get help please
  - utter_help
* hint: could you give me a hint
  - utter_hint
* look: look at the [window](object)
  - action_look
* pickup: pick up the [key](object)
  - action_pickup
  - slot{"key": true}
* pickup: pick up the [poster](object)
  - action_pickup
  - slot{"poster": true}
* inventory: what is in my inventory now
  - action_inventory
