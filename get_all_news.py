from webapp import create_app
from webapp.python_org_news import get_python_news

app = create_app()
with app.app_context():
<<<<<<< HEAD
    get_python_news()
=======
    get_python_news()

>>>>>>> 2d28924be116e0be8960dbceb9c11ed6301da9fb
