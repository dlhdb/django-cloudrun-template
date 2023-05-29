import firebase_admin
from firebase_admin import firestore
import threading


class FirebaseHelper:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, service_account_file=None):
        if cls._instance is None:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._init(service_account_file)

        return cls._instance

    def _init(self, service_account_file=None):
        if service_account_file is None:
            # use default service account file
            self._default_app = firebase_admin.initialize_app()
        else:
            self._default_app = firebase_admin.initialize_app(
                credential=firebase_admin.credentials.Certificate(service_account_file))
        self._firestore = firestore.client(self._default_app)

    @property
    def firestore(self):
        return self._firestore
