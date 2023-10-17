import requests

class MIDJ:
    def __init__(self, config={}):
        self.baseURL = config.get('baseURL', 'https://api.midj.app')
        self.authorization = config.get('authorization')  # Add 'authorization' argument here
        if not self.authorization:
            raise ValueError("Authorization is required.")

    def generate(self, prompt):
        try:
            response = requests.post(
                f"{self.baseURL}/api/generate",
                json={'prompt': prompt},
                headers={'Authorization': self.authorization}
            )
            return response.json()
        except requests.exceptions.RequestException as error:
            return {'error': str(error)}

    def pregenerate(self, prompt):
        try:
            response = requests.post(
                f"{self.baseURL}/pre/generate",
                json={'prompt': prompt},
                headers={'Authorization': self.authorization}
            )
            return response.json()
        except requests.exceptions.RequestException as error:
            return {'error': str(error)}

    def get_by_trigger(self, trigger_id):
        try:
            response = requests.post(
                f"{self.baseURL}/api/getByTrigger",
                json={'trigger_id': trigger_id},
                headers={'Authorization': self.authorization}
            )
            return response.json()
        except requests.exceptions.RequestException as error:
            return {'error': str(error)}

    def generate_variation(self, index, trigger_id, msg_hash):
        try:
            response = requests.post(
                f"{self.baseURL}/api/variation",
                json={'index': index, 'trigger_id': trigger_id, 'msg_hash': msg_hash},
                headers={'Authorization': self.authorization}
            )
            return response.json()
        except requests.exceptions.RequestException as error:
            return {'error': str(error)}

    def pregenerate_variation(self, index, trigger_id, msg_hash):
        try:
            response = requests.post(
                f"{self.baseURL}/pre/variation",
                json={'index': index, 'trigger_id': trigger_id, 'msg_hash': msg_hash},
                headers={'Authorization': self.authorization}
            )
            return response.json()
        except requests.exceptions.RequestException as error:
            return {'error': str(error)}

    def upscale_image(self, index, trigger_id, msg_hash):
        try:
            response = requests.post(
                f"{self.baseURL}/api/upscale",
                json={'index': index, 'trigger_id': trigger_id, 'msg_hash': msg_hash},
                headers={'Authorization': self.authorization}
            )
            return response.json()
        except requests.exceptions.RequestException as error:
            return {'error': str(error)}

    def preupscale_image(self, index, trigger_id, msg_hash):
        try:
            response = requests.post(
                f"{self.baseURL}/pre/upscale",
                json={'index': index, 'trigger_id': trigger_id, 'msg_hash': msg_hash},
                headers={'Authorization': self.authorization}
            )
            return response.json()
        except requests.exceptions.RequestException as error:
            return {'error': str(error)}
