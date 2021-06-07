from django.shortcuts import render
from django.conf import settings

DEBUG = False


def private_chat_room_view(request, *args, **kwargs):
    room_id = request.GET.get("room_id")
    user = request.user
    if not user.is_authenticated:
        base_url = reverse('login')
        query_string = urlencode({'next': f"/chat/?room_id={room_id}"})
        url = f"{base_url}?{query_string}"
        return redirect(url)

    context = {}
    if room_id:
        context["room_id"] = room_id
    context['debug'] = DEBUG
    context['debug_mode'] = settings.DEBUG
    return render(request, 'messenger/messenger.html')
