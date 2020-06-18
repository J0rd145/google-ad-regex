import random
import string
import re

def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters.lower() + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

def gen_google_ad_url(randomAlphaNumeric = get_random_alphaNumeric_string(8)):
    return f"r{random.randint(1, 9)}---sn-{randomAlphaNumeric}.googlevideo.com"


def url_match(URL=gen_google_ad_url(), regex="(r[0-9]---sn-)([a-z0-9]*)(\.googlevideo\.com$)"):
    x = re.findall(regex, URL)
    match = {
        "url": URL,
        "result": x
    }
    return match

def validate_url(results = url_match()):
    result = (results.get("result")[0])
    print(result)

validate_url()