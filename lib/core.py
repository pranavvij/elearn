res = {
    '200':'Ok',
    '501':'Internal Server error',
    '401':'Unauthorized User',
    '405':'Method not allowed'
}

def respond(type):
    response = {}
    if type in res.keys():
        response['code'] = type
        response['message'] = res[type]
    else:
        response['code'] = type
        response['message'] = 'Something went wrong'
    return response