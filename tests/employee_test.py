import pytest
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class EmployeeTest(APITestCase):
    __data = {}
    __create_employee = {}

    @property
    def data_to_save(self):
        return self.__data_to_save

    @property
    def data_create_employee(self):
        return self.__data_create_employee

    @pytest.fixture
    def create_employee(self):
        from src.models import Employee

        employee = Employee(
            name="New Kaio",
            email="kaio_teco@hotmail.com",
            department="TI")
        employee.save()

        self.__data_create_employee = employee

    @pytest.fixture
    def setUp(self):
        self.client = APIClient()
        self.client.login(username='admin', password='default123')
        self.__data_to_save = {'name': 'Kaio', 'email': 'kaio.teco@gmail.com', 'department': 'WebDevelopment'}
        self.create_employee()

    @pytest.mark.django_db
    def test_create_employee(self):
        response = self.client.post('/api/employees/',
                                    self.__data_to_save,
                                    format='json',
                                    follow=True)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @pytest.mark.django_db
    def test_update_employee(self):
        response = self.client.put('/api/employees/' + format(self.__data_create_employee.id) + '/',
                                   self.__data_to_save,
                                   format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_get_employee(self):
        response = self.client.get('/api/employees/' + format(self.__data_create_employee.id) + '/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_get_employees(self):
        response = self.client.get('/api/employees/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_get_not_found(self):
        response = self.client.get('/api/employees/13/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @pytest.mark.django_db
    def test_delete(self):
        response = self.client.delete('/api/employees/' + format(self.__data_create_employee.id) + '/',
                                      {"id": self.__data_create_employee.id},
                                      format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, status.HTTP_200_OK)
