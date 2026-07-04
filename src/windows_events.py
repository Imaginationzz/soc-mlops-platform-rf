WINDOWS_EVENTS = {
    4624: {
        "name": "Successful Logon",
        "severity": "Low"
    },

    4625: {
        "name": "Failed Logon",
        "severity": "Medium"
    },

    4672: {
        "name": "Special Privileges Assigned",
        "severity": "High"
    }
}


def describe_event(event_id: int):

    event = WINDOWS_EVENTS.get(event_id)

    if event is None:
        return "Unknown Event"

    return f"{event_id} - {event['name']} ({event['severity']})"


if __name__ == "__main__":

    print(describe_event(4624))
    print(describe_event(4625))
    print(describe_event(4672))