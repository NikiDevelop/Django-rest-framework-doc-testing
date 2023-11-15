import pytest
from api.models import User

# Creamos un usuario 
# Comprobamos si se ha creado y si tiene el mismo nombre que le pasamos 
@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create(
        name='Lucia',
        nickName='Luci30',
        age=30,
        is_active=True
    )
    assert user.name == 'Lucia'
# 1 passed: nos dice que nuestro test ha pasado

