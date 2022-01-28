from django.test import TestCase
from .models import Session
from django.utils import timezone
from django.urls import reverse
from .forms import SessionForm
# from .views import session_list_view

# Create your tests here.

# Testing Model


class SessionTest(TestCase):

    def create_session(self, session='2025/2026', is_current_session=False):
        return Session.objects.create(session=session, is_current_session=is_current_session)

    def test_session_creation(self):
        w = self.create_session()
        self.assertTrue(isinstance(w, Session))
        self.assertEqual(w.__str__(), w.session)

