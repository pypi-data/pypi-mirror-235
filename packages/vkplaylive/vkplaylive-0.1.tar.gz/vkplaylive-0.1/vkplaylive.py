import base64
import aiohttp


class VKPLAPIClient:
    def __init__(self, client_id, secret):
        self.client_id = client_id
        self.secret = secret
        self.base_url = "https://api.vkplay.live/oauth/server/token"

    async def get_access_token(self):
        headers = {
            "Authorization": f"Basic {self.get_base64_credentials()}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials"
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url, headers=headers, data=data) as response:
                if response.status == 200:
                    response_data = await response.json()
                    return response_data.get("access_token")
                else:
                    print("Failed to get the application token")
                    return None

    def get_base64_credentials(self):
        credentials = f"{self.client_id}:{self.secret}"
        return base64.b64encode(credentials.encode()).decode()

    async def get_channel_info(self, access_token, channel_url):
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        params = {
            "channel_url": channel_url
        }

        async with aiohttp.ClientSession() as session:
            async with session.get("https://apidev.vkplay.live/v1/channel", headers=headers, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logger.info("Error in receiving channel information")
                    return None

