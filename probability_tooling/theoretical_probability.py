class Event:
    def __init__(self, special_event, events):
        self.special_event = special_event
        self.events = events

    def event_prob(self):
        return (self.special_event/self.events) * 100
