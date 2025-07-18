from cydb_app import CydbApp


def init_app(app: CydbApp) -> None:
    from flask_cors import CORS

    from controllers.service_api import bp as service_api_bp

    CORS(
        service_api_bp,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    )

    app.register_blueprint(service_api_bp)
