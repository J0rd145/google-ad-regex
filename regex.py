import random
import string
import re

def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters.lower() + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

def gen_google_ad_url(randomAlphaNumeric = get_random_alphaNumeric_string(8)):
    return f"r{random.randint(1, 9)}---sn-{randomAlphaNumeric}.googlevideo.com"

def url_match():
    URL = gen_google_ad_url()
    regex="(r[0-9]---sn-)([a-z0-9]*)(\.googlevideo\.com$)"
    x = re.findall(regex, URL)
    return x

def validate_url():
    result = url_match()
    if not result:
        return False
    if result == None:
        return False
    else:
        for match in result:
            if match == None:
                return False
    return True

def average_success_rate():
    successes = []
    failures = []
    for i in range(0, 5000):
        gen_result = validate_url()
        if gen_result == True:
            successes.append(gen_result)
        else:
            failures.append(gen_result)

    total_tests = len(successes) + len(failures)
    total_successes = len(successes)
    total_failures = len(failures)
    print("Total Success From 0 -",total_tests,"tests are:", total_successes)
    print("Total Failures From 0 -",total_tests,"tests are:", total_failures) 

if __name__ == "__main__":
    average_success_rate()