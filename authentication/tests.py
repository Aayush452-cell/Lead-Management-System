from django.test import TestCase
from .models import CustomUser,Leads

class ModelTesting(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(email="email@gmail.com", first_name="email", last_name="singh",
                                                 password="email@000")
        self.lead = Leads.objects.create(name="name",email="lead@gmail.com",status="cold",notes="new lead",sales_representative=self.user)

    def test_CustomUser_model(self):
        user = self.user
        self.assertTrue(isinstance(user, CustomUser))
        self.assertEqual(str(user), 'email@gmail.com')

    def test_Leads_model(self):
        lead = self.lead
        self.assertTrue(isinstance(lead, Leads))
        self.assertEqual(str(lead), 'leads@gmail.com')
