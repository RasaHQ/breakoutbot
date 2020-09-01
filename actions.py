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


able_to_pick_up = ["key", "poster"]


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
                        dispatcher.utter_message(text=f"You've picked up the {item} and it is in your inventory.")

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


combinations = {
    ('key', 'door'): "Hey the key fits! Amazing! The door is now open.",
    ('poster', 'box'): "Why put the poster back in the box? You've just picked it up!",
    ('key', 'box'): "Why put the key back in the box? It's probably super useful.",
}
combinations.update({(i2, i1): v for (i1, i2), v in combinations.items()})


class ActionUse(Action):
    def name(self) -> Text:
        return "action_use"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = [e['value'] for e in tracker.latest_message['entities'] if e['entity'] == 'object']
        if len(entities) == 0:
            dispatcher.utter_message(text="I think you want to combine items but something is unclear.")
            dispatcher.utter_message(text="Could you retry and make sure you spelled the items correctly?.")
            return []
        elif len(entities) == 1:
            dispatcher.utter_message(text="I think you want to combine items but something is unclear.")
            dispatcher.utter_message(text=f"I could only make out that you wanted to use {entities[0]}.")
            dispatcher.utter_message(text="Could you retry and make sure you spelled the items correctly?.")
            return []
        elif len(entities) > 2:
            dispatcher.utter_message(text="I think you want to combine items but something is unclear.")
            dispatcher.utter_message(text=f"I could only make out that you wanted to combine {' and '.join(entities)}.")
            dispatcher.utter_message(text="You can only combine two items at a time.")
            return []
        # there are two items and they are confirmed 
        item1, item2 = entities
        if (item1, item2) in combinations.keys():
            dispatcher.utter_message(text=combinations[(item1, item2)])
        else:
            dispatcher.utter_message(text=f"I don't think combining {item1} with {item2} makes sense.")
        return []
