from requests_cache import CachedSession


class TrustTrackAPI:
    def __init__(self, api_key: str, version: int = 1):
        self.api_key = api_key
        self.session = CachedSession(expire_after=60, backend='memory')
        self.version = version

    def get_all_objects(self):
        params = {'version': self.version, 'api_key': self.api_key}
        response = self.session.get(url=TrustTrackURLs.get_objects_url(), params=params, expire_after=600)
        if response.status_code == 200:
            return response.json()

    def get_object_id_by_reg_number(self, reg_number: str):
        object_id = None
        objects = self.get_all_objects()
        for obj in objects:
            if obj['name'] == reg_number:
                object_id = obj['id']
                break
        return object_id

    def get_all_vehicles(self):
        objects = self.get_all_objects()
        vehicles = []
        for obj in objects:
            if len(str(obj['imei'])) == 15:
                vehicles.append(obj)
        return vehicles

    def get_all_trailers(self):
        objects = self.get_all_objects()
        vehicles = []
        for obj in objects:
            if len(str(obj['imei'])) == 6:
                vehicles.append(obj)
        return vehicles

class TrustTrackURLs:
    api_base_url = 'https://api.fm-track.com'

    @classmethod
    def get_objects_url(cls, object_id=None):
        if object_id:
            url = cls.api_base_url + '/objects/' + object_id
        else:
            url = cls.api_base_url + '/objects'
        return url

    @classmethod
    def get_object_coordinates_history_url(cls, object_id):
        return cls.api_base_url + '/objects/' + object_id + '/coordinates'

    @classmethod
    def get_object_trips(cls, object_id):
        return cls.api_base_url + '/objects/' + object_id + '/trips'

    @classmethod
    def get_drivers_url(cls, driver_id=None):
        if driver_id:
            url = cls.api_base_url + '/drivers/' + driver_id
        else:
            url = cls.api_base_url + '/drivers'
        return url

    @classmethod
    def get_events_history_url(cls):
        return cls.api_base_url + '/detected-events'

    @classmethod
    def get_fuel_events_url(cls):
        return cls.api_base_url + '/fuel-events'
