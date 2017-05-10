from rest_framework.test import (APIRequestFactory, APITestCase, APITransactionTestCase)
from rest_framework import status
from django.urls import reverse
from users.models import (Guest, RestaurantManager)
from restaurant.models import (Restaurant, Table, Region, Reservation, Invite)
#from django.utils.dateparse import parse_datetime
from datetime import datetime, timedelta

from django.utils import timezone

# Create your tests here.

class GuestTest(APITestCase):

    def setUp(self):
        self.email = 'deyanbre@gmail.com'

        self.g1 = Guest.objects.create(username='aktivan', email=self.email, is_active=True, first_name='Aktii')
        self.g1.set_password('pass')
        self.g1.save()
        self.g2 = Guest.objects.create(username='neaktivan', email=self.email, is_active=False, first_name='Neaktiii')
        self.g2.set_password('pass')
        self.g2.save()
        #self.client.login(username='aktivan', password='pass')

        #print('g1 Aktivan:', self.g1.is_active)
        #print('g2 Aktivan:', self.g2.is_active)

        self.data = {'username': 'test_user',
        'password': 'pass',
        'first_name': 'test',
        'last_name': 'test_last',
        'email': 'deyanbre@gmail.com',
        'city': 'teslic'}

        self.client.post(reverse('guest-create'), self.data, format='json')


    def test_not_create_duplicated_guest(self):
        url = reverse('guest-create')

        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_non_activated(self):
        url = reverse('login-auth')
        data = {'username': 'neaktivan', 'password': 'pass'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)

    def test_login_activated(self):
        url = reverse('login-auth')
        data = {'username': 'aktivan', 'password': 'pass'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    
class ReservationTest(APITransactionTestCase):

    def setUp(self):
        self.email = 'deyanbre@gmail.com'
        self.g1 = Guest.objects.create(username='aktivan', email=self.email, is_active=True, first_name='Aktii')
        self.g1.set_password('pass')
        self.g1.save()

        self.login_data = {'username': 'aktivan', 'password': 'pass'}
        self.token = self.client.post(reverse('login-auth'), self.login_data, format='json')
        self.token = self.token.data['token']
        #print(self.token)

        self.rm = RestaurantManager.objects.create(username='rm', password='')
        self.r = Restaurant.objects.create(name='restaurant', owner=self.rm)
        self.region = Region.objects.create(restaurant=self.r)
        self.region2 = Region.objects.create(restaurant=self.r)
        self.table1 = Table.objects.create(region=self.region)
        self.table2 = Table.objects.create(region=self.region)
        self.table3 = Table.objects.create(region=self.region2)
        self.table4 = Table.objects.create(region=self.region2)

        #{"coming":"2017-05-02T23:34:00.000Z","duration":3,"restaurant":5,"reserved_tables":[264]}
        self.coming = timezone.now() + timedelta(hours=1)
        self.data = {'coming': self.coming, 'duration': 2, 'restaurant': self.r.id, 'reserved_tables': [self.table1.id]}

        self.data2_overlapping_after = {'coming': self.coming + timedelta(hours=1), 'duration': 2, 'restaurant': self.r.id, 'reserved_tables': [self.table1.id]}

        self.data2_overlapping_before = {'coming': self.coming - timedelta(hours=1), 'duration': 2, 'restaurant': self.r.id, 'reserved_tables': [self.table1.id]}

        self.data2_overlapping_between = {'coming': self.coming + timedelta(minutes=20), 'duration': 1, 'restaurant': self.r.id, 'reserved_tables': [self.table1.id]}

        self.data_multiple_tables = {'coming': self.coming, 'duration': 2, 'restaurant': self.r.id, 'reserved_tables': [self.table1.id, self.table2.id, self.table3.id]}

    def test_make_one_reservation(self):
        url = reverse('reservation-create')
        
        response = self.client.post(url, self.data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        #print(url, ':', response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_make_multiple_reservations_same_time(self):
        url = reverse('reservation-create')
        #print('########jedan####')
        response1 = self.client.post(url, self.data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        #print('########dva####')
        response2 = self.client.post(url, self.data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        #print('########tri####')

        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST, response2.data)
        #self.assertEqual()

    def test_make_multiple_reservations_overlapping_after(self):
        url = reverse('reservation-create')

        response1 = self.client.post(url, self.data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        response2 = self.client.post(url, self.data2_overlapping_after, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))

        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST, response2.data)

    def test_make_multiple_reservations_overlapping_before(self):
        url = reverse('reservation-create')

        response1 = self.client.post(url, self.data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        response2 = self.client.post(url, self.data2_overlapping_before, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))

        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST, response2.data)

    def test_make_multiple_reservations_overlapping_between(self):
        url = reverse('reservation-create')

        response1 = self.client.post(url, self.data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        response2 = self.client.post(url, self.data2_overlapping_between, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))

        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST, response2.data)

    def test_make_reservation_multiple_tables(self):
        url = reverse('reservation-create')

        response = self.client.post(url, self.data_multiple_tables, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    
    def test_make_reservation_multiple_tables_overlapping_same(self):
        url = reverse('reservation-create')
        print('r1:', timezone.now())
        response1 = self.client.post(url, self.data_multiple_tables, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        print('r1:', timezone.now())
        response2 = self.client.post(url, self.data_multiple_tables, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED, response1.data)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST, response2.data)

    
    def test_make_reservation_multiple_tables_overlapping_after(self):
        url = reverse('reservation-create')

        response1 = self.client.post(url, self.data_multiple_tables, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        self.data_multiple_tables['coming'] += timedelta(hours=1)
        response2 = self.client.post(url, self.data_multiple_tables, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED, response1.data)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST, response2.data)
    
    def test_make_reservation_multiple_tables_overlapping_before(self):
        url = reverse('reservation-create')

        response1 = self.client.post(url, self.data_multiple_tables, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        self.data_multiple_tables['coming'] -= timedelta(hours=1)
        response2 = self.client.post(url, self.data_multiple_tables, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED, response1.data)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST, response2.data)


    def test_make_reservation_multiple_tables_overlapping_between(self):
        url = reverse('reservation-create')

        response1 = self.client.post(url, self.data_multiple_tables, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        self.data_multiple_tables['coming'] += timedelta(minutes=20)
        self.data_multiple_tables['duration'] = 1
        response2 = self.client.post(url, self.data_multiple_tables, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED, response1.data)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST, response2.data)

    
    def test_make_reservation_multiple_tables_overlapping_full(self):
        url = reverse('reservation-create')

        response1 = self.client.post(url, self.data_multiple_tables, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        self.data_multiple_tables['coming'] -= timedelta(minutes=20)
        self.data_multiple_tables['duration'] = 4
        response2 = self.client.post(url, self.data_multiple_tables, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED, response1.data)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST, response2.data)





class InvitesTest(APITransactionTestCase):

    def setUp(self):
        self.email = 'deyanbre@gmail.com'
        self.g1 = Guest.objects.create(username='aktivan', email=self.email, is_active=True, first_name='Aktii')
        self.g1.set_password('pass')
        self.g1.save()

        self.g2 = Guest.objects.create(username='aktivan2', email=self.email, is_active=True, first_name='Aktii')
        self.g2.set_password('pass')
        self.g2.save()

        self.login_data = {'username': 'aktivan', 'password': 'pass'}
        self.token1 = self.client.post(reverse('login-auth'), self.login_data, format='json')
        self.token1 = self.token1.data['token']

        self.login_data = {'username': 'aktivan2', 'password': 'pass'}
        self.token2 = self.client.post(reverse('login-auth'), self.login_data, format='json')
        self.token2 = self.token2.data['token']

        self.rm = RestaurantManager.objects.create(username='rm', password='')
        self.r = Restaurant.objects.create(name='restaurant', owner=self.rm)
        self.region = Region.objects.create(restaurant=self.r)
        self.region2 = Region.objects.create(restaurant=self.r)
        self.table1 = Table.objects.create(region=self.region)

        self.coming = timezone.now() + timedelta(hours=1)
        self.data = {'coming': self.coming, 'duration': 2, 'restaurant': self.r.id, 'reserved_tables': [self.table1.id]}
        
        #self.data = {'reservation': }

        self.url1 = reverse('reservation-create')
        self.url2 = reverse('invite-create')

    def test_send_invite(self):
        response1 = self.client.post(self.url1, self.data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED, response1.data)

        invite_data = {'reservation': response1.data['id'], 'guests': [self.g2.id]}
        response2 = self.client.post(self.url2, invite_data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED, response2.data)

    def test_send_invite_twice_for_same_reservation(self):
        response1 = self.client.post(self.url1, self.data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED, response1.data)

        invite_data = {'reservation': response1.data['id'], 'guests': [self.g2.id]}
        response2 = self.client.post(self.url2, invite_data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED, response2.data)

        response3 = self.client.post(self.url2, invite_data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response3.status_code, status.HTTP_400_BAD_REQUEST, response3.data)

    def test_send_invite_and_accept(self):
        response1 = self.client.post(self.url1, self.data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED, response1.data)

        invite_data = {'reservation': response1.data['id'], 'guests': [self.g2.id]}
        response2 = self.client.post(self.url2, invite_data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED, response2.data)

        confirm_invite_url = reverse('invites-confirm', kwargs={'id':response2.data['id']})
        #print(confirm_invite_url)
        confirm_data = {'confirm': True}
        response3 = self.client.post(confirm_invite_url, confirm_data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token2))
        self.assertEqual(response3.status_code, status.HTTP_200_OK, response3.data)


    def test_send_invite_and_accept_and_cancel(self):
        response1 = self.client.post(self.url1, self.data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED, response1.data)

        invite_data = {'reservation': response1.data['id'], 'guests': [self.g2.id]}
        response2 = self.client.post(self.url2, invite_data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED, response2.data)

        confirm_invite_url = reverse('invites-confirm', kwargs={'id':response2.data['id']})
        confirm_data = {'confirm': True}
        response3 = self.client.post(confirm_invite_url, confirm_data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token2))
        self.assertEqual(response3.status_code, status.HTTP_200_OK, response3.data)

        confirm_data = {'confirm': False}
        response4 = self.client.post(confirm_invite_url, confirm_data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token2))
        self.assertEqual(response4.status_code, status.HTTP_400_BAD_REQUEST, response4.data)


    def test_unauthorized_invite_confirmation(self):
        response1 = self.client.post(self.url1, self.data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED, response1.data)

        invite_data = {'reservation': response1.data['id'], 'guests': [self.g2.id]}
        response2 = self.client.post(self.url2, invite_data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED, response2.data)

        confirm_invite_url = reverse('invites-confirm', kwargs={'id':response2.data['id']})
        confirm_data = {'confirm': True}
        response3 = self.client.post(confirm_invite_url, confirm_data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response3.status_code, status.HTTP_401_UNAUTHORIZED, response3.data)


    def test_cancel_invite_on_time(self):
        self.data['coming'] = timezone.now() + timedelta(minutes=29)
        response1 = self.client.post(self.url1, self.data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED, response1.data)

        invite_data = {'reservation': response1.data['id'], 'guests': [self.g2.id]}
        response2 = self.client.post(self.url2, invite_data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED, response2.data)

        confirm_invite_url = reverse('invites-confirm', kwargs={'id':response2.data['id']})
        confirm_data = {'confirm': False}
        response3 = self.client.post(confirm_invite_url, confirm_data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token2))
        self.assertEqual(response3.status_code, status.HTTP_400_BAD_REQUEST, response3.data)


    def test_invite_list(self):
        self.data['coming'] = timezone.now() + timedelta(minutes=50)
        response1 = self.client.post(self.url1, self.data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED, response1.data)

        invite_data = {'reservation': response1.data['id'], 'guests': [self.g2.id]}
        response2 = self.client.post(self.url2, invite_data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token1))
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED, response2.data)

        response3 = self.client.get(reverse('invites-my'), format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token2))
        self.assertEqual(len(response3.data), 1, response3.data)

