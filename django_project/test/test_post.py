import pytest
from blog.factories import PostFactory

@pytest.fixture()
def Post_Published():
  return PostFactory(title='python with factories')

@pytest.mark.django_db
def test_create_published_post(Post_Published):
  assert Post_Published.title=='python with factories'
  


