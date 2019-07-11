from SIGEN.app import app
from SIGEN.routes import ROUTES

for route in ROUTES:
    app.add_url_rule(route[0], route[1], route[2])

if __name__ == '__main__':
    app.run(port='5000')
