def deploy():
    """Run deployment tasks."""
    from app import create_app, db
    from flask_migrate import upgrade, migrate, init, stamp
    from models import Paragraphs

    app = create_app()
    app.app_context().push()

    db.create_all()

    stamp()
    migrate()
    upgrade()

deploy()