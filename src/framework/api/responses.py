from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict


def validation_error_response(errors: ReturnDict) -> Response:
    return Response(
        {
            "errors": errors,
        },
        status=400,
    )
