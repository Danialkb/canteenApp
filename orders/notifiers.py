from ws_notifier.notifier import WebsocketNotifier


class OrderCreatedNotifier:

    def __init__(self):
        self.ws = WebsocketNotifier()

    def notify(self, user_id, order):
        self.ws.notify(
            {
                "type": "send_notification_to_user",
                "event": "order_created",
                "user_id": str(user_id),
                "order": order,
            },
            group=str(user_id),
        )
