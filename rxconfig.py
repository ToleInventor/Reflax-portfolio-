import reflex as rx

config = rx.Config(
    app_name="app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.PROD,  # Change to PROD for production
    telemetry_enabled=False,
    frontend_port=3000,
    backend_port=8000,
)
