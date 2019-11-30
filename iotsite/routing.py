from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
#import chat.routing
#import vehicles.routing
import sensors.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            sensors.routing.websocket_urlpatterns
            #chat.routing.websocket_urlpatterns
            #+ vehicles.routing.websocket_urlpatterns
        )
    ),
})
