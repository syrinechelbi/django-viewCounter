from django.test import TestCase
from django.urls import reverse
from .models import Counter


class CounterModelTest(TestCase):
    def test_counter_creation(self):
        """
        Test que le modèle Counter est correctement créé avec les valeurs par défaut.
        """
        counter = Counter.objects.create(key="counter", value=0)
        self.assertEqual(counter.key, "counter")
        self.assertEqual(counter.value, 0)


class CounterViewTest(TestCase):
    def test_view_creates_counter_if_not_exists(self):
        """
        Test que la vue `index` crée un compteur s'il n'existe pas.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        counter = Counter.objects.get(key="counter")
        self.assertEqual(counter.value, 1)

    def test_view_increments_counter(self):
        """
        Test que la vue `index` incrémente la valeur du compteur s'il existe déjà.
        """
        counter = Counter.objects.create(key="counter", value=5)
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        counter.refresh_from_db()  # Actualise le modèle depuis la base de données
        self.assertEqual(counter.value, 6)

    def test_view_renders_template(self):
        """
        Test que la vue `index` utilise le bon template et passe le contexte attendu.
        """
        counter = Counter.objects.create(key="counter", value=2)
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "counter/index.html")
        self.assertContains(
            response, "3"
        )  # Vérifie que la valeur du compteur est passée au contexte
