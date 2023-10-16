import requests
import numpy as np
import datetime
class stellarium_api():
    
    def __init__(self, address = 'http://localhost:8090',
                    lat = -30.7249,
                    lon = 21.45714,
                    altitude = 1086,
                    name = 'meerkat_site',
                    country = 'South Africa'):
        """interfacing class for a stellarium program with remote control enabled

        Args:
            address (str, optional): the uri address for the stellarium program. Defaults to 'http://localhost:8090'.
            lat (float, optional): the latitude location to set. Defaults to -30.7249.
            lon (float, optional): the longitude location to set. Defaults to 21.45714.
            altitude (int, optional): the altitude to set (in meter). Defaults to 1086.
            name (str, optional): the name to give the location. Defaults to 'meerkat_site'.
        """
        self.address = address
        self.lat = lat
        self.lon = lon
        self.altitude = altitude
        self.loc_name = name
        self.country = country
        
    def ping(self):
        """ping the stellarium api

        Returns:
            dict: empty if not available otherwise the current status
        """
        r = requests.get(self.address + '/api/main/status')
        if r.status_code != 200:
            return {}
        else:
            return r.json()

    def get_status(self):
        """get current status in stellarium

        Returns:
            dict: status of the program as dict
        """
        r = requests.get(self.address + '/api/main/status')
        r.raise_for_status()
        return r.json()
    
    def set_loc(self):
        """set the location as given during construction to the stellarium api
        """


        r = requests.post(self.address + '/api/location/setlocationfields', params = {                      
            'latitude': self.lat,
            'longitude': self.lon,
            'altitude': self.altitude,
            'name': self.loc_name,
            'country': self.country
        })
        r.raise_for_status()


    def set_boresight(self, az, el):
        """set the boresight location

        Args:
            az (float): azimuth position in DEGREE
            el (float): elevation position in DEGREE
        """
        az = (180 - az) % 360 # stellarium az definition != mke az definition MKE 0 = North +90 = East
        r = requests.post(self.address + '/api/main/view', params={'az': np.deg2rad(az), 'alt': np.deg2rad(el)})
        r.raise_for_status()


    def move_boresight(self, x, y):
        """joystick like move the boresight (setting an angular speed)

        Args:
            x (float): number -1...+1 with neg = move left and pos = move right
            y (float): number -1...+1 with neg = move down pos = move up
        """
        r = requests.post(self.address + '/api/main/move', params={'x': np.clip(x, -1, 1), 'y': np.clip(y, -1, 1)})
        r.raise_for_status()


    def set_time(self, time):
        """set the internal time in stellarium

        Args:
            time (astropy.time.Time): the internal telescope time
        """
        r = requests.post(self.address + '/api/main/time', params={'time': time.jd})
        r.raise_for_status()

    def run(self, scu_api, verb=True):
        """
            runs a continious feedthrough interface to 
            translate between a Meerkat Extension Dish 
            and Stellarium. 
        Args:
            scu_api (mke_sculib.scu.scu): an MKE scu object
        """
        if verb: 
            print('initializing contact with app...')
            
        
        status = self.ping()
        if not status:
            raise ConnectionError('Could not connect to the stellarium program. Make sure the program is running and has remote control plugin enabled')
        if verb:
            print('--> OK')
            print('current status ins stellarium:')
            print(status)
            print('Setting config...')
        self.set_time(scu_api.t_internal)
        self.set_loc()
        if verb:
            print('--> OK')
            print('current status ins stellarium:')
            print(self.get_status())
            print('starting periodic update...')
            print('')
            print(' TIME (UTC)          | AZIMUTH (deg) | ELEVATION (deg) | FPS')
        t = datetime.datetime.utcnow()
        while 1:
            az, el = scu_api.azel
            if verb:
                t_last = t
                t = datetime.datetime.utcnow()
                dt = abs((t - t_last).total_seconds())
                fps = 0. if dt <= 0 else 1/dt
                print(' {} | {: 10.4f}    | {: 10.4f}      | {: 4.2f}'.format(t.isoformat().split('.')[0], az % 360, el, fps), end='\r')
            self.set_boresight(az, el)


if __name__ == "__main__":
    
    from mke_sculib.scu import scu as scu_api
    api = stellarium_api()

    # print(api.ping())
    # print('done')
    # for az in [0, 90, 180, 270, 360]:
    #     api.set_boresight(az, 0)
    #     a = input(str(az) + ' press enter')

    # for el in [0, 12, 35, 65, 90]:
    #     api.set_boresight(az, el)
    #     a = input(str(el) + ' press enter')


    # api.run(scu_api('http://10.98.76.45:8997'))
    api.run(scu_api('http://localhost:8080'))