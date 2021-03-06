DICT: dict = {
            200: {
                'status': 'OK',
                'detail': 'successfully'
                },
            201: {
                'status': 'Created',
                'detail': 'Created'
                },
            202: {
                'status': 'Accepted',
                'detail': 'Accepted'
                },
            206: {
                'status': "Partial Content",
                'detail': "Partial Content"
                },
            400: {
                'status': 'Bad Request',
                'detail': 'Bad Request'
                },
            401: {
                'status': 'Unauthorized',
                'detail': 'Unauthorized'
                },
            403: {
                'status': 'Forbidden',
                'detail': 'Forbidden'
                },
            404: {
                'status': 'Not Found',
                'detail': 'Not Found'
                },
            405: {
                'status': 'Method Not Allowed',
                'detail': 'Method Not Allowed'
                },
            408: {
                'status': 'Request Timeout',
                'detail': 'Request Timeout'
                },
            409: {
                'status': 'Conflict',
                'detail': 'Such user (flow) is already on the server.'
                },
            415: {
                'status': 'Unsupported Media Type',
                'detail': 'Unsupported Media Type'
                },
            417: {
                'status': 'Expectation Failed',
                'detail': 'Expectation Failed'
                },
            426: {
                'status': 'Upgrade Required',
                'detail': 'Upgrade Required'
                },
            429: {
                'status': 'Too Many Requests',
                'detail': 'Too Many Requests'
                },
            499: {
                'status': 'Client Closed Request',
                'detail': 'Client Closed Request'
                },
            500: {
                'status': 'Internal Server Error',
                'detail': 'Internal Server Error'
                },
            503: {
                'status': 'Service Unavailable',
                'detail': 'Service Unavailable'
                },
            520: {
                'status': 'Unknown Error',
                'detail': 'Unknown Error'
            },
            526: {
                'status': 'Invalid SSL Certificate',
                'detail': 'Invalid SSL Certificate'
                },
            }