from django.test import TestCase
import datetime

from django.utils import timezone
from django.urls import reverse

from .models import Poll


class PollModelTest(TestCase):
    def test_dummy(self):
        self.assertEqual(1, True)


# Create your tests here.
