# ruff: noqa: D100

from django.urls import path

from tests.framework_integrations.callbacks.apps.django_callbacks_a_app import (
    callbacks,
)
from tests.framework_integrations.webhooks.apps.django_webhooks_app import (
    webhooks,
)

urlpatterns = [
    path("webhooks", webhooks),
    path("callbacks", callbacks),
]
