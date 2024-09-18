from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionBookSlot(Action):
    def name(self) -> str:
        return "action_book_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        # Retrieve values from slots
        doctor = tracker.get_slot('doctor')
        time = tracker.get_slot('time')

        if doctor and time:
            dispatcher.utter_message(text=f"Your appointment with {doctor} has been booked for {time}.")
        else:
            dispatcher.utter_message(text="Please select both a doctor and a time slot.")
        return []


class ActionProvideDoctorOptions(Action):
    def name(self) -> str:
        return "action_provide_doctor_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        doctors = ["Dr. Smith", "Dr. Johnson", "Dr. Lee"]
        dispatcher.utter_message(
            text="Here are the doctors available. Please select one:",
            buttons=[
                {"title": doctor, "payload": f"/select_doctor{{\"doctor\":\"{doctor}\"}}"}
                for doctor in doctors
            ]
        )
        return []


class ActionProvideTimeSlots(Action):
    def name(self) -> str:
        return "action_provide_time_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        doctor = tracker.get_slot('doctor')
        if doctor:
            time_slots = ["10:00 AM", "11:00 AM", "01:00 PM", "03:00 PM"]
            dispatcher.utter_message(
                text=f"Here are the available time slots for {doctor}. Please choose one:",
                buttons=[
                    {"title": slot, "payload": f"/select_time_slot{{\"time\":\"{slot}\"}}"}
                    for slot in time_slots
                ]
            )
        else:
            dispatcher.utter_message(text="Please select a doctor first.")
        return []
