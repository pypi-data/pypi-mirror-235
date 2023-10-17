import logging
from datetime import datetime, timedelta

import pytz
import requests
import urllib3

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# noinspection RequestsNoVerify
class FeatureToggleUi:
    def __init__(self, url, username, password):
        self.url = str(url)
        self.username = str(username)
        self.password = str(password)
        self.headers = {
            'Content-Type': 'application/json',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept': '*/*',
            'Connection': 'close',
        }

    def search_features(self):
        """Not implemented"""
        raise NotImplementedError
        pass

    def search_feature(self):
        """Not implemented"""
        raise NotImplementedError
        pass

    def create_feature(self, ft, data):
        """
        Creating Feature
        :param ft:  Name of Feature
        :param data: Json Data for creating Feature
        :return: Status Code
        """
        logging.info(f"Creating {ft} at {self.url}")
        response = requests.post(
            self.url,
            headers=self.headers,
            json=data,
            verify=False,
            auth=(self.username, self.password),
        )
        if response.status_code == 201:
            logging.info(f"{ft} added")
        elif response.status_code == 500:
            logging.warning(f"{ft} already exists")
        else:
            logging.error({response.status_code, response.text})
            input("Press Enter to continue...\n")
        return response.status_code

    def delete_feature(self, ft):
        """
        Deleting Feature
        :param ft: Name of Feature
        :return: Status Code
        """
        raise NotImplementedError
        logging.info(f"Deleting {ft} at {self.url}")
        response = requests.delete(
            f'{self.url}/{ft}',
            headers=self.headers,
            verify=False,
            auth=(self.username, self.password),
        )
        if response.status_code == 200:
            dt = datetime.now(tz=pytz.timezone('Europe/Moscow'))
            dt = dt + timedelta(days=14)
            logging.info(f"{ft} will be removed at {dt.strftime('%H:%M, %d.%m.%Y')}")
        else:
            logging.error({response.status_code, response.text})
            input("Press Enter to continue...\n")
        return response.status_code

    def restore_feature(self, ft):
        """
        Remove flag in Feature for deleting
        :param ft: Name of Feature
        :return: Status Code
        """
        raise NotImplementedError
        logging.info(f"Removing delete flag for {ft} at {self.url}")
        response = requests.patch(
            f'{self.url}/{ft}',
            headers=self.headers,
            verify=False,
            auth=(self.username, self.password),
        )
        if response.status_code == 200:
            logging.info(f"Deletion of {ft} reverted")
        else:
            logging.error({response.status_code, response.text})
            input("Press Enter to continue...\n")
        return response.status_code

    def create_user_list(self, ft):
        """
        Creating empty user list in Feature
        :param ft: Name of Feature
        :return: Status Code
        """
        logging.info(f"Creating user list in {ft} at {self.url}")
        response = requests.post(
            f'{self.url}/{ft}/users',
            headers=self.headers,
            json=[],
            verify=False,
            auth=(self.username, self.password),
        )
        if response.status_code == 200:
            logging.info(f"User list successful added to {ft}")
        else:
            logging.error({response.status_code, response.text})
            input("Press Enter to continue...\n")
        return response.status_code

    def add_user_to_feature(self, ft, data):
        """
        Adding users to Feature
        :param ft: Name of Feature
        :param data: List of users
        :return: Status Code
        """
        logging.info(f"Adding users to {ft} at {self.url}")
        response = requests.put(
            f'{self.url}/{ft}/users',
            headers=self.headers,
            json=data,
            verify=False,
            auth=(self.username, self.password),
        )
        if response.status_code == 200:
            logging.info(f"User successful added to {ft}")
        elif response.status_code == 400:
            logging.warning(f"Incorrect user list")
        elif response.status_code == 500:
            logging.warning(f"Incorrect feature name")
        else:
            logging.error({response.status_code, response.text})
            input("Press Enter to continue...\n")
        return response.status_code

    def remove_user_from_feature(self, ft, data):
        """
        Removing user from Feature
        :param ft: Name of Feature
        :param data:
        :return: Status Code
        """
        raise NotImplementedError
        logging.info(f"Removing users from {ft} at {self.url}")
        response = requests.delete(
            f'{self.url}/{ft}/users',
            headers=self.headers,
            json=data,
            verify=False,
            auth=(self.username, self.password),
        )
        if response.status_code == 200:
            logging.info(f"User successful removed from {ft}")
        elif response.status_code == 400:
            logging.warning(f"Incorrect user list")
        else:
            logging.error({response.status_code, response.text})
            input("Press Enter to continue...\n")
        return response.status_code
