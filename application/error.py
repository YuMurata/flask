class InternalServerError:
    code = 500

    @classmethod
    def handler(cls, error):
        return ('internal_server_error', cls.code)


error_list = [InternalServerError]
