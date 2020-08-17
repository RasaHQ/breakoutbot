from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

look_descriptions = {
    "window": "The window is shut sealed and it seems like I am on the 5th floor. Jumping out of the window seems dangerous.",
    "box": "It's a cardboard box. There's a poster inside of it and a key.",
    "key": "It's a standard issue key. It may just be the `key` to solving this level.",
    "door": "The door looks sturdy. It's locked.",
    "poster": "It's a poster of an Island full of Monkeys. Weird.",
    "room": "The room is completely empty. There's a window, a cardboard box and a door."
}

class ActionLook(Action):
    def name(self) -> Text:
        return "action_look"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        spoken = False
        for blob in tracker.latest_message['entities']:
            if blob['entity'] == 'object':
                dispatcher.utter_message(text=look_descriptions[blob['value']])
                spoken = True
        if not spoken:
            dispatcher.utter_message(text="Could you repeat what you're trying to look at?")
        return []


able_to_pick_up = ["key"]

class ActionPickUp(Action):
    def name(self) -> Text:
        return "action_pickup"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        items_to_add = []
        # We need to check what objects the user wants to pick up. We cannot pick up 
        # all objects and we need to check if the object is already in your inventory.
        for blob in tracker.latest_message['entities']:
            if blob['entity'] == 'object':
                item = blob['value']
                if item not in able_to_pick_up:
                    dispatcher.utter_message(text=f"You can't pick up {item}.")
                else:
                    item_in_inventory = tracker.get_slot(item)
                    if item_in_inventory:
                        dispatcher.utter_message(text=f"You already have {item} in your inventory.")
                    else:
                        items_to_add.append(SlotSet(item, True))
                        dispatcher.utter_message(text=f"You've picked up {item} and it is in your inventory.")
        
        # We could add multiple items here.
        if len(items_to_add) > 0:
            return items_to_add
        dispatcher.utter_message(text="Are you sure you spelled the item you wanted to pick up correctly?")
        return []


class ActionInventory(Action):
    def name(self) -> Text:
        return "action_inventory"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        items_in_inventory = [item for item in able_to_pick_up if tracker.get_slot(item)]
        if len(items_in_inventory) == 0:
            dispatcher.utter_message(text="There are no items in your inventory.")
            return []
        dispatcher.utter_message(text="These are the items in your inventory:")
        for item in items_in_inventory:
            dispatcher.utter_message(text=f"- {item}")
        return []
