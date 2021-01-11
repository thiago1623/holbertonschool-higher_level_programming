#!/usr/bin/python3
#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""


if __name__ == "__main__":
    """request"""
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
