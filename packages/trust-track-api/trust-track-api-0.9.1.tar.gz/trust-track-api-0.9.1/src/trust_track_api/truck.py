from .trust_track_api import TrustTrackAPI, TrustTrackURLs
from datetime import datetime, timedelta
from pytz import utc


class Truck:
    def __init__(self, api: TrustTrackAPI, regNumber: str = None, object_id: str = None):
        self.api = api
        if object_id:
            self.object_id = object_id
        elif regNumber:
            self.object_id = self.api.get_object_id_by_reg_number(regNumber)
        else:
            self.object_id = None

    @staticmethod
    def __localize_from_to_dates(fromDate: datetime, toDate: datetime):
        if fromDate.tzinfo:
            fromDate = fromDate.astimezone(utc)
        else:
            utc.localize(fromDate)
        if not toDate:
            toDate = datetime.now(utc)
        if toDate.tzinfo:
            toDate = toDate.astimezone(utc)
        else:
            utc.localize(toDate)
        if toDate.astimezone(utc) > datetime.now(utc):
            toDate = datetime.now(utc)
        return fromDate, toDate

    def __get_truck_coordinate_by_date(self, date: datetime, version: int = 2):
        if date.tzinfo:
            date = date.astimezone(utc)
        else:
            utc.localize(date)

        url = (
                TrustTrackURLs.get_object_coordinates_history_url(self.object_id) + '/' +
                date.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        )
        params = {
            'version': version,
            'api_key': self.api.api_key
        }
        response = self.api.session.get(url=url, params=params)
        if response.status_code == 200:
            return [response.json()]

    def __get_truck_coordinates_by_period(self, fromDate: datetime, toDate: datetime = None,
                                          limit: int = 100, getAll: bool = False, version: int = 2):

        fromDate, toDate = self.__localize_from_to_dates(fromDate, toDate)

        url = TrustTrackURLs.get_object_coordinates_history_url(self.object_id)
        params = {
            'version': version,
            'api_key': self.api.api_key,
            'limit': limit,
            'from_datetime': fromDate.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            'to_datetime': toDate.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        }
        items = []
        while True:
            response = self.api.session.get(url=url, params=params)
            if response.status_code == 200:
                continuation_token = response.json()['continuation_token']
                if not continuation_token or not getAll:
                    items.extend(response.json()['items'])
                    break
                else:
                    items.extend(response.json()['items'])
                    params.update({'from_datetime': continuation_token})

            else:
                break
        return items

    def get_truck_details(self):
        params = {'version': self.api.version, 'api_key': self.api.api_key}
        response = self.api.session.get(url=TrustTrackURLs.get_objects_url(self.object_id), params=params,
                                        expire_after='DO_NOT_CACHE')
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_truck_coordinates(self, fromDate: datetime = None, toDate: datetime = None, date: datetime = None,
                              limit: int = 100, getAll: bool = False, version: int = 2):
        if date:
            items = self.__get_truck_coordinate_by_date(date, version)
        elif fromDate and toDate:
            items = self.__get_truck_coordinates_by_period(fromDate, toDate, limit, getAll, version)
        elif fromDate and not toDate:
            items = self.__get_truck_coordinates_by_period(fromDate, datetime.now(utc), limit, getAll, version)
        else:
            items = []
        return items

    def get_truck_trips(self, fromDate: datetime, toDate: datetime = None,
                        limit: int = 100, getAll: bool = False, version: int = 1):

        fromDate, toDate = self.__localize_from_to_dates(fromDate, toDate)

        params = {
            'version': version,
            'api_key': self.api.api_key,
            'limit': limit,
            'from_datetime': fromDate.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            'to_datetime': toDate.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        }
        items = []
        while True:
            response = self.api.session.get(url=TrustTrackURLs.get_object_trips(self.object_id), params=params)
            if response.status_code == 200:
                continuation_token = response.json()['continuation_token']
                if not continuation_token or not getAll:
                    items.extend(response.json()['trips'])
                    break
                else:
                    items.extend(response.json()['trips'])
                    params.update({'from_Datetime': continuation_token})

            else:
                break
        return items

    def get_truck_events_history(self, fromDate: datetime, toDate: datetime = None,
                                 limit: int = 100, getAll: bool = False, version: int = 1):

        fromDate, toDate = self.__localize_from_to_dates(fromDate, toDate)

        params = {
            'version': version,
            'api_key': self.api.api_key,
            'limit': limit,
            'object_id': self.object_id,
            'from_datetime': fromDate.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            'to_datetime': toDate.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        }
        items = []
        while True:
            response = self.api.session.get(url=TrustTrackURLs.get_events_history_url(), params=params)
            if response.status_code == 200:
                continuation_token = response.json()['continuation_token']
                if not continuation_token or not getAll:
                    items.extend(response.json()['events'])
                    break
                else:
                    items.extend(response.json()['events'])
                    params.update({'continuation_token': continuation_token})

            else:
                break
        return items

    def get_truck_fuel_events(self, fromDate: datetime, toDate: datetime = None,
                              limit: int = 100, getAll: bool = True, version: int = 1):

        fromDate, toDate = self.__localize_from_to_dates(fromDate, toDate)

        params = {
            'version': version,
            'api_key': self.api.api_key,
            'limit': limit,
            'object_id': self.object_id,
            'from_datetime': fromDate.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            'to_datetime': toDate.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        }
        items = []
        while True:
            response = self.api.session.get(url=TrustTrackURLs.get_fuel_events_url(), params=params)
            if response.status_code == 200:
                continuation_token = response.json()['continuation_token']
                if not continuation_token or not getAll:
                    items.extend(response.json()['items'])
                    break
                else:
                    items.extend(response.json()['items'])
                    params.update({'continuation_token': continuation_token})

            else:
                break
        return items

    def get_truck_fuel_consumption(self, fromDate: datetime, toDate: datetime):

        fromDate, toDate = self.__localize_from_to_dates(fromDate, toDate)

        fuel_events = self.get_truck_fuel_events(fromDate, toDate)
        data_at_start = self.__get_truck_coordinates_by_period(fromDate, fromDate + timedelta(minutes=40), limit=1)
        data_at_end = self.__get_truck_coordinates_by_period(
            toDate - timedelta(hours=3), toDate, limit=1000, getAll=True
        )
        fuel_at_start = 0.00
        fuel_at_end = 0.00
        fuel_during = 0.00
        if data_at_start and data_at_end:
            fuel_at_start = float(data_at_start[0]['inputs']['calculated_inputs']['fuel_level'])
            fuel_at_end = float(data_at_end[-1]['inputs']['calculated_inputs']['fuel_level'])
            for event in fuel_events:
                if event['event_type'] == 'REFUEL':
                    fuel_during = fuel_during + float(event['difference'])
                elif event['event_type'] == 'DRAIN':
                    fuel_during = fuel_during - float(event['difference'])

        return round(fuel_at_start + fuel_during - fuel_at_end, 2)
