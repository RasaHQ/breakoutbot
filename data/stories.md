## happy path
* greet
  - utter_greet
* help
  - utter_help
* look
  - action_look
* pickup
  - action_pickup
  - slot{"key": true}
* pickup
  - action_pickup
  - slot{"poster": true}
* inventory
  - action_inventory
* use
  - action_use

## hint hint path
* greet
  - utter_greet
* help
  - utter_help
* hint
  - utter_hint
* look
  - action_look

## also happy path
* greet
  - utter_greet
* inventory
  - action_inventory
* look
  - action_look
* pickup
  - action_pickup
  - slot{"poster": true}
* inventory
  - action_inventory
* pickup
  - action_pickup
  - slot{"key": true}
* inventory
  - action_inventory
* look
  - action_look
* use
  - action_use
