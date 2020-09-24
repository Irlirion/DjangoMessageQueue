# DjangoMessageQueue
## Install
1. Install Django: `python -m pip install Django`
2. Clone repo: `git clone https://github.com/Irlirion/DjangoMessageQueue.git`
3. Go to server directory: `cd DjangoMessageQueue`
4. Run server: `py manage.py runserver`

## Usage
1. Send POST request to your_site_url/register/
2. Get JSON request with "uuid" and save it
3. Send POST request to your_site_url/get_clients/
4. Get JSON request with client`s uuides, choose one and save it 
5. Send POST request to your_site_url/send_message/ with "from_uuid", "to_uuid", "message" ("from_uuid" from 1 step, "to_uuid" from 4 step)
6. Send POST request to your_site_url/get_messages/ with "uuid" from 2 step
7. Get JSON request with your messages :0
8. Enjoy :3
