    from datetime import datetime, timedelta
    from cal_setup import get_calendar_service


    def main():
        # update the event to tomorrow 9 AM IST
        service = get_calendar_service()

        d = datetime.now().date()
        tomorrow = datetime(d.year, d.month, d.day, 9)+timedelta(days=1)
        start = tomorrow.isoformat()
        end = (tomorrow + timedelta(hours=2)).isoformat()

        event_result = service.events().update(
          calendarId='household chores',
          eventId='<place your event ID here>',
          body={
           "summary": 'Updated Family calendar',
           "description": 'For distribution of childcare & housework',
           "start": {"dateTime": start, "timeZone": 'Asia/HongKong'},
           "end": {"dateTime": end, "timeZone": 'Asia/HongKong'},
           },
        ).execute()

        print("updated event")
        print("id: ", event_result['id'])
        print("summary: ", event_result['summary'])
        print("starts at: ", event_result['start']['dateTime'])
        print("ends at: ", event_result['end']['dateTime'])

    if __name__ == '__main__':