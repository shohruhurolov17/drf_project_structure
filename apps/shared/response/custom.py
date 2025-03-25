from rest_framework import status, response


class CustomResponse(response.Response):

    def __init__(self, success=True, message=None, data=None, status=status.HTTP_200_OK, **kwargs):

        response = {
            "success": success,
            **({"message": message} if message else {}),
            **({"data": data} if data else {}),
        }

        super().__init__(response, status, **kwargs)