import pytest
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory, APITestCase


class EmployeeTest(APITestCase):
    __data = {}

    @property
    def data(self):
        return self.__data

    @pytest.fixture
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.client.login(username='admin', password='default123')
        self.__data = {'name': 'Kaio', 'email': 'kaio.teco@gmail.com', 'department': 'WebDevelopment'}

    @pytest.mark.django_db
    def test_create_employee(self):
        response = self.client.post('/api/employees/',
                                    self.__data,
                                    format='json',
                                    follow=True)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    """
    @pytest.mark.django_db
    def test_update_employee(self):
        from src.models import Employee
        self.__data = {'name': 'Kaio Edição', 'email': 'kaio.teco@gmail.com', 'department': 'Business'}

        response = self.client.put('/api/employees/'.format(Employee.objects.all().last().id) + '/',
                                   self.__data,
                                   format='json',
                                   content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_get_employee(self):
        from src.models import Employee

        response = self.client.get('/api/employee/'.format(Employee.objects.all().last().id) + '/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    """

    @pytest.mark.django_db
    def test_get_employees(self):
        response = self.client.get('/api/employees/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_get_not_found(self):
        response = self.client.get('/api/employees/46545456/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    @pytest.mark.django_db
    def test_delete(self):
        from src.models import Employee

        response = self.client.delete('/api/employees/'.format(Employee.objects.all().last().id) + '/',
                                      json.dumps({"id": Employee.objects.all().last().id}),
                                      format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    """