from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookTests(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            published_date="2023-01-01",
            isbn="1234567890123",
            pages=200,
            cover="http://example.com/cover.jpg",
            language="English"
        )
        self.list_url = reverse('book-list-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'published_date': '2024-01-01',
            'isbn': '9876543210123',
            'pages': 300,
            'cover': 'http://example.com/new_cover.jpg',
            'language': 'French'
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(pk=response.data['id']).title, 'New Book')

    def test_get_book_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        data = {
            'title': 'Updated Book',
            'author': 'Test Author',
            'published_date': '2023-01-01',
            'isbn': '1234567890123',
            'pages': 200,
            'cover': 'http://example.com/cover.jpg',
            'language': 'English'
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book.pk).title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
