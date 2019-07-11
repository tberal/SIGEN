import SIGEN.views as views


ROUTES = [
        ('/', 'upload', views.UploadView.as_view('upload')),
        ('/map', 'map', views.MapView.as_view('map')),
        ]

