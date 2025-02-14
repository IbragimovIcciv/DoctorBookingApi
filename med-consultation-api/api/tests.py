import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import News, User
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user(db):
    return User.objects.create_user(username="test_user", email="test@gmail.com", password="1234", role="user")


@pytest.fixture
def create_news(db, create_user):
    return News.objects.create(
        user=create_user,
        title="Namunaviy Yangilik Sarlavhasi", # noqa
        img=SimpleUploadedFile("test_rasm.jpg", b"rasm_ma'lumotlari", content_type="image/jpeg"),
    )


def test_get_all_news(api_client, create_news):
    url = reverse("news-list")  # Bu yerda URL nomi sizning loyiha endpointingiz bilan mos bo'lishi kerak # noqa
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
    assert response.data[0]["title"] == "Namunaviy Yangilik Sarlavhasi" # noqa


def test_get_single_news(api_client, create_news):
    url = reverse("news-detail", kwargs={"pk": create_news.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "Namunaviy Yangilik Sarlavhasi" # noqa
    assert "img" in response.data


def test_img_field_absence(api_client, db, create_user):
    news = News.objects.create(user=create_user, title="Rasmsiz Yangilik") # noqa
    url = reverse("news-detail", kwargs={"pk": news.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["img"] is None
