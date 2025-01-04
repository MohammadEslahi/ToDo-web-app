from django.test import TestCase
from .models import Task, Category
from accounts.models import CustomUser


class TaskTestCase(TestCase):
    def setUp(self):
        test_author = CustomUser.objects.create_user(username='test_author', password='test_password', email='test@test.test')
        Task.objects.create(name='test_task_name', priority='high', author= test_author)
    
    def test_if_task_created(self):
        test_task_exists = Task.objects.filter(name='test_task_name').exists()
        self.assertTrue(test_task_exists)

    def test_task_priority_is_correct(self):
        test_task = Task.objects.get(name='test_task_name')
        self.assertEqual(test_task.priority, 'high')

    def test_default_checked_status(self):
        test_task = Task.objects.get(name='test_task_name')
        self.assertEqual(test_task.checked, False)

    def test_editing_tasks_priority(self):
        test_task = Task.objects.get(name='test_task_name')
        test_task.priority = 'low'
        test_task.save()
        self.assertEqual(test_task.priority, 'low')

    def test_editing_tasks_name(self):
        test_task = Task.objects.get(name='test_task_name')
        test_task.name = 'edited_test_task_name'
        test_task.save()
        self.assertEqual(test_task.name, 'edited_test_task_name')

    def test_task_category(self):
        test_author = CustomUser.objects.get(username='test_author')
        test_category = Category.objects.create(name='test_category', author=test_author)
        test_task = Task.objects.get(name='test_task_name')
        test_task.category = test_category
        test_task.save()
        self.assertEqual(test_task.category, test_category)

    def test_date_auto_add_now(self):
        test_task = Task.objects.get(name='test_task_name')
        self.assertIsNotNone(test_task.date_created)

    def test_editing_multiple_fields(self):
        test_task = Task.objects.get(name='test_task_name')
        test_task.name = 'edited_test_task_name'
        test_task.priority='medium'
        test_task.save()
        self.assertEqual(test_task.name, 'edited_test_task_name')
        self.assertEqual(test_task.priority, 'medium')




class CategoryTestCase(TestCase):
    def setUp(self):
        test_author = CustomUser.objects.create_user(username='test_author', password='test_password', email='test@test.test')
        Category.objects.create(name='test_category', author=test_author)
    
    def test_category_created(self):
        test_category_exists = Category.objects.filter(name='test_category').exists()
        self.assertTrue(test_category_exists)

    def test_category_author_is_set(self):
        test_category = Category.objects.get(name='test_category')
        self.assertEqual(test_category.author.username, 'test_author')
    
    def test_deleting_category(self):
        test_category = Category.objects.get(name='test_category')
        test_category.delete()
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(name='test_category')
